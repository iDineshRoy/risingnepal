from student.views import (
    StudentView,
    # StudentListView,
    ParentView,
    StudentParentView,
    YearGradeSectionView,
    YearGradeSectionStudentView,
)

# ---------------------------------------------------- #

sv = StudentView()
pv = ParentView()
spv = StudentParentView()
ygs = YearGradeSectionView()
ygss = YearGradeSectionStudentView()
urlpatterns = (
    sv.url_patterns()
    + pv.url_patterns()
    + spv.url_patterns()
    + ygs.url_patterns()
    + ygss.url_patterns()
)
