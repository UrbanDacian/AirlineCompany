from Tests.TestCRUD import testAdaugaCheltuiala, testStergeCheltuiala, testModificaCheltuiala
from Tests.TestFunctionalitate1 import testCrestereClase
from Tests.TestFunctionalitate2 import testIeftinireCheltuiala
from Tests.TestFunctionalitate3 import testPretulMaxim
from Tests.TestFunctionalitate4 import testOrdonarePreturi
from Tests.TestFunctionalitate5 import testSuma


def runAllTests():
    testOrdonarePreturi()
    testIeftinireCheltuiala()
    testPretulMaxim()
    testCrestereClase()