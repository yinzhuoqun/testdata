from django.shortcuts import render

# Create your views here.

from django.views import generic
from testfly.models import *
from django.utils import timezone


class IndexView(generic.ListView):
    template_name = 'testfly/test_report_list.html'
    context_object_name = 'test_report_list'

    test_platform_choice = {
        "Android": "1",
        'iOS': "2",
        'other': "0",
    }
    # if platform in test_platform_choice.keys():
    #     choice_platform = test_platform_choice[platform]
    # test_report_list = TestReport.objects.all()

    def get_queryset(self):
        """Return the last five published questions."""
        return TestReport.objects.filter().order_by('-test_version')


def Platform(request, platform):
    template_name = 'testfly/test_report_platform.html'
    title = "%s | TestReport" % platform
    test_platform_choice = {
        "Android": "1",
        'iOS': "2",
        'other': "0",
    }
    if platform in test_platform_choice.keys():
        choice_platform = test_platform_choice[platform]

    test_report_platform = TestReport.objects.filter(test_platform=choice_platform).order_by('-test_version')

    return render(request, template_name, locals())


def Detail(request, platform, version):
    template_name = 'testfly/test_report_detail.html'
    title = "%s %s | TestReport" % (platform, version)
    test_platform_choice = {
        "Android": "1",
        'iOS': "2",
        'other': "0",
    }
    if platform in test_platform_choice.keys():
        choice_platform = test_platform_choice[platform]

    test_report = TestReport.objects.get(test_platform=choice_platform, test_version=version)
    test_docs = test_report.test_docs.strip("\n").split("\n")
    test_docs = filter(lambda x: len(x) > 2, test_docs)

    test_points = test_report.test_points.strip("\n").split("\n")
    test_points = filter(lambda x: len(x) > 2, test_points)

    test_risks = test_report.test_risks.strip("\n").split("\n")
    test_risks = filter(lambda x: len(x) > 2, test_risks)

    test_bug_info = test_report.buginfo_set.get(pk=test_report.id)

    from django.db.models import F, FloatField, Sum, Count, Max, Avg

    test_bug_surplus_info = test_report.bugsurplusinfo_set.get(pk=test_report.id)
    bug_surplus_total = test_bug_surplus_info.bug_surplus_block + test_bug_surplus_info.bug_surplus_major + \
        test_bug_surplus_info.bug_surplus_normal + test_bug_surplus_info.bug_surplus_trivial

    bug_total = test_bug_info.bug_block + test_bug_info.bug_major + \
                        test_bug_info.bug_normal + test_bug_info.bug_trivial

    test_participants = test_report.testparticipants_set.filter(test_participants_id=test_report.id)
    test_report_other = {"test_platform": platform, "test_points": test_points, "test_docs": test_docs,
                         "test_risks": test_risks}
    return render(request, template_name, locals())
