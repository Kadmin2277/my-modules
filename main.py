import colorPrint
import TypeVariable

string = TypeVariable.TypeVar("String", str)
colorPrint.ColorPrint.colorPrint(string, 'red')