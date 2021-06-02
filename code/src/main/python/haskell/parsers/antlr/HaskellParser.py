# Generated from HaskellParser.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\u008f")
        buf.write("\u0b87\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\tU\4V\t")
        buf.write("V\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4^\t^\4")
        buf.write("_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4g\tg\4")
        buf.write("h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\4o\to\4p\tp\4")
        buf.write("q\tq\4r\tr\4s\ts\4t\tt\4u\tu\4v\tv\4w\tw\4x\tx\4y\ty\4")
        buf.write("z\tz\4{\t{\4|\t|\4}\t}\4~\t~\4\177\t\177\4\u0080\t\u0080")
        buf.write("\4\u0081\t\u0081\4\u0082\t\u0082\4\u0083\t\u0083\4\u0084")
        buf.write("\t\u0084\4\u0085\t\u0085\4\u0086\t\u0086\4\u0087\t\u0087")
        buf.write("\4\u0088\t\u0088\4\u0089\t\u0089\4\u008a\t\u008a\4\u008b")
        buf.write("\t\u008b\4\u008c\t\u008c\4\u008d\t\u008d\4\u008e\t\u008e")
        buf.write("\4\u008f\t\u008f\4\u0090\t\u0090\4\u0091\t\u0091\4\u0092")
        buf.write("\t\u0092\4\u0093\t\u0093\4\u0094\t\u0094\4\u0095\t\u0095")
        buf.write("\4\u0096\t\u0096\4\u0097\t\u0097\4\u0098\t\u0098\4\u0099")
        buf.write("\t\u0099\4\u009a\t\u009a\4\u009b\t\u009b\4\u009c\t\u009c")
        buf.write("\4\u009d\t\u009d\4\u009e\t\u009e\4\u009f\t\u009f\4\u00a0")
        buf.write("\t\u00a0\4\u00a1\t\u00a1\4\u00a2\t\u00a2\4\u00a3\t\u00a3")
        buf.write("\4\u00a4\t\u00a4\4\u00a5\t\u00a5\4\u00a6\t\u00a6\4\u00a7")
        buf.write("\t\u00a7\4\u00a8\t\u00a8\4\u00a9\t\u00a9\4\u00aa\t\u00aa")
        buf.write("\4\u00ab\t\u00ab\4\u00ac\t\u00ac\4\u00ad\t\u00ad\4\u00ae")
        buf.write("\t\u00ae\4\u00af\t\u00af\4\u00b0\t\u00b0\4\u00b1\t\u00b1")
        buf.write("\4\u00b2\t\u00b2\4\u00b3\t\u00b3\4\u00b4\t\u00b4\4\u00b5")
        buf.write("\t\u00b5\4\u00b6\t\u00b6\4\u00b7\t\u00b7\4\u00b8\t\u00b8")
        buf.write("\4\u00b9\t\u00b9\4\u00ba\t\u00ba\4\u00bb\t\u00bb\4\u00bc")
        buf.write("\t\u00bc\4\u00bd\t\u00bd\4\u00be\t\u00be\4\u00bf\t\u00bf")
        buf.write("\4\u00c0\t\u00c0\4\u00c1\t\u00c1\4\u00c2\t\u00c2\4\u00c3")
        buf.write("\t\u00c3\4\u00c4\t\u00c4\4\u00c5\t\u00c5\4\u00c6\t\u00c6")
        buf.write("\4\u00c7\t\u00c7\4\u00c8\t\u00c8\4\u00c9\t\u00c9\4\u00ca")
        buf.write("\t\u00ca\4\u00cb\t\u00cb\4\u00cc\t\u00cc\4\u00cd\t\u00cd")
        buf.write("\4\u00ce\t\u00ce\4\u00cf\t\u00cf\4\u00d0\t\u00d0\4\u00d1")
        buf.write("\t\u00d1\4\u00d2\t\u00d2\4\u00d3\t\u00d3\4\u00d4\t\u00d4")
        buf.write("\4\u00d5\t\u00d5\4\u00d6\t\u00d6\4\u00d7\t\u00d7\4\u00d8")
        buf.write("\t\u00d8\4\u00d9\t\u00d9\4\u00da\t\u00da\4\u00db\t\u00db")
        buf.write("\4\u00dc\t\u00dc\4\u00dd\t\u00dd\4\u00de\t\u00de\4\u00df")
        buf.write("\t\u00df\4\u00e0\t\u00e0\4\u00e1\t\u00e1\4\u00e2\t\u00e2")
        buf.write("\4\u00e3\t\u00e3\4\u00e4\t\u00e4\4\u00e5\t\u00e5\4\u00e6")
        buf.write("\t\u00e6\4\u00e7\t\u00e7\4\u00e8\t\u00e8\4\u00e9\t\u00e9")
        buf.write("\4\u00ea\t\u00ea\4\u00eb\t\u00eb\4\u00ec\t\u00ec\4\u00ed")
        buf.write("\t\u00ed\4\u00ee\t\u00ee\4\u00ef\t\u00ef\4\u00f0\t\u00f0")
        buf.write("\4\u00f1\t\u00f1\4\u00f2\t\u00f2\4\u00f3\t\u00f3\4\u00f4")
        buf.write("\t\u00f4\4\u00f5\t\u00f5\4\u00f6\t\u00f6\4\u00f7\t\u00f7")
        buf.write("\4\u00f8\t\u00f8\4\u00f9\t\u00f9\4\u00fa\t\u00fa\4\u00fb")
        buf.write("\t\u00fb\4\u00fc\t\u00fc\4\u00fd\t\u00fd\4\u00fe\t\u00fe")
        buf.write("\4\u00ff\t\u00ff\4\u0100\t\u0100\4\u0101\t\u0101\3\2\5")
        buf.write("\2\u0204\n\2\3\2\7\2\u0207\n\2\f\2\16\2\u020a\13\2\3\2")
        buf.write("\5\2\u020d\n\2\3\2\7\2\u0210\n\2\f\2\16\2\u0213\13\2\3")
        buf.write("\2\3\2\5\2\u0217\n\2\3\2\5\2\u021a\n\2\3\2\5\2\u021d\n")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\5\3\u0224\n\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\5\3\5\7\5\u022f\n\5\f\5\16\5\u0232\13\5\3")
        buf.write("\6\6\6\u0235\n\6\r\6\16\6\u0236\3\7\3\7\3\7\5\7\u023c")
        buf.write("\n\7\3\b\3\b\3\b\3\b\3\b\7\b\u0243\n\b\f\b\16\b\u0246")
        buf.write("\13\b\3\b\3\b\5\b\u024a\n\b\3\t\3\t\3\t\3\t\3\t\5\t\u0251")
        buf.write("\n\t\7\t\u0253\n\t\f\t\16\t\u0256\13\t\3\t\3\t\5\t\u025a")
        buf.write("\n\t\3\n\3\n\3\n\3\n\3\n\5\n\u0261\n\n\7\n\u0263\n\n\f")
        buf.write("\n\16\n\u0266\13\n\3\n\3\n\5\n\u026a\n\n\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\f\3\f\5\f\u0273\n\f\3\r\3\r\3\r\6\r\u0278\n")
        buf.write("\r\r\r\16\r\u0279\3\16\3\16\3\16\3\16\7\16\u0280\n\16")
        buf.write("\f\16\16\16\u0283\13\16\5\16\u0285\n\16\3\16\5\16\u0288")
        buf.write("\n\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\7\17\u0295\n\17\f\17\16\17\u0298\13\17\5\17\u029a")
        buf.write("\n\17\3\17\5\17\u029d\n\17\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\7\17\u02a7\n\17\f\17\16\17\u02aa\13\17\5")
        buf.write("\17\u02ac\n\17\3\17\5\17\u02af\n\17\3\17\3\17\5\17\u02b3")
        buf.write("\n\17\3\20\3\20\5\20\u02b7\n\20\3\20\3\20\3\20\5\20\u02bc")
        buf.write("\n\20\3\20\5\20\u02bf\n\20\3\20\6\20\u02c2\n\20\r\20\16")
        buf.write("\20\u02c3\3\21\3\21\3\21\3\21\7\21\u02ca\n\21\f\21\16")
        buf.write("\21\u02cd\13\21\3\21\5\21\u02d0\n\21\5\21\u02d2\n\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\7\21\u02da\n\21\f\21\16\21")
        buf.write("\u02dd\13\21\3\21\5\21\u02e0\n\21\5\21\u02e2\n\21\3\21")
        buf.write("\5\21\u02e5\n\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\7\22\u02f0\n\22\f\22\16\22\u02f3\13\22\5\22\u02f5")
        buf.write("\n\22\3\22\5\22\u02f8\n\22\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\5\22\u0300\n\22\3\22\5\22\u0303\n\22\5\22\u0305\n")
        buf.write("\22\3\23\3\23\5\23\u0309\n\23\3\24\3\24\3\25\3\25\3\25")
        buf.write("\7\25\u0310\n\25\f\25\16\25\u0313\13\25\3\26\3\26\6\26")
        buf.write("\u0317\n\26\r\26\16\26\u0318\3\26\3\26\6\26\u031d\n\26")
        buf.write("\r\26\16\26\u031e\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\5\27\u032a\n\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\5\27\u0332\n\27\3\27\3\27\3\27\3\27\5\27\u0338\n\27\3")
        buf.write("\27\3\27\3\27\3\27\5\27\u033e\n\27\3\27\3\27\3\27\3\27")
        buf.write("\5\27\u0344\n\27\3\30\3\30\3\30\5\30\u0349\n\30\3\30\5")
        buf.write("\30\u034c\n\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\5\31\u0357\n\31\3\31\5\31\u035a\n\31\3\31\5\31\u035d")
        buf.write("\n\31\3\31\3\31\5\31\u0361\n\31\3\31\3\31\3\31\5\31\u0366")
        buf.write("\n\31\3\31\3\31\5\31\u036a\n\31\3\31\3\31\3\31\5\31\u036f")
        buf.write("\n\31\3\31\3\31\5\31\u0373\n\31\3\31\3\31\5\31\u0377\n")
        buf.write("\31\3\31\5\31\u037a\n\31\3\31\5\31\u037d\n\31\3\31\3\31")
        buf.write("\5\31\u0381\n\31\3\31\3\31\5\31\u0385\n\31\3\31\5\31\u0388")
        buf.write("\n\31\3\31\5\31\u038b\n\31\3\31\3\31\3\31\3\31\5\31\u0391")
        buf.write("\n\31\5\31\u0393\n\31\3\32\3\32\3\32\3\32\3\32\3\33\3")
        buf.write("\33\3\33\7\33\u039d\n\33\f\33\16\33\u03a0\13\33\3\34\3")
        buf.write("\34\5\34\u03a4\n\34\3\34\3\34\5\34\u03a8\n\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\5\34\u03b0\n\34\3\34\3\34\5\34\u03b4")
        buf.write("\n\34\3\34\3\34\3\34\5\34\u03b9\n\34\3\34\3\34\5\34\u03bd")
        buf.write("\n\34\3\34\3\34\3\34\5\34\u03c2\n\34\3\34\3\34\5\34\u03c6")
        buf.write("\n\34\3\34\5\34\u03c9\n\34\3\34\5\34\u03cc\n\34\3\34\3")
        buf.write("\34\3\34\5\34\u03d1\n\34\3\34\3\34\5\34\u03d5\n\34\3\34")
        buf.write("\5\34\u03d8\n\34\3\34\5\34\u03db\n\34\5\34\u03dd\n\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\5\35\u03eb\n\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \5 \u03f6\n \3!\3!\3!\3\"\3\"\3\"\3\"\3#\6#\u0400")
        buf.write("\n#\r#\16#\u0401\3$\3$\3$\3%\3%\5%\u0409\n%\3%\3%\3%\3")
        buf.write("%\3%\3%\3%\3%\3%\5%\u0414\n%\3&\3&\6&\u0418\n&\r&\16&")
        buf.write("\u0419\3&\3&\7&\u041e\n&\f&\16&\u0421\13&\3&\7&\u0424")
        buf.write("\n&\f&\16&\u0427\13&\3\'\3\'\5\'\u042b\n\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\5\'\u0436\n\'\3(\3(\5(\u043a")
        buf.write("\n(\3(\3(\5(\u043e\n(\3(\3(\5(\u0442\n(\3(\3(\5(\u0446")
        buf.write("\n(\3(\3(\5(\u044a\n(\3(\5(\u044d\n(\3)\3)\5)\u0451\n")
        buf.write(")\3)\3)\3)\5)\u0456\n)\3)\5)\u0459\n)\3)\3)\3)\5)\u045e")
        buf.write("\n)\3)\3)\5)\u0462\n)\3)\5)\u0465\n)\3)\3)\3)\5)\u046a")
        buf.write("\n)\3)\3)\5)\u046e\n)\3)\5)\u0471\n)\3)\3)\5)\u0475\n")
        buf.write(")\3)\5)\u0478\n)\3)\5)\u047b\n)\3)\3)\5)\u047f\n)\3)\5")
        buf.write(")\u0482\n)\3)\3)\5)\u0486\n)\3)\5)\u0489\n)\3)\5)\u048c")
        buf.write("\n)\5)\u048e\n)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3,\5,\u049a")
        buf.write("\n,\3-\3-\3-\3-\3-\3-\3-\5-\u04a3\n-\3.\3.\3.\3.\3.\5")
        buf.write(".\u04aa\n.\3/\3/\5/\u04ae\n/\3/\3/\3/\3/\3/\3/\3/\5/\u04b7")
        buf.write("\n/\3/\3/\3/\3/\3/\3/\3/\5/\u04c0\n/\3\60\3\60\3\60\3")
        buf.write("\60\3\60\3\60\3\60\3\60\3\60\5\60\u04cb\n\60\3\61\3\61")
        buf.write("\5\61\u04cf\n\61\3\61\3\61\5\61\u04d3\n\61\3\61\3\61\3")
        buf.write("\62\3\62\3\62\3\62\5\62\u04db\n\62\3\63\6\63\u04de\n\63")
        buf.write("\r\63\16\63\u04df\3\64\3\64\5\64\u04e4\n\64\3\65\3\65")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\5\65\u04f0\n")
        buf.write("\65\5\65\u04f2\n\65\3\66\3\66\5\66\u04f6\n\66\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\66\3\66\5\66\u0501\n\66\3")
        buf.write("\67\6\67\u0504\n\67\r\67\16\67\u0505\38\38\38\78\u050b")
        buf.write("\n8\f8\168\u050e\138\39\39\39\59\u0513\n9\39\39\3:\3:")
        buf.write("\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;\5;\u0523\n;\3<\3<\6<\u0527")
        buf.write("\n<\r<\16<\u0528\3<\3<\7<\u052d\n<\f<\16<\u0530\13<\3")
        buf.write("<\7<\u0533\n<\f<\16<\u0536\13<\3=\3=\5=\u053a\n=\3=\3")
        buf.write("=\3>\3>\3>\3?\3?\5?\u0543\n?\3@\3@\6@\u0547\n@\r@\16@")
        buf.write("\u0548\3@\3@\7@\u054d\n@\f@\16@\u0550\13@\3@\7@\u0553")
        buf.write("\n@\f@\16@\u0556\13@\3A\3A\5A\u055a\nA\3A\3A\3B\3B\3B")
        buf.write("\3C\3C\6C\u0563\nC\rC\16C\u0564\3C\3C\7C\u0569\nC\fC\16")
        buf.write("C\u056c\13C\3C\7C\u056f\nC\fC\16C\u0572\13C\3D\3D\5D\u0576")
        buf.write("\nD\3D\3D\3E\3E\3E\5E\u057d\nE\3E\3E\5E\u0581\nE\3F\3")
        buf.write("F\3F\3G\3G\3G\3G\7G\u058a\nG\fG\16G\u058d\13G\3G\5G\u0590")
        buf.write("\nG\3H\3H\5H\u0594\nH\3H\5H\u0597\nH\3H\3H\3H\3H\3I\3")
        buf.write("I\5I\u059f\nI\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\3J\5")
        buf.write("J\u05ae\nJ\3K\3K\5K\u05b2\nK\3K\3K\3K\5K\u05b7\nK\3K\5")
        buf.write("K\u05ba\nK\3L\6L\u05bd\nL\rL\16L\u05be\3M\3M\3M\3M\3M")
        buf.write("\3M\3M\5M\u05c8\nM\3N\3N\3N\3N\7N\u05ce\nN\fN\16N\u05d1")
        buf.write("\13N\3N\5N\u05d4\nN\3O\3O\3O\3P\3P\3P\3P\7P\u05dd\nP\f")
        buf.write("P\16P\u05e0\13P\3P\5P\u05e3\nP\3Q\3Q\3Q\3R\3R\3R\5R\u05eb")
        buf.write("\nR\3R\5R\u05ee\nR\3S\3S\3S\7S\u05f3\nS\fS\16S\u05f6\13")
        buf.write("S\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3T\3")
        buf.write("T\5T\u060a\nT\3U\3U\3U\5U\u060f\nU\3U\3U\3U\3U\3U\3U\5")
        buf.write("U\u0617\nU\3V\3V\3W\3W\3X\5X\u061e\nX\3X\3X\3X\3X\3Y\3")
        buf.write("Y\3Y\3Z\3Z\3Z\3[\3[\3\\\3\\\3]\3]\3]\7]\u0631\n]\f]\16")
        buf.write("]\u0634\13]\3^\3^\3^\7^\u0639\n^\f^\16^\u063c\13^\3_\3")
        buf.write("_\3_\3_\3_\3_\5_\u0644\n_\3`\3`\3a\3a\3a\3a\3a\5a\u064d")
        buf.write("\na\3b\3b\3b\3b\3b\5b\u0654\nb\3c\3c\5c\u0658\nc\3c\3")
        buf.write("c\3c\3c\3c\3c\3c\3c\3c\3c\3c\3c\5c\u0666\nc\3d\3d\5d\u066a")
        buf.write("\nd\3d\3d\3d\3d\3d\3d\3d\3d\3d\3d\3d\3d\5d\u0678\nd\3")
        buf.write("e\3e\3f\3f\3g\3g\3g\3g\3g\5g\u0683\ng\3h\3h\3h\3h\3h\5")
        buf.write("h\u068a\nh\3i\3i\3j\6j\u068f\nj\rj\16j\u0690\3k\3k\3l")
        buf.write("\3l\3m\6m\u0698\nm\rm\16m\u0699\3n\3n\3n\3n\3n\3n\3n\3")
        buf.write("n\3n\3n\5n\u06a6\nn\3o\3o\3o\3o\3o\3o\3o\3o\3o\5o\u06b1")
        buf.write("\no\3o\3o\3o\3o\3o\3o\3o\3o\3o\3o\3o\3o\3o\3o\3o\3o\3")
        buf.write("o\3o\3o\3o\3o\3o\3o\3o\3o\3o\3o\3o\3o\3o\3o\3o\3o\3o\3")
        buf.write("o\3o\3o\3o\3o\3o\3o\5o\u06dc\no\3o\3o\3o\3o\3o\3o\3o\3")
        buf.write("o\3o\3o\3o\3o\5o\u06ea\no\3p\3p\3q\3q\3q\7q\u06f1\nq\f")
        buf.write("q\16q\u06f4\13q\3r\3r\3r\7r\u06f9\nr\fr\16r\u06fc\13r")
        buf.write("\3s\3s\3s\3s\3s\7s\u0703\ns\fs\16s\u0706\13s\3t\6t\u0709")
        buf.write("\nt\rt\16t\u070a\3u\3u\3u\3u\3u\3u\3u\3u\3u\3u\3u\5u\u0718")
        buf.write("\nu\3v\3v\3v\3v\3v\3v\3v\5v\u0721\nv\3w\3w\3w\3x\3x\3")
        buf.write("x\7x\u0729\nx\fx\16x\u072c\13x\3y\5y\u072f\ny\3y\3y\5")
        buf.write("y\u0733\ny\3z\6z\u0736\nz\rz\16z\u0737\3{\3{\3|\3|\3|")
        buf.write("\5|\u073f\n|\3|\7|\u0742\n|\f|\16|\u0745\13|\3|\3|\3}")
        buf.write("\3}\3}\3}\7}\u074d\n}\f}\16}\u0750\13}\3~\3~\3\177\3\177")
        buf.write("\3\177\3\177\3\u0080\3\u0080\3\u0080\3\u0081\3\u0081\3")
        buf.write("\u0081\7\u0081\u075e\n\u0081\f\u0081\16\u0081\u0761\13")
        buf.write("\u0081\3\u0082\5\u0082\u0764\n\u0082\3\u0082\3\u0082\3")
        buf.write("\u0082\5\u0082\u0769\n\u0082\3\u0082\3\u0082\3\u0083\3")
        buf.write("\u0083\5\u0083\u076f\n\u0083\3\u0083\3\u0083\3\u0084\3")
        buf.write("\u0084\3\u0085\3\u0085\3\u0085\7\u0085\u0778\n\u0085\f")
        buf.write("\u0085\16\u0085\u077b\13\u0085\3\u0086\3\u0086\3\u0086")
        buf.write("\3\u0086\3\u0087\6\u0087\u0782\n\u0087\r\u0087\16\u0087")
        buf.write("\u0783\3\u0088\3\u0088\3\u0088\3\u0088\3\u0088\3\u0088")
        buf.write("\3\u0088\3\u0088\3\u0088\3\u0088\5\u0088\u0790\n\u0088")
        buf.write("\3\u0089\3\u0089\3\u0089\3\u0089\3\u0089\3\u0089\3\u0089")
        buf.write("\5\u0089\u0799\n\u0089\3\u008a\3\u008a\3\u008a\5\u008a")
        buf.write("\u079e\n\u008a\3\u008a\3\u008a\3\u008a\3\u008a\6\u008a")
        buf.write("\u07a4\n\u008a\r\u008a\16\u008a\u07a5\5\u008a\u07a8\n")
        buf.write("\u008a\3\u008b\3\u008b\3\u008b\6\u008b\u07ad\n\u008b\r")
        buf.write("\u008b\16\u008b\u07ae\5\u008b\u07b1\n\u008b\3\u008c\3")
        buf.write("\u008c\3\u008c\5\u008c\u07b6\n\u008c\3\u008c\3\u008c\5")
        buf.write("\u008c\u07ba\n\u008c\5\u008c\u07bc\n\u008c\3\u008d\6\u008d")
        buf.write("\u07bf\n\u008d\r\u008d\16\u008d\u07c0\3\u008e\3\u008e")
        buf.write("\3\u008e\3\u008e\3\u008e\3\u008f\3\u008f\3\u008f\3\u008f")
        buf.write("\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f")
        buf.write("\3\u008f\5\u008f\u07d4\n\u008f\3\u008f\3\u008f\3\u008f")
        buf.write("\3\u008f\3\u008f\3\u008f\3\u008f\5\u008f\u07dd\n\u008f")
        buf.write("\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f\5\u008f\u07e4")
        buf.write("\n\u008f\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f")
        buf.write("\3\u008f\5\u008f\u07ed\n\u008f\3\u008f\3\u008f\3\u008f")
        buf.write("\3\u008f\3\u008f\5\u008f\u07f4\n\u008f\3\u008f\3\u008f")
        buf.write("\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f\5\u008f")
        buf.write("\u07fe\n\u008f\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f")
        buf.write("\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f\3\u008f")
        buf.write("\3\u008f\3\u008f\3\u008f\5\u008f\u080f\n\u008f\3\u008f")
        buf.write("\3\u008f\6\u008f\u0813\n\u008f\r\u008f\16\u008f\u0814")
        buf.write("\5\u008f\u0817\n\u008f\3\u0090\3\u0090\3\u0090\3\u0090")
        buf.write("\3\u0090\3\u0090\3\u0090\3\u0090\3\u0090\5\u0090\u0822")
        buf.write("\n\u0090\3\u0091\3\u0091\3\u0091\3\u0091\3\u0092\3\u0092")
        buf.write("\3\u0092\3\u0092\3\u0093\3\u0093\5\u0093\u082e\n\u0093")
        buf.write("\3\u0094\3\u0094\3\u0094\3\u0094\3\u0094\3\u0094\3\u0094")
        buf.write("\3\u0094\3\u0094\3\u0094\3\u0094\3\u0094\3\u0094\3\u0094")
        buf.write("\3\u0094\3\u0094\3\u0094\3\u0094\3\u0094\3\u0094\3\u0094")
        buf.write("\5\u0094\u0845\n\u0094\3\u0095\3\u0095\3\u0095\3\u0095")
        buf.write("\7\u0095\u084b\n\u0095\f\u0095\16\u0095\u084e\13\u0095")
        buf.write("\3\u0096\3\u0096\3\u0097\5\u0097\u0853\n\u0097\3\u0097")
        buf.write("\3\u0097\3\u0098\6\u0098\u0858\n\u0098\r\u0098\16\u0098")
        buf.write("\u0859\3\u0098\3\u0098\5\u0098\u085e\n\u0098\3\u0099\3")
        buf.write("\u0099\3\u0099\3\u0099\3\u0099\3\u0099\3\u0099\3\u0099")
        buf.write("\3\u0099\3\u0099\3\u0099\3\u0099\3\u0099\3\u0099\3\u0099")
        buf.write("\3\u0099\3\u0099\3\u0099\3\u0099\3\u0099\3\u0099\3\u0099")
        buf.write("\3\u0099\5\u0099\u0877\n\u0099\3\u0099\3\u0099\3\u0099")
        buf.write("\5\u0099\u087c\n\u0099\3\u0099\3\u0099\3\u0099\3\u0099")
        buf.write("\3\u0099\3\u0099\3\u0099\3\u0099\3\u0099\3\u0099\3\u0099")
        buf.write("\3\u0099\3\u0099\3\u0099\3\u0099\5\u0099\u088d\n\u0099")
        buf.write("\3\u009a\3\u009a\3\u009a\5\u009a\u0892\n\u009a\3\u009a")
        buf.write("\7\u009a\u0895\n\u009a\f\u009a\16\u009a\u0898\13\u009a")
        buf.write("\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b")
        buf.write("\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b")
        buf.write("\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b")
        buf.write("\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b")
        buf.write("\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b")
        buf.write("\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b")
        buf.write("\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b")
        buf.write("\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b")
        buf.write("\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b\3\u009b")
        buf.write("\5\u009b\u08d9\n\u009b\3\u009b\3\u009b\5\u009b\u08dd\n")
        buf.write("\u009b\3\u009c\3\u009c\5\u009c\u08e1\n\u009c\3\u009d\3")
        buf.write("\u009d\3\u009d\3\u009e\3\u009e\3\u009e\3\u009f\6\u009f")
        buf.write("\u08ea\n\u009f\r\u009f\16\u009f\u08eb\3\u00a0\3\u00a0")
        buf.write("\3\u00a1\3\u00a1\5\u00a1\u08f2\n\u00a1\3\u00a1\3\u00a1")
        buf.write("\3\u00a2\3\u00a2\7\u00a2\u08f8\n\u00a2\f\u00a2\16\u00a2")
        buf.write("\u08fb\13\u00a2\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a3")
        buf.write("\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a3\3\u00a3\5\u00a3")
        buf.write("\u0908\n\u00a3\3\u00a4\3\u00a4\3\u00a4\3\u00a4\3\u00a4")
        buf.write("\3\u00a4\3\u00a4\3\u00a4\5\u00a4\u0912\n\u00a4\3\u00a4")
        buf.write("\3\u00a4\3\u00a4\5\u00a4\u0917\n\u00a4\5\u00a4\u0919\n")
        buf.write("\u00a4\3\u00a5\3\u00a5\5\u00a5\u091d\n\u00a5\3\u00a6\3")
        buf.write("\u00a6\3\u00a6\3\u00a6\5\u00a6\u0923\n\u00a6\3\u00a7\3")
        buf.write("\u00a7\3\u00a7\3\u00a7\3\u00a7\3\u00a7\3\u00a7\3\u00a7")
        buf.write("\3\u00a7\3\u00a7\3\u00a7\3\u00a7\3\u00a7\3\u00a7\3\u00a7")
        buf.write("\3\u00a7\3\u00a7\3\u00a7\3\u00a7\3\u00a7\3\u00a7\3\u00a7")
        buf.write("\3\u00a7\3\u00a7\5\u00a7\u093d\n\u00a7\3\u00a8\3\u00a8")
        buf.write("\3\u00a8\3\u00a8\3\u00a8\7\u00a8\u0944\n\u00a8\f\u00a8")
        buf.write("\16\u00a8\u0947\13\u00a8\3\u00a9\3\u00a9\3\u00aa\3\u00aa")
        buf.write("\3\u00aa\7\u00aa\u094e\n\u00aa\f\u00aa\16\u00aa\u0951")
        buf.write("\13\u00aa\3\u00ab\3\u00ab\3\u00ab\7\u00ab\u0956\n\u00ab")
        buf.write("\f\u00ab\16\u00ab\u0959\13\u00ab\3\u00ab\3\u00ab\3\u00ab")
        buf.write("\7\u00ab\u095e\n\u00ab\f\u00ab\16\u00ab\u0961\13\u00ab")
        buf.write("\3\u00ab\3\u00ab\3\u00ab\7\u00ab\u0966\n\u00ab\f\u00ab")
        buf.write("\16\u00ab\u0969\13\u00ab\3\u00ab\3\u00ab\3\u00ab\7\u00ab")
        buf.write("\u096e\n\u00ab\f\u00ab\16\u00ab\u0971\13\u00ab\5\u00ab")
        buf.write("\u0973\n\u00ab\3\u00ac\3\u00ac\3\u00ac\3\u00ac\3\u00ac")
        buf.write("\3\u00ac\3\u00ac\3\u00ac\3\u00ac\3\u00ac\3\u00ac\3\u00ac")
        buf.write("\3\u00ac\3\u00ac\3\u00ac\3\u00ac\3\u00ac\3\u00ac\5\u00ac")
        buf.write("\u0987\n\u00ac\3\u00ad\3\u00ad\3\u00ad\7\u00ad\u098c\n")
        buf.write("\u00ad\f\u00ad\16\u00ad\u098f\13\u00ad\3\u00ae\3\u00ae")
        buf.write("\3\u00ae\3\u00ae\3\u00ae\3\u00ae\3\u00ae\5\u00ae\u0998")
        buf.write("\n\u00ae\3\u00af\3\u00af\3\u00af\7\u00af\u099d\n\u00af")
        buf.write("\f\u00af\16\u00af\u09a0\13\u00af\6\u00af\u09a2\n\u00af")
        buf.write("\r\u00af\16\u00af\u09a3\3\u00af\3\u00af\3\u00af\3\u00af")
        buf.write("\3\u00af\5\u00af\u09ab\n\u00af\3\u00b0\3\u00b0\3\u00b0")
        buf.write("\3\u00b1\3\u00b1\5\u00b1\u09b2\n\u00b1\3\u00b2\3\u00b2")
        buf.write("\3\u00b2\5\u00b2\u09b7\n\u00b2\3\u00b3\6\u00b3\u09ba\n")
        buf.write("\u00b3\r\u00b3\16\u00b3\u09bb\3\u00b4\3\u00b4\3\u00b4")
        buf.write("\3\u00b4\3\u00b4\5\u00b4\u09c3\n\u00b4\3\u00b5\3\u00b5")
        buf.write("\3\u00b5\3\u00b5\3\u00b5\3\u00b6\3\u00b6\3\u00b7\3\u00b7")
        buf.write("\3\u00b8\3\u00b8\3\u00b9\6\u00b9\u09d1\n\u00b9\r\u00b9")
        buf.write("\16\u00b9\u09d2\3\u00ba\3\u00ba\3\u00ba\3\u00ba\3\u00bb")
        buf.write("\3\u00bb\5\u00bb\u09db\n\u00bb\3\u00bb\3\u00bb\3\u00bc")
        buf.write("\3\u00bc\6\u00bc\u09e1\n\u00bc\r\u00bc\16\u00bc\u09e2")
        buf.write("\3\u00bc\3\u00bc\7\u00bc\u09e7\n\u00bc\f\u00bc\16\u00bc")
        buf.write("\u09ea\13\u00bc\3\u00bc\7\u00bc\u09ed\n\u00bc\f\u00bc")
        buf.write("\16\u00bc\u09f0\13\u00bc\3\u00bd\3\u00bd\3\u00bd\3\u00bd")
        buf.write("\6\u00bd\u09f6\n\u00bd\r\u00bd\16\u00bd\u09f7\5\u00bd")
        buf.write("\u09fa\n\u00bd\3\u00be\3\u00be\3\u00be\3\u00be\3\u00be")
        buf.write("\3\u00be\3\u00be\5\u00be\u0a03\n\u00be\3\u00bf\3\u00bf")
        buf.write("\3\u00bf\7\u00bf\u0a08\n\u00bf\f\u00bf\16\u00bf\u0a0b")
        buf.write("\13\u00bf\3\u00bf\5\u00bf\u0a0e\n\u00bf\3\u00c0\3\u00c0")
        buf.write("\3\u00c0\3\u00c0\3\u00c0\5\u00c0\u0a15\n\u00c0\3\u00c1")
        buf.write("\3\u00c1\6\u00c1\u0a19\n\u00c1\r\u00c1\16\u00c1\u0a1a")
        buf.write("\3\u00c1\3\u00c1\3\u00c1\7\u00c1\u0a20\n\u00c1\f\u00c1")
        buf.write("\16\u00c1\u0a23\13\u00c1\3\u00c2\3\u00c2\3\u00c2\3\u00c2")
        buf.write("\3\u00c3\3\u00c3\3\u00c3\7\u00c3\u0a2c\n\u00c3\f\u00c3")
        buf.write("\16\u00c3\u0a2f\13\u00c3\3\u00c4\3\u00c4\3\u00c5\3\u00c5")
        buf.write("\3\u00c5\7\u00c5\u0a36\n\u00c5\f\u00c5\16\u00c5\u0a39")
        buf.write("\13\u00c5\3\u00c6\3\u00c6\3\u00c6\3\u00c6\3\u00c6\5\u00c6")
        buf.write("\u0a40\n\u00c6\3\u00c7\3\u00c7\3\u00c7\7\u00c7\u0a45\n")
        buf.write("\u00c7\f\u00c7\16\u00c7\u0a48\13\u00c7\3\u00c8\3\u00c8")
        buf.write("\5\u00c8\u0a4c\n\u00c8\3\u00c9\3\u00c9\5\u00c9\u0a50\n")
        buf.write("\u00c9\3\u00ca\3\u00ca\5\u00ca\u0a54\n\u00ca\3\u00cb\3")
        buf.write("\u00cb\3\u00cb\3\u00cb\3\u00cb\5\u00cb\u0a5b\n\u00cb\3")
        buf.write("\u00cc\3\u00cc\3\u00cc\3\u00cc\3\u00cc\3\u00cc\5\u00cc")
        buf.write("\u0a63\n\u00cc\3\u00cd\3\u00cd\3\u00cd\7\u00cd\u0a68\n")
        buf.write("\u00cd\f\u00cd\16\u00cd\u0a6b\13\u00cd\3\u00ce\3\u00ce")
        buf.write("\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce\3\u00ce")
        buf.write("\3\u00ce\3\u00ce\3\u00ce\5\u00ce\u0a79\n\u00ce\3\u00cf")
        buf.write("\3\u00cf\3\u00cf\5\u00cf\u0a7e\n\u00cf\3\u00d0\3\u00d0")
        buf.write("\3\u00d0\3\u00d0\3\u00d0\5\u00d0\u0a85\n\u00d0\3\u00d1")
        buf.write("\3\u00d1\3\u00d1\3\u00d1\3\u00d1\5\u00d1\u0a8c\n\u00d1")
        buf.write("\3\u00d2\3\u00d2\5\u00d2\u0a90\n\u00d2\3\u00d3\3\u00d3")
        buf.write("\3\u00d3\3\u00d3\3\u00d3\5\u00d3\u0a97\n\u00d3\3\u00d4")
        buf.write("\3\u00d4\3\u00d4\3\u00d4\3\u00d4\3\u00d4\3\u00d4\3\u00d4")
        buf.write("\3\u00d4\3\u00d4\3\u00d4\3\u00d4\3\u00d4\3\u00d4\5\u00d4")
        buf.write("\u0aa7\n\u00d4\3\u00d5\3\u00d5\3\u00d5\3\u00d5\3\u00d5")
        buf.write("\5\u00d5\u0aae\n\u00d5\3\u00d6\3\u00d6\3\u00d6\3\u00d6")
        buf.write("\3\u00d6\5\u00d6\u0ab5\n\u00d6\3\u00d7\3\u00d7\3\u00d7")
        buf.write("\5\u00d7\u0aba\n\u00d7\3\u00d7\3\u00d7\3\u00d8\3\u00d8")
        buf.write("\3\u00d9\3\u00d9\3\u00d9\5\u00d9\u0ac3\n\u00d9\3\u00da")
        buf.write("\3\u00da\3\u00da\3\u00da\3\u00da\5\u00da\u0aca\n\u00da")
        buf.write("\3\u00db\3\u00db\5\u00db\u0ace\n\u00db\3\u00dc\3\u00dc")
        buf.write("\3\u00dc\3\u00dc\3\u00dc\5\u00dc\u0ad5\n\u00dc\3\u00dd")
        buf.write("\3\u00dd\5\u00dd\u0ad9\n\u00dd\3\u00de\3\u00de\3\u00de")
        buf.write("\5\u00de\u0ade\n\u00de\3\u00df\3\u00df\3\u00df\3\u00df")
        buf.write("\3\u00e0\3\u00e0\3\u00e0\3\u00e0\3\u00e0\5\u00e0\u0ae9")
        buf.write("\n\u00e0\3\u00e1\3\u00e1\3\u00e1\3\u00e1\3\u00e1\5\u00e1")
        buf.write("\u0af0\n\u00e1\3\u00e2\3\u00e2\3\u00e3\3\u00e3\3\u00e3")
        buf.write("\3\u00e3\3\u00e4\3\u00e4\3\u00e4\3\u00e4\3\u00e4\5\u00e4")
        buf.write("\u0afd\n\u00e4\3\u00e5\3\u00e5\3\u00e6\3\u00e6\3\u00e6")
        buf.write("\5\u00e6\u0b04\n\u00e6\3\u00e6\3\u00e6\3\u00e7\3\u00e7")
        buf.write("\3\u00e7\3\u00e7\3\u00e7\5\u00e7\u0b0d\n\u00e7\3\u00e8")
        buf.write("\3\u00e8\3\u00e8\3\u00e8\3\u00e8\5\u00e8\u0b14\n\u00e8")
        buf.write("\3\u00e9\3\u00e9\3\u00e9\5\u00e9\u0b19\n\u00e9\3\u00e9")
        buf.write("\3\u00e9\3\u00ea\3\u00ea\5\u00ea\u0b1f\n\u00ea\3\u00ea")
        buf.write("\7\u00ea\u0b22\n\u00ea\f\u00ea\16\u00ea\u0b25\13\u00ea")
        buf.write("\3\u00eb\3\u00eb\3\u00eb\5\u00eb\u0b2a\n\u00eb\3\u00eb")
        buf.write("\3\u00eb\3\u00ec\3\u00ec\5\u00ec\u0b30\n\u00ec\3\u00ed")
        buf.write("\3\u00ed\5\u00ed\u0b34\n\u00ed\3\u00ee\6\u00ee\u0b37\n")
        buf.write("\u00ee\r\u00ee\16\u00ee\u0b38\3\u00ef\3\u00ef\3\u00f0")
        buf.write("\3\u00f0\3\u00f0\5\u00f0\u0b40\n\u00f0\3\u00f0\3\u00f0")
        buf.write("\3\u00f1\3\u00f1\7\u00f1\u0b46\n\u00f1\f\u00f1\16\u00f1")
        buf.write("\u0b49\13\u00f1\3\u00f2\3\u00f2\3\u00f2\5\u00f2\u0b4e")
        buf.write("\n\u00f2\3\u00f2\3\u00f2\3\u00f3\3\u00f3\7\u00f3\u0b54")
        buf.write("\n\u00f3\f\u00f3\16\u00f3\u0b57\13\u00f3\3\u00f4\3\u00f4")
        buf.write("\3\u00f4\3\u00f4\5\u00f4\u0b5d\n\u00f4\3\u00f5\3\u00f5")
        buf.write("\3\u00f6\3\u00f6\3\u00f7\3\u00f7\3\u00f8\3\u00f8\3\u00f8")
        buf.write("\7\u00f8\u0b68\n\u00f8\f\u00f8\16\u00f8\u0b6b\13\u00f8")
        buf.write("\3\u00f8\3\u00f8\3\u00f9\6\u00f9\u0b70\n\u00f9\r\u00f9")
        buf.write("\16\u00f9\u0b71\3\u00fa\6\u00fa\u0b75\n\u00fa\r\u00fa")
        buf.write("\16\u00fa\u0b76\3\u00fb\3\u00fb\3\u00fc\3\u00fc\3\u00fd")
        buf.write("\3\u00fd\3\u00fe\3\u00fe\3\u00ff\3\u00ff\3\u0100\3\u0100")
        buf.write("\3\u0101\3\u0101\3\u0101\2\2\u0102\2\4\6\b\n\f\16\20\22")
        buf.write("\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR")
        buf.write("TVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088")
        buf.write("\u008a\u008c\u008e\u0090\u0092\u0094\u0096\u0098\u009a")
        buf.write("\u009c\u009e\u00a0\u00a2\u00a4\u00a6\u00a8\u00aa\u00ac")
        buf.write("\u00ae\u00b0\u00b2\u00b4\u00b6\u00b8\u00ba\u00bc\u00be")
        buf.write("\u00c0\u00c2\u00c4\u00c6\u00c8\u00ca\u00cc\u00ce\u00d0")
        buf.write("\u00d2\u00d4\u00d6\u00d8\u00da\u00dc\u00de\u00e0\u00e2")
        buf.write("\u00e4\u00e6\u00e8\u00ea\u00ec\u00ee\u00f0\u00f2\u00f4")
        buf.write("\u00f6\u00f8\u00fa\u00fc\u00fe\u0100\u0102\u0104\u0106")
        buf.write("\u0108\u010a\u010c\u010e\u0110\u0112\u0114\u0116\u0118")
        buf.write("\u011a\u011c\u011e\u0120\u0122\u0124\u0126\u0128\u012a")
        buf.write("\u012c\u012e\u0130\u0132\u0134\u0136\u0138\u013a\u013c")
        buf.write("\u013e\u0140\u0142\u0144\u0146\u0148\u014a\u014c\u014e")
        buf.write("\u0150\u0152\u0154\u0156\u0158\u015a\u015c\u015e\u0160")
        buf.write("\u0162\u0164\u0166\u0168\u016a\u016c\u016e\u0170\u0172")
        buf.write("\u0174\u0176\u0178\u017a\u017c\u017e\u0180\u0182\u0184")
        buf.write("\u0186\u0188\u018a\u018c\u018e\u0190\u0192\u0194\u0196")
        buf.write("\u0198\u019a\u019c\u019e\u01a0\u01a2\u01a4\u01a6\u01a8")
        buf.write("\u01aa\u01ac\u01ae\u01b0\u01b2\u01b4\u01b6\u01b8\u01ba")
        buf.write("\u01bc\u01be\u01c0\u01c2\u01c4\u01c6\u01c8\u01ca\u01cc")
        buf.write("\u01ce\u01d0\u01d2\u01d4\u01d6\u01d8\u01da\u01dc\u01de")
        buf.write("\u01e0\u01e2\u01e4\u01e6\u01e8\u01ea\u01ec\u01ee\u01f0")
        buf.write("\u01f2\u01f4\u01f6\u01f8\u01fa\u01fc\u01fe\u0200\2\16")
        buf.write("\3\2\22\24\4\2\30\30\62\63\4\2()+,\3\2\"$\4\2NNee\t\2")
        buf.write("\6\6\16\16\32\32!!(*,,\62\64\4\2\u0086\u0086\u0088\u0088")
        buf.write("\4\2\u0087\u0087\u0089\u0089\4\2ff\u008a\u008a\7\2ffh")
        buf.write("hnnz}\u0086\u0087\t\2T[]acceeggijmm\3\2\u008b\u008d\2")
        buf.write("\u0c82\2\u0203\3\2\2\2\4\u0220\3\2\2\2\6\u0227\3\2\2\2")
        buf.write("\b\u022a\3\2\2\2\n\u0234\3\2\2\2\f\u023b\3\2\2\2\16\u023d")
        buf.write("\3\2\2\2\20\u024b\3\2\2\2\22\u025b\3\2\2\2\24\u026b\3")
        buf.write("\2\2\2\26\u0272\3\2\2\2\30\u0277\3\2\2\2\32\u027b\3\2")
        buf.write("\2\2\34\u02b2\3\2\2\2\36\u02b4\3\2\2\2 \u02e4\3\2\2\2")
        buf.write("\"\u0304\3\2\2\2$\u0308\3\2\2\2&\u030a\3\2\2\2(\u030c")
        buf.write("\3\2\2\2*\u031c\3\2\2\2,\u0343\3\2\2\2.\u0345\3\2\2\2")
        buf.write("\60\u0392\3\2\2\2\62\u0394\3\2\2\2\64\u0399\3\2\2\2\66")
        buf.write("\u03dc\3\2\2\28\u03ea\3\2\2\2:\u03ec\3\2\2\2<\u03ee\3")
        buf.write("\2\2\2>\u03f5\3\2\2\2@\u03f7\3\2\2\2B\u03fa\3\2\2\2D\u03ff")
        buf.write("\3\2\2\2F\u0403\3\2\2\2H\u0413\3\2\2\2J\u0415\3\2\2\2")
        buf.write("L\u0435\3\2\2\2N\u044c\3\2\2\2P\u048d\3\2\2\2R\u048f\3")
        buf.write("\2\2\2T\u0492\3\2\2\2V\u0499\3\2\2\2X\u04a2\3\2\2\2Z\u04a9")
        buf.write("\3\2\2\2\\\u04bf\3\2\2\2^\u04ca\3\2\2\2`\u04cc\3\2\2\2")
        buf.write("b\u04d6\3\2\2\2d\u04dd\3\2\2\2f\u04e3\3\2\2\2h\u04f1\3")
        buf.write("\2\2\2j\u0500\3\2\2\2l\u0503\3\2\2\2n\u0507\3\2\2\2p\u050f")
        buf.write("\3\2\2\2r\u0516\3\2\2\2t\u0522\3\2\2\2v\u0524\3\2\2\2")
        buf.write("x\u0537\3\2\2\2z\u053d\3\2\2\2|\u0542\3\2\2\2~\u0544\3")
        buf.write("\2\2\2\u0080\u0557\3\2\2\2\u0082\u055d\3\2\2\2\u0084\u0560")
        buf.write("\3\2\2\2\u0086\u0573\3\2\2\2\u0088\u0580\3\2\2\2\u008a")
        buf.write("\u0582\3\2\2\2\u008c\u0585\3\2\2\2\u008e\u0591\3\2\2\2")
        buf.write("\u0090\u059e\3\2\2\2\u0092\u05ad\3\2\2\2\u0094\u05af\3")
        buf.write("\2\2\2\u0096\u05bc\3\2\2\2\u0098\u05c7\3\2\2\2\u009a\u05c9")
        buf.write("\3\2\2\2\u009c\u05d5\3\2\2\2\u009e\u05d8\3\2\2\2\u00a0")
        buf.write("\u05e4\3\2\2\2\u00a2\u05ed\3\2\2\2\u00a4\u05ef\3\2\2\2")
        buf.write("\u00a6\u0609\3\2\2\2\u00a8\u0616\3\2\2\2\u00aa\u0618\3")
        buf.write("\2\2\2\u00ac\u061a\3\2\2\2\u00ae\u061d\3\2\2\2\u00b0\u0623")
        buf.write("\3\2\2\2\u00b2\u0626\3\2\2\2\u00b4\u0629\3\2\2\2\u00b6")
        buf.write("\u062b\3\2\2\2\u00b8\u062d\3\2\2\2\u00ba\u0635\3\2\2\2")
        buf.write("\u00bc\u0643\3\2\2\2\u00be\u0645\3\2\2\2\u00c0\u064c\3")
        buf.write("\2\2\2\u00c2\u0653\3\2\2\2\u00c4\u0665\3\2\2\2\u00c6\u0677")
        buf.write("\3\2\2\2\u00c8\u0679\3\2\2\2\u00ca\u067b\3\2\2\2\u00cc")
        buf.write("\u0682\3\2\2\2\u00ce\u0689\3\2\2\2\u00d0\u068b\3\2\2\2")
        buf.write("\u00d2\u068e\3\2\2\2\u00d4\u0692\3\2\2\2\u00d6\u0694\3")
        buf.write("\2\2\2\u00d8\u0697\3\2\2\2\u00da\u06a5\3\2\2\2\u00dc\u06e9")
        buf.write("\3\2\2\2\u00de\u06eb\3\2\2\2\u00e0\u06ed\3\2\2\2\u00e2")
        buf.write("\u06f5\3\2\2\2\u00e4\u06fd\3\2\2\2\u00e6\u0708\3\2\2\2")
        buf.write("\u00e8\u0717\3\2\2\2\u00ea\u0720\3\2\2\2\u00ec\u0722\3")
        buf.write("\2\2\2\u00ee\u0725\3\2\2\2\u00f0\u072e\3\2\2\2\u00f2\u0735")
        buf.write("\3\2\2\2\u00f4\u0739\3\2\2\2\u00f6\u073b\3\2\2\2\u00f8")
        buf.write("\u0748\3\2\2\2\u00fa\u0751\3\2\2\2\u00fc\u0753\3\2\2\2")
        buf.write("\u00fe\u0757\3\2\2\2\u0100\u075a\3\2\2\2\u0102\u0763\3")
        buf.write("\2\2\2\u0104\u076c\3\2\2\2\u0106\u0772\3\2\2\2\u0108\u0774")
        buf.write("\3\2\2\2\u010a\u077c\3\2\2\2\u010c\u0781\3\2\2\2\u010e")
        buf.write("\u078f\3\2\2\2\u0110\u0798\3\2\2\2\u0112\u07a7\3\2\2\2")
        buf.write("\u0114\u07b0\3\2\2\2\u0116\u07bb\3\2\2\2\u0118\u07be\3")
        buf.write("\2\2\2\u011a\u07c2\3\2\2\2\u011c\u0816\3\2\2\2\u011e\u0821")
        buf.write("\3\2\2\2\u0120\u0823\3\2\2\2\u0122\u0827\3\2\2\2\u0124")
        buf.write("\u082d\3\2\2\2\u0126\u0844\3\2\2\2\u0128\u0846\3\2\2\2")
        buf.write("\u012a\u084f\3\2\2\2\u012c\u0852\3\2\2\2\u012e\u0857\3")
        buf.write("\2\2\2\u0130\u088c\3\2\2\2\u0132\u088e\3\2\2\2\u0134\u08dc")
        buf.write("\3\2\2\2\u0136\u08e0\3\2\2\2\u0138\u08e2\3\2\2\2\u013a")
        buf.write("\u08e5\3\2\2\2\u013c\u08e9\3\2\2\2\u013e\u08ed\3\2\2\2")
        buf.write("\u0140\u08ef\3\2\2\2\u0142\u08f5\3\2\2\2\u0144\u0907\3")
        buf.write("\2\2\2\u0146\u0918\3\2\2\2\u0148\u091a\3\2\2\2\u014a\u0922")
        buf.write("\3\2\2\2\u014c\u093c\3\2\2\2\u014e\u093e\3\2\2\2\u0150")
        buf.write("\u0948\3\2\2\2\u0152\u094a\3\2\2\2\u0154\u0972\3\2\2\2")
        buf.write("\u0156\u0986\3\2\2\2\u0158\u0988\3\2\2\2\u015a\u0997\3")
        buf.write("\2\2\2\u015c\u09aa\3\2\2\2\u015e\u09ac\3\2\2\2\u0160\u09af")
        buf.write("\3\2\2\2\u0162\u09b6\3\2\2\2\u0164\u09b9\3\2\2\2\u0166")
        buf.write("\u09c2\3\2\2\2\u0168\u09c4\3\2\2\2\u016a\u09c9\3\2\2\2")
        buf.write("\u016c\u09cb\3\2\2\2\u016e\u09cd\3\2\2\2\u0170\u09d0\3")
        buf.write("\2\2\2\u0172\u09d4\3\2\2\2\u0174\u09d8\3\2\2\2\u0176\u09de")
        buf.write("\3\2\2\2\u0178\u09f9\3\2\2\2\u017a\u0a02\3\2\2\2\u017c")
        buf.write("\u0a0d\3\2\2\2\u017e\u0a14\3\2\2\2\u0180\u0a16\3\2\2\2")
        buf.write("\u0182\u0a24\3\2\2\2\u0184\u0a28\3\2\2\2\u0186\u0a30\3")
        buf.write("\2\2\2\u0188\u0a32\3\2\2\2\u018a\u0a3f\3\2\2\2\u018c\u0a41")
        buf.write("\3\2\2\2\u018e\u0a4b\3\2\2\2\u0190\u0a4f\3\2\2\2\u0192")
        buf.write("\u0a53\3\2\2\2\u0194\u0a5a\3\2\2\2\u0196\u0a62\3\2\2\2")
        buf.write("\u0198\u0a64\3\2\2\2\u019a\u0a78\3\2\2\2\u019c\u0a7d\3")
        buf.write("\2\2\2\u019e\u0a84\3\2\2\2\u01a0\u0a8b\3\2\2\2\u01a2\u0a8f")
        buf.write("\3\2\2\2\u01a4\u0a96\3\2\2\2\u01a6\u0aa6\3\2\2\2\u01a8")
        buf.write("\u0aad\3\2\2\2\u01aa\u0ab4\3\2\2\2\u01ac\u0ab9\3\2\2\2")
        buf.write("\u01ae\u0abd\3\2\2\2\u01b0\u0ac2\3\2\2\2\u01b2\u0ac9\3")
        buf.write("\2\2\2\u01b4\u0acd\3\2\2\2\u01b6\u0ad4\3\2\2\2\u01b8\u0ad8")
        buf.write("\3\2\2\2\u01ba\u0add\3\2\2\2\u01bc\u0adf\3\2\2\2\u01be")
        buf.write("\u0ae8\3\2\2\2\u01c0\u0aef\3\2\2\2\u01c2\u0af1\3\2\2\2")
        buf.write("\u01c4\u0af3\3\2\2\2\u01c6\u0afc\3\2\2\2\u01c8\u0afe\3")
        buf.write("\2\2\2\u01ca\u0b03\3\2\2\2\u01cc\u0b0c\3\2\2\2\u01ce\u0b13")
        buf.write("\3\2\2\2\u01d0\u0b18\3\2\2\2\u01d2\u0b1e\3\2\2\2\u01d4")
        buf.write("\u0b29\3\2\2\2\u01d6\u0b2f\3\2\2\2\u01d8\u0b33\3\2\2\2")
        buf.write("\u01da\u0b36\3\2\2\2\u01dc\u0b3a\3\2\2\2\u01de\u0b3f\3")
        buf.write("\2\2\2\u01e0\u0b43\3\2\2\2\u01e2\u0b4d\3\2\2\2\u01e4\u0b51")
        buf.write("\3\2\2\2\u01e6\u0b5c\3\2\2\2\u01e8\u0b5e\3\2\2\2\u01ea")
        buf.write("\u0b60\3\2\2\2\u01ec\u0b62\3\2\2\2\u01ee\u0b69\3\2\2\2")
        buf.write("\u01f0\u0b6f\3\2\2\2\u01f2\u0b74\3\2\2\2\u01f4\u0b78\3")
        buf.write("\2\2\2\u01f6\u0b7a\3\2\2\2\u01f8\u0b7c\3\2\2\2\u01fa\u0b7e")
        buf.write("\3\2\2\2\u01fc\u0b80\3\2\2\2\u01fe\u0b82\3\2\2\2\u0200")
        buf.write("\u0b84\3\2\2\2\u0202\u0204\7\u0086\2\2\u0203\u0202\3\2")
        buf.write("\2\2\u0203\u0204\3\2\2\2\u0204\u0208\3\2\2\2\u0205\u0207")
        buf.write("\5\u01ec\u00f7\2\u0206\u0205\3\2\2\2\u0207\u020a\3\2\2")
        buf.write("\2\u0208\u0206\3\2\2\2\u0208\u0209\3\2\2\2\u0209\u020c")
        buf.write("\3\2\2\2\u020a\u0208\3\2\2\2\u020b\u020d\5\n\6\2\u020c")
        buf.write("\u020b\3\2\2\2\u020c\u020d\3\2\2\2\u020d\u0211\3\2\2\2")
        buf.write("\u020e\u0210\5\u01ec\u00f7\2\u020f\u020e\3\2\2\2\u0210")
        buf.write("\u0213\3\2\2\2\u0211\u020f\3\2\2\2\u0211\u0212\3\2\2\2")
        buf.write("\u0212\u0216\3\2\2\2\u0213\u0211\3\2\2\2\u0214\u0217\5")
        buf.write("\4\3\2\u0215\u0217\5\26\f\2\u0216\u0214\3\2\2\2\u0216")
        buf.write("\u0215\3\2\2\2\u0217\u0219\3\2\2\2\u0218\u021a\7\u0087")
        buf.write("\2\2\u0219\u0218\3\2\2\2\u0219\u021a\3\2\2\2\u021a\u021c")
        buf.write("\3\2\2\2\u021b\u021d\5\u01ec\u00f7\2\u021c\u021b\3\2\2")
        buf.write("\2\u021c\u021d\3\2\2\2\u021d\u021e\3\2\2\2\u021e\u021f")
        buf.write("\7\2\2\3\u021f\3\3\2\2\2\u0220\u0221\7\27\2\2\u0221\u0223")
        buf.write("\5\u01ee\u00f8\2\u0222\u0224\5\32\16\2\u0223\u0222\3\2")
        buf.write("\2\2\u0223\u0224\3\2\2\2\u0224\u0225\3\2\2\2\u0225\u0226")
        buf.write("\5\6\4\2\u0226\5\3\2\2\2\u0227\u0228\7\35\2\2\u0228\u0229")
        buf.write("\5\b\5\2\u0229\7\3\2\2\2\u022a\u022b\5\u01e8\u00f5\2\u022b")
        buf.write("\u022c\5\26\f\2\u022c\u0230\5\u01ea\u00f6\2\u022d\u022f")
        buf.write("\5\u01ec\u00f7\2\u022e\u022d\3\2\2\2\u022f\u0232\3\2\2")
        buf.write("\2\u0230\u022e\3\2\2\2\u0230\u0231\3\2\2\2\u0231\t\3\2")
        buf.write("\2\2\u0232\u0230\3\2\2\2\u0233\u0235\5\f\7\2\u0234\u0233")
        buf.write("\3\2\2\2\u0235\u0236\3\2\2\2\u0236\u0234\3\2\2\2\u0236")
        buf.write("\u0237\3\2\2\2\u0237\13\3\2\2\2\u0238\u023c\5\16\b\2\u0239")
        buf.write("\u023c\5\20\t\2\u023a\u023c\5\22\n\2\u023b\u0238\3\2\2")
        buf.write("\2\u023b\u0239\3\2\2\2\u023b\u023a\3\2\2\2\u023c\r\3\2")
        buf.write("\2\2\u023d\u023e\7\u0082\2\2\u023e\u023f\7\65\2\2\u023f")
        buf.write("\u0244\5\24\13\2\u0240\u0241\7h\2\2\u0241\u0243\5\24\13")
        buf.write("\2\u0242\u0240\3\2\2\2\u0243\u0246\3\2\2\2\u0244\u0242")
        buf.write("\3\2\2\2\u0244\u0245\3\2\2\2\u0245\u0247\3\2\2\2\u0246")
        buf.write("\u0244\3\2\2\2\u0247\u0249\7\u0083\2\2\u0248\u024a\5\u01ec")
        buf.write("\u00f7\2\u0249\u0248\3\2\2\2\u0249\u024a\3\2\2\2\u024a")
        buf.write("\17\3\2\2\2\u024b\u024c\7\u0082\2\2\u024c\u0254\7\66\2")
        buf.write("\2\u024d\u0250\7\\\2\2\u024e\u0251\5\u01d2\u00ea\2\u024f")
        buf.write("\u0251\5\u01e0\u00f1\2\u0250\u024e\3\2\2\2\u0250\u024f")
        buf.write("\3\2\2\2\u0251\u0253\3\2\2\2\u0252\u024d\3\2\2\2\u0253")
        buf.write("\u0256\3\2\2\2\u0254\u0252\3\2\2\2\u0254\u0255\3\2\2\2")
        buf.write("\u0255\u0257\3\2\2\2\u0256\u0254\3\2\2\2\u0257\u0259\7")
        buf.write("\u0083\2\2\u0258\u025a\5\u01ec\u00f7\2\u0259\u0258\3\2")
        buf.write("\2\2\u0259\u025a\3\2\2\2\u025a\21\3\2\2\2\u025b\u025c")
        buf.write("\7\u0082\2\2\u025c\u0264\7\67\2\2\u025d\u0260\7\\\2\2")
        buf.write("\u025e\u0261\5\u01d2\u00ea\2\u025f\u0261\5\u01e0\u00f1")
        buf.write("\2\u0260\u025e\3\2\2\2\u0260\u025f\3\2\2\2\u0261\u0263")
        buf.write("\3\2\2\2\u0262\u025d\3\2\2\2\u0263\u0266\3\2\2\2\u0264")
        buf.write("\u0262\3\2\2\2\u0264\u0265\3\2\2\2\u0265\u0267\3\2\2\2")
        buf.write("\u0266\u0264\3\2\2\2\u0267\u0269\7\u0083\2\2\u0268\u026a")
        buf.write("\5\u01ec\u00f7\2\u0269\u0268\3\2\2\2\u0269\u026a\3\2\2")
        buf.write("\2\u026a\23\3\2\2\2\u026b\u026c\7\u0081\2\2\u026c\25\3")
        buf.write("\2\2\2\u026d\u026e\5\30\r\2\u026e\u026f\5*\26\2\u026f")
        buf.write("\u0273\3\2\2\2\u0270\u0273\5\30\r\2\u0271\u0273\5*\26")
        buf.write("\2\u0272\u026d\3\2\2\2\u0272\u0270\3\2\2\2\u0272\u0271")
        buf.write("\3\2\2\2\u0273\27\3\2\2\2\u0274\u0278\5\36\20\2\u0275")
        buf.write("\u0278\7\3\2\2\u0276\u0278\5\u01ec\u00f7\2\u0277\u0274")
        buf.write("\3\2\2\2\u0277\u0275\3\2\2\2\u0277\u0276\3\2\2\2\u0278")
        buf.write("\u0279\3\2\2\2\u0279\u0277\3\2\2\2\u0279\u027a\3\2\2\2")
        buf.write("\u027a\31\3\2\2\2\u027b\u0284\7z\2\2\u027c\u0281\5\34")
        buf.write("\17\2\u027d\u027e\7h\2\2\u027e\u0280\5\34\17\2\u027f\u027d")
        buf.write("\3\2\2\2\u0280\u0283\3\2\2\2\u0281\u027f\3\2\2\2\u0281")
        buf.write("\u0282\3\2\2\2\u0282\u0285\3\2\2\2\u0283\u0281\3\2\2\2")
        buf.write("\u0284\u027c\3\2\2\2\u0284\u0285\3\2\2\2\u0285\u0287\3")
        buf.write("\2\2\2\u0286\u0288\7h\2\2\u0287\u0286\3\2\2\2\u0287\u0288")
        buf.write("\3\2\2\2\u0288\u0289\3\2\2\2\u0289\u028a\7{\2\2\u028a")
        buf.write("\33\3\2\2\2\u028b\u02b3\5\u01ce\u00e8\2\u028c\u029c\5")
        buf.write("\u01ac\u00d7\2\u028d\u028e\7z\2\2\u028e\u028f\7d\2\2\u028f")
        buf.write("\u029d\7{\2\2\u0290\u0299\7z\2\2\u0291\u0296\5$\23\2\u0292")
        buf.write("\u0293\7h\2\2\u0293\u0295\5$\23\2\u0294\u0292\3\2\2\2")
        buf.write("\u0295\u0298\3\2\2\2\u0296\u0294\3\2\2\2\u0296\u0297\3")
        buf.write("\2\2\2\u0297\u029a\3\2\2\2\u0298\u0296\3\2\2\2\u0299\u0291")
        buf.write("\3\2\2\2\u0299\u029a\3\2\2\2\u029a\u029b\3\2\2\2\u029b")
        buf.write("\u029d\7{\2\2\u029c\u028d\3\2\2\2\u029c\u0290\3\2\2\2")
        buf.write("\u029c\u029d\3\2\2\2\u029d\u02b3\3\2\2\2\u029e\u02ae\5")
        buf.write("\u01ca\u00e6\2\u029f\u02a0\7z\2\2\u02a0\u02a1\7d\2\2\u02a1")
        buf.write("\u02af\7{\2\2\u02a2\u02ab\7z\2\2\u02a3\u02a8\5\u01ce\u00e8")
        buf.write("\2\u02a4\u02a5\7h\2\2\u02a5\u02a7\5\u01ce\u00e8\2\u02a6")
        buf.write("\u02a4\3\2\2\2\u02a7\u02aa\3\2\2\2\u02a8\u02a6\3\2\2\2")
        buf.write("\u02a8\u02a9\3\2\2\2\u02a9\u02ac\3\2\2\2\u02aa\u02a8\3")
        buf.write("\2\2\2\u02ab\u02a3\3\2\2\2\u02ab\u02ac\3\2\2\2\u02ac\u02ad")
        buf.write("\3\2\2\2\u02ad\u02af\7{\2\2\u02ae\u029f\3\2\2\2\u02ae")
        buf.write("\u02a2\3\2\2\2\u02ae\u02af\3\2\2\2\u02af\u02b3\3\2\2\2")
        buf.write("\u02b0\u02b1\7\27\2\2\u02b1\u02b3\5\u01ee\u00f8\2\u02b2")
        buf.write("\u028b\3\2\2\2\u02b2\u028c\3\2\2\2\u02b2\u029e\3\2\2\2")
        buf.write("\u02b2\u02b0\3\2\2\2\u02b3\35\3\2\2\2\u02b4\u02b6\7\20")
        buf.write("\2\2\u02b5\u02b7\7\32\2\2\u02b6\u02b5\3\2\2\2\u02b6\u02b7")
        buf.write("\3\2\2\2\u02b7\u02b8\3\2\2\2\u02b8\u02bb\5\u01ee\u00f8")
        buf.write("\2\u02b9\u02ba\7\6\2\2\u02ba\u02bc\5\u01ee\u00f8\2\u02bb")
        buf.write("\u02b9\3\2\2\2\u02bb\u02bc\3\2\2\2\u02bc\u02be\3\2\2\2")
        buf.write("\u02bd\u02bf\5 \21\2\u02be\u02bd\3\2\2\2\u02be\u02bf\3")
        buf.write("\2\2\2\u02bf\u02c1\3\2\2\2\u02c0\u02c2\5\u01ec\u00f7\2")
        buf.write("\u02c1\u02c0\3\2\2\2\u02c2\u02c3\3\2\2\2\u02c3\u02c1\3")
        buf.write("\2\2\2\u02c3\u02c4\3\2\2\2\u02c4\37\3\2\2\2\u02c5\u02d1")
        buf.write("\7z\2\2\u02c6\u02cb\5\"\22\2\u02c7\u02c8\7h\2\2\u02c8")
        buf.write("\u02ca\5\"\22\2\u02c9\u02c7\3\2\2\2\u02ca\u02cd\3\2\2")
        buf.write("\2\u02cb\u02c9\3\2\2\2\u02cb\u02cc\3\2\2\2\u02cc\u02cf")
        buf.write("\3\2\2\2\u02cd\u02cb\3\2\2\2\u02ce\u02d0\7h\2\2\u02cf")
        buf.write("\u02ce\3\2\2\2\u02cf\u02d0\3\2\2\2\u02d0\u02d2\3\2\2\2")
        buf.write("\u02d1\u02c6\3\2\2\2\u02d1\u02d2\3\2\2\2\u02d2\u02d3\3")
        buf.write("\2\2\2\u02d3\u02e5\7{\2\2\u02d4\u02d5\7\16\2\2\u02d5\u02e1")
        buf.write("\7z\2\2\u02d6\u02db\5\"\22\2\u02d7\u02d8\7h\2\2\u02d8")
        buf.write("\u02da\5\"\22\2\u02d9\u02d7\3\2\2\2\u02da\u02dd\3\2\2")
        buf.write("\2\u02db\u02d9\3\2\2\2\u02db\u02dc\3\2\2\2\u02dc\u02df")
        buf.write("\3\2\2\2\u02dd\u02db\3\2\2\2\u02de\u02e0\7h\2\2\u02df")
        buf.write("\u02de\3\2\2\2\u02df\u02e0\3\2\2\2\u02e0\u02e2\3\2\2\2")
        buf.write("\u02e1\u02d6\3\2\2\2\u02e1\u02e2\3\2\2\2\u02e2\u02e3\3")
        buf.write("\2\2\2\u02e3\u02e5\7{\2\2\u02e4\u02c5\3\2\2\2\u02e4\u02d4")
        buf.write("\3\2\2\2\u02e5!\3\2\2\2\u02e6\u0305\5\u01cc\u00e7\2\u02e7")
        buf.write("\u02f7\5\u01ae\u00d8\2\u02e8\u02e9\7z\2\2\u02e9\u02ea")
        buf.write("\7d\2\2\u02ea\u02f8\7{\2\2\u02eb\u02f4\7z\2\2\u02ec\u02f1")
        buf.write("\5$\23\2\u02ed\u02ee\7h\2\2\u02ee\u02f0\5$\23\2\u02ef")
        buf.write("\u02ed\3\2\2\2\u02f0\u02f3\3\2\2\2\u02f1\u02ef\3\2\2\2")
        buf.write("\u02f1\u02f2\3\2\2\2\u02f2\u02f5\3\2\2\2\u02f3\u02f1\3")
        buf.write("\2\2\2\u02f4\u02ec\3\2\2\2\u02f4\u02f5\3\2\2\2\u02f5\u02f6")
        buf.write("\3\2\2\2\u02f6\u02f8\7{\2\2\u02f7\u02e8\3\2\2\2\u02f7")
        buf.write("\u02eb\3\2\2\2\u02f7\u02f8\3\2\2\2\u02f8\u0305\3\2\2\2")
        buf.write("\u02f9\u0302\5\u01c8\u00e5\2\u02fa\u02fb\7z\2\2\u02fb")
        buf.write("\u02fc\7d\2\2\u02fc\u0303\7{\2\2\u02fd\u02ff\7z\2\2\u02fe")
        buf.write("\u0300\5\u00b8]\2\u02ff\u02fe\3\2\2\2\u02ff\u0300\3\2")
        buf.write("\2\2\u0300\u0301\3\2\2\2\u0301\u0303\7{\2\2\u0302\u02fa")
        buf.write("\3\2\2\2\u0302\u02fd\3\2\2\2\u0302\u0303\3\2\2\2\u0303")
        buf.write("\u0305\3\2\2\2\u0304\u02e6\3\2\2\2\u0304\u02e7\3\2\2\2")
        buf.write("\u0304\u02f9\3\2\2\2\u0305#\3\2\2\2\u0306\u0309\5\u01cc")
        buf.write("\u00e7\2\u0307\u0309\5\u0196\u00cc\2\u0308\u0306\3\2\2")
        buf.write("\2\u0308\u0307\3\2\2\2\u0309%\3\2\2\2\u030a\u030b\t\2")
        buf.write("\2\2\u030b\'\3\2\2\2\u030c\u0311\5\u01b4\u00db\2\u030d")
        buf.write("\u030e\7h\2\2\u030e\u0310\5\u01b4\u00db\2\u030f\u030d")
        buf.write("\3\2\2\2\u0310\u0313\3\2\2\2\u0311\u030f\3\2\2\2\u0311")
        buf.write("\u0312\3\2\2\2\u0312)\3\2\2\2\u0313\u0311\3\2\2\2\u0314")
        buf.write("\u0316\5,\27\2\u0315\u0317\5\u01ec\u00f7\2\u0316\u0315")
        buf.write("\3\2\2\2\u0317\u0318\3\2\2\2\u0318\u0316\3\2\2\2\u0318")
        buf.write("\u0319\3\2\2\2\u0319\u031d\3\2\2\2\u031a\u031d\7\3\2\2")
        buf.write("\u031b\u031d\5\u01ec\u00f7\2\u031c\u0314\3\2\2\2\u031c")
        buf.write("\u031a\3\2\2\2\u031c\u031b\3\2\2\2\u031d\u031e\3\2\2\2")
        buf.write("\u031e\u031c\3\2\2\2\u031e\u031f\3\2\2\2\u031f+\3\2\2")
        buf.write("\2\u0320\u0344\5.\30\2\u0321\u0344\5\60\31\2\u0322\u0344")
        buf.write("\5\62\32\2\u0323\u0344\5\66\34\2\u0324\u0344\5`\61\2\u0325")
        buf.write("\u0344\5b\62\2\u0326\u0327\7\n\2\2\u0327\u0329\7z\2\2")
        buf.write("\u0328\u032a\5\u00e2r\2\u0329\u0328\3\2\2\2\u0329\u032a")
        buf.write("\3\2\2\2\u032a\u032b\3\2\2\2\u032b\u0344\7{\2\2\u032c")
        buf.write("\u032d\7 \2\2\u032d\u0344\5\u00a8U\2\u032e\u032f\7\u0082")
        buf.write("\2\2\u032f\u0331\7?\2\2\u0330\u0332\5\u009eP\2\u0331\u0330")
        buf.write("\3\2\2\2\u0331\u0332\3\2\2\2\u0332\u0333\3\2\2\2\u0333")
        buf.write("\u0344\7\u0083\2\2\u0334\u0335\7\u0082\2\2\u0335\u0337")
        buf.write("\7@\2\2\u0336\u0338\5\u009aN\2\u0337\u0336\3\2\2\2\u0337")
        buf.write("\u0338\3\2\2\2\u0338\u0339\3\2\2\2\u0339\u0344\7\u0083")
        buf.write("\2\2\u033a\u033b\7\u0082\2\2\u033b\u033d\7=\2\2\u033c")
        buf.write("\u033e\5\u008cG\2\u033d\u033c\3\2\2\2\u033d\u033e\3\2")
        buf.write("\2\2\u033e\u033f\3\2\2\2\u033f\u0344\7\u0083\2\2\u0340")
        buf.write("\u0344\5\u00a6T\2\u0341\u0344\5\u0112\u008a\2\u0342\u0344")
        buf.write("\5\u0128\u0095\2\u0343\u0320\3\2\2\2\u0343\u0321\3\2\2")
        buf.write("\2\u0343\u0322\3\2\2\2\u0343\u0323\3\2\2\2\u0343\u0324")
        buf.write("\3\2\2\2\u0343\u0325\3\2\2\2\u0343\u0326\3\2\2\2\u0343")
        buf.write("\u032c\3\2\2\2\u0343\u032e\3\2\2\2\u0343\u0334\3\2\2\2")
        buf.write("\u0343\u033a\3\2\2\2\u0343\u0340\3\2\2\2\u0343\u0341\3")
        buf.write("\2\2\2\u0343\u0342\3\2\2\2\u0344-\3\2\2\2\u0345\u0346")
        buf.write("\7\b\2\2\u0346\u0348\5Z.\2\u0347\u0349\5\u00ecw\2\u0348")
        buf.write("\u0347\3\2\2\2\u0348\u0349\3\2\2\2\u0349\u034b\3\2\2\2")
        buf.write("\u034a\u034c\5z>\2\u034b\u034a\3\2\2\2\u034b\u034c\3\2")
        buf.write("\2\2\u034c/\3\2\2\2\u034d\u034e\7\34\2\2\u034e\u034f\5")
        buf.write("\u00ccg\2\u034f\u0350\7j\2\2\u0350\u0351\5\u00c2b\2\u0351")
        buf.write("\u0393\3\2\2\2\u0352\u0353\7\34\2\2\u0353\u0354\7&\2\2")
        buf.write("\u0354\u0356\5\u00ccg\2\u0355\u0357\5V,\2\u0356\u0355")
        buf.write("\3\2\2\2\u0356\u0357\3\2\2\2\u0357\u0359\3\2\2\2\u0358")
        buf.write("\u035a\5@!\2\u0359\u0358\3\2\2\2\u0359\u035a\3\2\2\2\u035a")
        buf.write("\u035c\3\2\2\2\u035b\u035d\5F$\2\u035c\u035b\3\2\2\2\u035c")
        buf.write("\u035d\3\2\2\2\u035d\u0393\3\2\2\2\u035e\u0360\7\t\2\2")
        buf.write("\u035f\u0361\5^\60\2\u0360\u035f\3\2\2\2\u0360\u0361\3")
        buf.write("\2\2\2\u0361\u0362\3\2\2\2\u0362\u0363\5Z.\2\u0363\u0365")
        buf.write("\5\u00fe\u0080\2\u0364\u0366\5\u010c\u0087\2\u0365\u0364")
        buf.write("\3\2\2\2\u0365\u0366\3\2\2\2\u0366\u0393\3\2\2\2\u0367")
        buf.write("\u0369\7\30\2\2\u0368\u036a\5^\60\2\u0369\u0368\3\2\2")
        buf.write("\2\u0369\u036a\3\2\2\2\u036a\u036b\3\2\2\2\u036b\u036c")
        buf.write("\5Z.\2\u036c\u036e\5\u00fe\u0080\2\u036d\u036f\5\u010c")
        buf.write("\u0087\2\u036e\u036d\3\2\2\2\u036e\u036f\3\2\2\2\u036f")
        buf.write("\u0393\3\2\2\2\u0370\u0372\7\t\2\2\u0371\u0373\5^\60\2")
        buf.write("\u0372\u0371\3\2\2\2\u0372\u0373\3\2\2\2\u0373\u0374\3")
        buf.write("\2\2\2\u0374\u0376\5Z.\2\u0375\u0377\5R*\2\u0376\u0375")
        buf.write("\3\2\2\2\u0376\u0377\3\2\2\2\u0377\u0379\3\2\2\2\u0378")
        buf.write("\u037a\5\u00f6|\2\u0379\u0378\3\2\2\2\u0379\u037a\3\2")
        buf.write("\2\2\u037a\u037c\3\2\2\2\u037b\u037d\5\u010c\u0087\2\u037c")
        buf.write("\u037b\3\2\2\2\u037c\u037d\3\2\2\2\u037d\u0393\3\2\2\2")
        buf.write("\u037e\u0380\7\30\2\2\u037f\u0381\5^\60\2\u0380\u037f")
        buf.write("\3\2\2\2\u0380\u0381\3\2\2\2\u0381\u0382\3\2\2\2\u0382")
        buf.write("\u0384\5Z.\2\u0383\u0385\5R*\2\u0384\u0383\3\2\2\2\u0384")
        buf.write("\u0385\3\2\2\2\u0385\u0387\3\2\2\2\u0386\u0388\5\u00f6")
        buf.write("|\2\u0387\u0386\3\2\2\2\u0387\u0388\3\2\2\2\u0388\u038a")
        buf.write("\3\2\2\2\u0389\u038b\5\u010c\u0087\2\u038a\u0389\3\2\2")
        buf.write("\2\u038a\u038b\3\2\2\2\u038b\u0393\3\2\2\2\u038c\u038d")
        buf.write("\7\t\2\2\u038d\u038e\7&\2\2\u038e\u0390\5\u00ccg\2\u038f")
        buf.write("\u0391\5T+\2\u0390\u038f\3\2\2\2\u0390\u0391\3\2\2\2\u0391")
        buf.write("\u0393\3\2\2\2\u0392\u034d\3\2\2\2\u0392\u0352\3\2\2\2")
        buf.write("\u0392\u035e\3\2\2\2\u0392\u0367\3\2\2\2\u0392\u0370\3")
        buf.write("\2\2\2\u0392\u037e\3\2\2\2\u0392\u038c\3\2\2\2\u0393\61")
        buf.write("\3\2\2\2\u0394\u0395\7\34\2\2\u0395\u0396\5\64\33\2\u0396")
        buf.write("\u0397\7M\2\2\u0397\u0398\5\u00c2b\2\u0398\63\3\2\2\2")
        buf.write("\u0399\u039e\5\u01a8\u00d5\2\u039a\u039b\7h\2\2\u039b")
        buf.write("\u039d\5\u01a8\u00d5\2\u039c\u039a\3\2\2\2\u039d\u03a0")
        buf.write("\3\2\2\2\u039e\u039c\3\2\2\2\u039e\u039f\3\2\2\2\u039f")
        buf.write("\65\3\2\2\2\u03a0\u039e\3\2\2\2\u03a1\u03a3\7\25\2\2\u03a2")
        buf.write("\u03a4\58\35\2\u03a3\u03a2\3\2\2\2\u03a3\u03a4\3\2\2\2")
        buf.write("\u03a4\u03a5\3\2\2\2\u03a5\u03a7\5\u00dep\2\u03a6\u03a8")
        buf.write("\5\u0082B\2\u03a7\u03a6\3\2\2\2\u03a7\u03a8\3\2\2\2\u03a8")
        buf.write("\u03dd\3\2\2\2\u03a9\u03aa\7\34\2\2\u03aa\u03ab\7\25\2")
        buf.write("\2\u03ab\u03dd\5L\'\2\u03ac\u03ad\7\t\2\2\u03ad\u03af")
        buf.write("\7\25\2\2\u03ae\u03b0\5^\60\2\u03af\u03ae\3\2\2\2\u03af")
        buf.write("\u03b0\3\2\2\2\u03b0\u03b1\3\2\2\2\u03b1\u03b3\5\\/\2")
        buf.write("\u03b2\u03b4\5\u010c\u0087\2\u03b3\u03b2\3\2\2\2\u03b3")
        buf.write("\u03b4\3\2\2\2\u03b4\u03dd\3\2\2\2\u03b5\u03b6\7\30\2")
        buf.write("\2\u03b6\u03b8\7\25\2\2\u03b7\u03b9\5^\60\2\u03b8\u03b7")
        buf.write("\3\2\2\2\u03b8\u03b9\3\2\2\2\u03b9\u03ba\3\2\2\2\u03ba")
        buf.write("\u03bc\5\\/\2\u03bb\u03bd\5\u010c\u0087\2\u03bc\u03bb")
        buf.write("\3\2\2\2\u03bc\u03bd\3\2\2\2\u03bd\u03dd\3\2\2\2\u03be")
        buf.write("\u03bf\7\t\2\2\u03bf\u03c1\7\25\2\2\u03c0\u03c2\5^\60")
        buf.write("\2\u03c1\u03c0\3\2\2\2\u03c1\u03c2\3\2\2\2\u03c2\u03c3")
        buf.write("\3\2\2\2\u03c3\u03c5\5\\/\2\u03c4\u03c6\5R*\2\u03c5\u03c4")
        buf.write("\3\2\2\2\u03c5\u03c6\3\2\2\2\u03c6\u03c8\3\2\2\2\u03c7")
        buf.write("\u03c9\5\u00f6|\2\u03c8\u03c7\3\2\2\2\u03c8\u03c9\3\2")
        buf.write("\2\2\u03c9\u03cb\3\2\2\2\u03ca\u03cc\5\u010c\u0087\2\u03cb")
        buf.write("\u03ca\3\2\2\2\u03cb\u03cc\3\2\2\2\u03cc\u03dd\3\2\2\2")
        buf.write("\u03cd\u03ce\7\30\2\2\u03ce\u03d0\7\25\2\2\u03cf\u03d1")
        buf.write("\5^\60\2\u03d0\u03cf\3\2\2\2\u03d0\u03d1\3\2\2\2\u03d1")
        buf.write("\u03d2\3\2\2\2\u03d2\u03d4\5\\/\2\u03d3\u03d5\5R*\2\u03d4")
        buf.write("\u03d3\3\2\2\2\u03d4\u03d5\3\2\2\2\u03d5\u03d7\3\2\2\2")
        buf.write("\u03d6\u03d8\5\u00f6|\2\u03d7\u03d6\3\2\2\2\u03d7\u03d8")
        buf.write("\3\2\2\2\u03d8\u03da\3\2\2\2\u03d9\u03db\5\u010c\u0087")
        buf.write("\2\u03da\u03d9\3\2\2\2\u03da\u03db\3\2\2\2\u03db\u03dd")
        buf.write("\3\2\2\2\u03dc\u03a1\3\2\2\2\u03dc\u03a9\3\2\2\2\u03dc")
        buf.write("\u03ac\3\2\2\2\u03dc\u03b5\3\2\2\2\u03dc\u03be\3\2\2\2")
        buf.write("\u03dc\u03cd\3\2\2\2\u03dd\67\3\2\2\2\u03de\u03df\7\u0082")
        buf.write("\2\2\u03df\u03e0\7G\2\2\u03e0\u03eb\7\u0083\2\2\u03e1")
        buf.write("\u03e2\7\u0082\2\2\u03e2\u03e3\7F\2\2\u03e3\u03eb\7\u0083")
        buf.write("\2\2\u03e4\u03e5\7\u0082\2\2\u03e5\u03e6\7H\2\2\u03e6")
        buf.write("\u03eb\7\u0083\2\2\u03e7\u03e8\7\u0082\2\2\u03e8\u03e9")
        buf.write("\7I\2\2\u03e9\u03eb\7\u0083\2\2\u03ea\u03de\3\2\2\2\u03ea")
        buf.write("\u03e1\3\2\2\2\u03ea\u03e4\3\2\2\2\u03ea\u03e7\3\2\2\2")
        buf.write("\u03eb9\3\2\2\2\u03ec\u03ed\t\3\2\2\u03ed;\3\2\2\2\u03ee")
        buf.write("\u03ef\7\64\2\2\u03ef\u03f0\5\u00c0a\2\u03f0=\3\2\2\2")
        buf.write("\u03f1\u03f6\7\62\2\2\u03f2\u03f6\7\63\2\2\u03f3\u03f6")
        buf.write("\7\30\2\2\u03f4\u03f6\5<\37\2\u03f5\u03f1\3\2\2\2\u03f5")
        buf.write("\u03f2\3\2\2\2\u03f5\u03f3\3\2\2\2\u03f5\u03f4\3\2\2\2")
        buf.write("\u03f6?\3\2\2\2\u03f7\u03f8\7X\2\2\u03f8\u03f9\5B\"\2")
        buf.write("\u03f9A\3\2\2\2\u03fa\u03fb\5\u01c6\u00e4\2\u03fb\u03fc")
        buf.write("\7N\2\2\u03fc\u03fd\5D#\2\u03fdC\3\2\2\2\u03fe\u0400\5")
        buf.write("\u01c6\u00e4\2\u03ff\u03fe\3\2\2\2\u0400\u0401\3\2\2\2")
        buf.write("\u0401\u03ff\3\2\2\2\u0401\u0402\3\2\2\2\u0402E\3\2\2")
        buf.write("\2\u0403\u0404\7\35\2\2\u0404\u0405\5H%\2\u0405G\3\2\2")
        buf.write("\2\u0406\u0408\5\u01e8\u00f5\2\u0407\u0409\5J&\2\u0408")
        buf.write("\u0407\3\2\2\2\u0408\u0409\3\2\2\2\u0409\u040a\3\2\2\2")
        buf.write("\u040a\u040b\5\u01ea\u00f6\2\u040b\u0414\3\2\2\2\u040c")
        buf.write("\u040d\7\u0086\2\2\u040d\u040e\7d\2\2\u040e\u0414\7\u0087")
        buf.write("\2\2\u040f\u0410\5\u01e8\u00f5\2\u0410\u0411\7d\2\2\u0411")
        buf.write("\u0412\5\u01ea\u00f6\2\u0412\u0414\3\2\2\2\u0413\u0406")
        buf.write("\3\2\2\2\u0413\u040c\3\2\2\2\u0413\u040f\3\2\2\2\u0414")
        buf.write("I\3\2\2\2\u0415\u041f\5L\'\2\u0416\u0418\5\u01ec\u00f7")
        buf.write("\2\u0417\u0416\3\2\2\2\u0418\u0419\3\2\2\2\u0419\u0417")
        buf.write("\3\2\2\2\u0419\u041a\3\2\2\2\u041a\u041b\3\2\2\2\u041b")
        buf.write("\u041c\5L\'\2\u041c\u041e\3\2\2\2\u041d\u0417\3\2\2\2")
        buf.write("\u041e\u0421\3\2\2\2\u041f\u041d\3\2\2\2\u041f\u0420\3")
        buf.write("\2\2\2\u0420\u0425\3\2\2\2\u0421\u041f\3\2\2\2\u0422\u0424")
        buf.write("\5\u01ec\u00f7\2\u0423\u0422\3\2\2\2\u0424\u0427\3\2\2")
        buf.write("\2\u0425\u0423\3\2\2\2\u0425\u0426\3\2\2\2\u0426K\3\2")
        buf.write("\2\2\u0427\u0425\3\2\2\2\u0428\u042a\7\37\2\2\u0429\u042b")
        buf.write("\5\u00e6t\2\u042a\u0429\3\2\2\2\u042a\u042b\3\2\2\2\u042b")
        buf.write("\u042c\3\2\2\2\u042c\u042d\7e\2\2\u042d\u042e\5\u00cc")
        buf.write("g\2\u042e\u042f\7j\2\2\u042f\u0430\5\u00c0a\2\u0430\u0436")
        buf.write("\3\2\2\2\u0431\u0432\5\u00ccg\2\u0432\u0433\7j\2\2\u0433")
        buf.write("\u0434\5\u00c0a\2\u0434\u0436\3\2\2\2\u0435\u0428\3\2")
        buf.write("\2\2\u0435\u0431\3\2\2\2\u0436M\3\2\2\2\u0437\u0439\7")
        buf.write("\t\2\2\u0438\u043a\7&\2\2\u0439\u0438\3\2\2\2\u0439\u043a")
        buf.write("\3\2\2\2\u043a\u043b\3\2\2\2\u043b\u043d\5\u00ccg\2\u043c")
        buf.write("\u043e\5T+\2\u043d\u043c\3\2\2\2\u043d\u043e\3\2\2\2\u043e")
        buf.write("\u044d\3\2\2\2\u043f\u0441\7\34\2\2\u0440\u0442\7&\2\2")
        buf.write("\u0441\u0440\3\2\2\2\u0441\u0442\3\2\2\2\u0442\u0443\3")
        buf.write("\2\2\2\u0443\u0445\5\u00ccg\2\u0444\u0446\5X-\2\u0445")
        buf.write("\u0444\3\2\2\2\u0445\u0446\3\2\2\2\u0446\u044d\3\2\2\2")
        buf.write("\u0447\u0449\7\34\2\2\u0448\u044a\7\25\2\2\u0449\u0448")
        buf.write("\3\2\2\2\u0449\u044a\3\2\2\2\u044a\u044b\3\2\2\2\u044b")
        buf.write("\u044d\5L\'\2\u044c\u0437\3\2\2\2\u044c\u043f\3\2\2\2")
        buf.write("\u044c\u0447\3\2\2\2\u044dO\3\2\2\2\u044e\u0450\7\34\2")
        buf.write("\2\u044f\u0451\7\25\2\2\u0450\u044f\3\2\2\2\u0450\u0451")
        buf.write("\3\2\2\2\u0451\u0452\3\2\2\2\u0452\u048e\5L\'\2\u0453")
        buf.write("\u0455\7\t\2\2\u0454\u0456\7\25\2\2\u0455\u0454\3\2\2")
        buf.write("\2\u0455\u0456\3\2\2\2\u0456\u0458\3\2\2\2\u0457\u0459")
        buf.write("\5^\60\2\u0458\u0457\3\2\2\2\u0458\u0459\3\2\2\2\u0459")
        buf.write("\u045a\3\2\2\2\u045a\u045b\5\\/\2\u045b\u045d\5\u00fe")
        buf.write("\u0080\2\u045c\u045e\5\u010c\u0087\2\u045d\u045c\3\2\2")
        buf.write("\2\u045d\u045e\3\2\2\2\u045e\u048e\3\2\2\2\u045f\u0461")
        buf.write("\7\30\2\2\u0460\u0462\7\25\2\2\u0461\u0460\3\2\2\2\u0461")
        buf.write("\u0462\3\2\2\2\u0462\u0464\3\2\2\2\u0463\u0465\5^\60\2")
        buf.write("\u0464\u0463\3\2\2\2\u0464\u0465\3\2\2\2\u0465\u0466\3")
        buf.write("\2\2\2\u0466\u0467\5\\/\2\u0467\u0469\5\u00fe\u0080\2")
        buf.write("\u0468\u046a\5\u010c\u0087\2\u0469\u0468\3\2\2\2\u0469")
        buf.write("\u046a\3\2\2\2\u046a\u048e\3\2\2\2\u046b\u046d\7\t\2\2")
        buf.write("\u046c\u046e\7\25\2\2\u046d\u046c\3\2\2\2\u046d\u046e")
        buf.write("\3\2\2\2\u046e\u0470\3\2\2\2\u046f\u0471\5^\60\2\u0470")
        buf.write("\u046f\3\2\2\2\u0470\u0471\3\2\2\2\u0471\u0472\3\2\2\2")
        buf.write("\u0472\u0474\5\\/\2\u0473\u0475\5R*\2\u0474\u0473\3\2")
        buf.write("\2\2\u0474\u0475\3\2\2\2\u0475\u0477\3\2\2\2\u0476\u0478")
        buf.write("\5\u00f6|\2\u0477\u0476\3\2\2\2\u0477\u0478\3\2\2\2\u0478")
        buf.write("\u047a\3\2\2\2\u0479\u047b\5\u010c\u0087\2\u047a\u0479")
        buf.write("\3\2\2\2\u047a\u047b\3\2\2\2\u047b\u048e\3\2\2\2\u047c")
        buf.write("\u047e\7\30\2\2\u047d\u047f\7\25\2\2\u047e\u047d\3\2\2")
        buf.write("\2\u047e\u047f\3\2\2\2\u047f\u0481\3\2\2\2\u0480\u0482")
        buf.write("\5^\60\2\u0481\u0480\3\2\2\2\u0481\u0482\3\2\2\2\u0482")
        buf.write("\u0483\3\2\2\2\u0483\u0485\5\\/\2\u0484\u0486\5R*\2\u0485")
        buf.write("\u0484\3\2\2\2\u0485\u0486\3\2\2\2\u0486\u0488\3\2\2\2")
        buf.write("\u0487\u0489\5\u00f6|\2\u0488\u0487\3\2\2\2\u0488\u0489")
        buf.write("\3\2\2\2\u0489\u048b\3\2\2\2\u048a\u048c\5\u010c\u0087")
        buf.write("\2\u048b\u048a\3\2\2\2\u048b\u048c\3\2\2\2\u048c\u048e")
        buf.write("\3\2\2\2\u048d\u044e\3\2\2\2\u048d\u0453\3\2\2\2\u048d")
        buf.write("\u045f\3\2\2\2\u048d\u046b\3\2\2\2\u048d\u047c\3\2\2\2")
        buf.write("\u048eQ\3\2\2\2\u048f\u0490\7M\2\2\u0490\u0491\5\u00f4")
        buf.write("{\2\u0491S\3\2\2\2\u0492\u0493\7M\2\2\u0493\u0494\5\u00f4")
        buf.write("{\2\u0494U\3\2\2\2\u0495\u0496\7M\2\2\u0496\u049a\5\u00f4")
        buf.write("{\2\u0497\u0498\7j\2\2\u0498\u049a\5\u00e8u\2\u0499\u0495")
        buf.write("\3\2\2\2\u0499\u0497\3\2\2\2\u049aW\3\2\2\2\u049b\u049c")
        buf.write("\7M\2\2\u049c\u04a3\5\u00f4{\2\u049d\u049e\7j\2\2\u049e")
        buf.write("\u049f\5\u00eav\2\u049f\u04a0\7X\2\2\u04a0\u04a1\5B\"")
        buf.write("\2\u04a1\u04a3\3\2\2\2\u04a2\u049b\3\2\2\2\u04a2\u049d")
        buf.write("\3\2\2\2\u04a3Y\3\2\2\2\u04a4\u04a5\5\u00c8e\2\u04a5\u04a6")
        buf.write("\7L\2\2\u04a6\u04a7\5\u00ccg\2\u04a7\u04aa\3\2\2\2\u04a8")
        buf.write("\u04aa\5\u00ccg\2\u04a9\u04a4\3\2\2\2\u04a9\u04a8\3\2")
        buf.write("\2\2\u04aa[\3\2\2\2\u04ab\u04ad\7\37\2\2\u04ac\u04ae\5")
        buf.write("\u00e6t\2\u04ad\u04ac\3\2\2\2\u04ad\u04ae\3\2\2\2\u04ae")
        buf.write("\u04af\3\2\2\2\u04af\u04b0\7e\2\2\u04b0\u04b1\5\u00c8")
        buf.write("e\2\u04b1\u04b2\7L\2\2\u04b2\u04b3\5\u00ccg\2\u04b3\u04c0")
        buf.write("\3\2\2\2\u04b4\u04b6\7\37\2\2\u04b5\u04b7\5\u00e6t\2\u04b6")
        buf.write("\u04b5\3\2\2\2\u04b6\u04b7\3\2\2\2\u04b7\u04b8\3\2\2\2")
        buf.write("\u04b8\u04b9\7e\2\2\u04b9\u04c0\5\u00ccg\2\u04ba\u04bb")
        buf.write("\5\u00c8e\2\u04bb\u04bc\7L\2\2\u04bc\u04bd\5\u00ccg\2")
        buf.write("\u04bd\u04c0\3\2\2\2\u04be\u04c0\5\u00ccg\2\u04bf\u04ab")
        buf.write("\3\2\2\2\u04bf\u04b4\3\2\2\2\u04bf\u04ba\3\2\2\2\u04bf")
        buf.write("\u04be\3\2\2\2\u04c0]\3\2\2\2\u04c1\u04c2\7\u0082\2\2")
        buf.write("\u04c2\u04c3\7E\2\2\u04c3\u04c4\7\177\2\2\u04c4\u04c5")
        buf.write("\7\177\2\2\u04c5\u04cb\7\u0083\2\2\u04c6\u04c7\7\u0082")
        buf.write("\2\2\u04c7\u04c8\7E\2\2\u04c8\u04c9\7\177\2\2\u04c9\u04cb")
        buf.write("\7\u0083\2\2\u04ca\u04c1\3\2\2\2\u04ca\u04c6\3\2\2\2\u04cb")
        buf.write("_\3\2\2\2\u04cc\u04ce\7\13\2\2\u04cd\u04cf\5> \2\u04ce")
        buf.write("\u04cd\3\2\2\2\u04ce\u04cf\3\2\2\2\u04cf\u04d0\3\2\2\2")
        buf.write("\u04d0\u04d2\7\25\2\2\u04d1\u04d3\58\35\2\u04d2\u04d1")
        buf.write("\3\2\2\2\u04d2\u04d3\3\2\2\2\u04d3\u04d4\3\2\2\2\u04d4")
        buf.write("\u04d5\5\u00dep\2\u04d5a\3\2\2\2\u04d6\u04d7\7\34\2\2")
        buf.write("\u04d7\u04d8\7\'\2\2\u04d8\u04da\5\u01a8\u00d5\2\u04d9")
        buf.write("\u04db\5d\63\2\u04da\u04d9\3\2\2\2\u04da\u04db\3\2\2\2")
        buf.write("\u04dbc\3\2\2\2\u04dc\u04de\5f\64\2\u04dd\u04dc\3\2\2")
        buf.write("\2\u04de\u04df\3\2\2\2\u04df\u04dd\3\2\2\2\u04df\u04e0")
        buf.write("\3\2\2\2\u04e0e\3\2\2\2\u04e1\u04e4\5\u01d2\u00ea\2\u04e2")
        buf.write("\u04e4\7\36\2\2\u04e3\u04e1\3\2\2\2\u04e3\u04e2\3\2\2")
        buf.write("\2\u04e4g\3\2\2\2\u04e5\u04e6\7\61\2\2\u04e6\u04e7\5j")
        buf.write("\66\2\u04e7\u04e8\7j\2\2\u04e8\u04e9\5\u016a\u00b6\2\u04e9")
        buf.write("\u04f2\3\2\2\2\u04ea\u04eb\7\61\2\2\u04eb\u04ec\5j\66")
        buf.write("\2\u04ec\u04ed\7O\2\2\u04ed\u04ef\5\u016a\u00b6\2\u04ee")
        buf.write("\u04f0\5p9\2\u04ef\u04ee\3\2\2\2\u04ef\u04f0\3\2\2\2\u04f0")
        buf.write("\u04f2\3\2\2\2\u04f1\u04e5\3\2\2\2\u04f1\u04ea\3\2\2\2")
        buf.write("\u04f2i\3\2\2\2\u04f3\u04f5\5\u0196\u00cc\2\u04f4\u04f6")
        buf.write("\5l\67\2\u04f5\u04f4\3\2\2\2\u04f5\u04f6\3\2\2\2\u04f6")
        buf.write("\u0501\3\2\2\2\u04f7\u04f8\5\u01d2\u00ea\2\u04f8\u04f9")
        buf.write("\5\u019e\u00d0\2\u04f9\u04fa\5\u01d2\u00ea\2\u04fa\u0501")
        buf.write("\3\2\2\2\u04fb\u04fc\5\u0196\u00cc\2\u04fc\u04fd\7\u0086")
        buf.write("\2\2\u04fd\u04fe\5n8\2\u04fe\u04ff\7\u0087\2\2\u04ff\u0501")
        buf.write("\3\2\2\2\u0500\u04f3\3\2\2\2\u0500\u04f7\3\2\2\2\u0500")
        buf.write("\u04fb\3\2\2\2\u0501k\3\2\2\2\u0502\u0504\5\u01d2\u00ea")
        buf.write("\2\u0503\u0502\3\2\2\2\u0504\u0505\3\2\2\2\u0505\u0503")
        buf.write("\3\2\2\2\u0505\u0506\3\2\2\2\u0506m\3\2\2\2\u0507\u050c")
        buf.write("\5\u01cc\u00e7\2\u0508\u0509\7h\2\2\u0509\u050b\5\u01cc")
        buf.write("\u00e7\2\u050a\u0508\3\2\2\2\u050b\u050e\3\2\2\2\u050c")
        buf.write("\u050a\3\2\2\2\u050c\u050d\3\2\2\2\u050do\3\2\2\2\u050e")
        buf.write("\u050c\3\2\2\2\u050f\u0510\7\35\2\2\u0510\u0512\5\u01e8")
        buf.write("\u00f5\2\u0511\u0513\5\u0084C\2\u0512\u0511\3\2\2\2\u0512")
        buf.write("\u0513\3\2\2\2\u0513\u0514\3\2\2\2\u0514\u0515\5\u01ea")
        buf.write("\u00f6\2\u0515q\3\2\2\2\u0516\u0517\7\61\2\2\u0517\u0518")
        buf.write("\5\u0198\u00cd\2\u0518\u0519\7M\2\2\u0519\u051a\5\u00b6")
        buf.write("\\\2\u051as\3\2\2\2\u051b\u0523\5N(\2\u051c\u0523\5\u0114")
        buf.write("\u008b\2\u051d\u051e\7\n\2\2\u051e\u051f\5\u0128\u0095")
        buf.write("\2\u051f\u0520\7M\2\2\u0520\u0521\5\u00b6\\\2\u0521\u0523")
        buf.write("\3\2\2\2\u0522\u051b\3\2\2\2\u0522\u051c\3\2\2\2\u0522")
        buf.write("\u051d\3\2\2\2\u0523u\3\2\2\2\u0524\u052e\5t;\2\u0525")
        buf.write("\u0527\5\u01ec\u00f7\2\u0526\u0525\3\2\2\2\u0527\u0528")
        buf.write("\3\2\2\2\u0528\u0526\3\2\2\2\u0528\u0529\3\2\2\2\u0529")
        buf.write("\u052a\3\2\2\2\u052a\u052b\5t;\2\u052b\u052d\3\2\2\2\u052c")
        buf.write("\u0526\3\2\2\2\u052d\u0530\3\2\2\2\u052e\u052c\3\2\2\2")
        buf.write("\u052e\u052f\3\2\2\2\u052f\u0534\3\2\2\2\u0530\u052e\3")
        buf.write("\2\2\2\u0531\u0533\5\u01ec\u00f7\2\u0532\u0531\3\2\2\2")
        buf.write("\u0533\u0536\3\2\2\2\u0534\u0532\3\2\2\2\u0534\u0535\3")
        buf.write("\2\2\2\u0535w\3\2\2\2\u0536\u0534\3\2\2\2\u0537\u0539")
        buf.write("\5\u01e8\u00f5\2\u0538\u053a\5v<\2\u0539\u0538\3\2\2\2")
        buf.write("\u0539\u053a\3\2\2\2\u053a\u053b\3\2\2\2\u053b\u053c\5")
        buf.write("\u01ea\u00f6\2\u053cy\3\2\2\2\u053d\u053e\7\35\2\2\u053e")
        buf.write("\u053f\5x=\2\u053f{\3\2\2\2\u0540\u0543\5P)\2\u0541\u0543")
        buf.write("\5\u0114\u008b\2\u0542\u0540\3\2\2\2\u0542\u0541\3\2\2")
        buf.write("\2\u0543}\3\2\2\2\u0544\u054e\5|?\2\u0545\u0547\5\u01ec")
        buf.write("\u00f7\2\u0546\u0545\3\2\2\2\u0547\u0548\3\2\2\2\u0548")
        buf.write("\u0546\3\2\2\2\u0548\u0549\3\2\2\2\u0549\u054a\3\2\2\2")
        buf.write("\u054a\u054b\5|?\2\u054b\u054d\3\2\2\2\u054c\u0546\3\2")
        buf.write("\2\2\u054d\u0550\3\2\2\2\u054e\u054c\3\2\2\2\u054e\u054f")
        buf.write("\3\2\2\2\u054f\u0554\3\2\2\2\u0550\u054e\3\2\2\2\u0551")
        buf.write("\u0553\5\u01ec\u00f7\2\u0552\u0551\3\2\2\2\u0553\u0556")
        buf.write("\3\2\2\2\u0554\u0552\3\2\2\2\u0554\u0555\3\2\2\2\u0555")
        buf.write("\177\3\2\2\2\u0556\u0554\3\2\2\2\u0557\u0559\5\u01e8\u00f5")
        buf.write("\2\u0558\u055a\5~@\2\u0559\u0558\3\2\2\2\u0559\u055a\3")
        buf.write("\2\2\2\u055a\u055b\3\2\2\2\u055b\u055c\5\u01ea\u00f6\2")
        buf.write("\u055c\u0081\3\2\2\2\u055d\u055e\7\35\2\2\u055e\u055f")
        buf.write("\5\u0080A\2\u055f\u0083\3\2\2\2\u0560\u056a\5\u0114\u008b")
        buf.write("\2\u0561\u0563\5\u01ec\u00f7\2\u0562\u0561\3\2\2\2\u0563")
        buf.write("\u0564\3\2\2\2\u0564\u0562\3\2\2\2\u0564\u0565\3\2\2\2")
        buf.write("\u0565\u0566\3\2\2\2\u0566\u0567\5\u0114\u008b\2\u0567")
        buf.write("\u0569\3\2\2\2\u0568\u0562\3\2\2\2\u0569\u056c\3\2\2\2")
        buf.write("\u056a\u0568\3\2\2\2\u056a\u056b\3\2\2\2\u056b\u0570\3")
        buf.write("\2\2\2\u056c\u056a\3\2\2\2\u056d\u056f\5\u01ec\u00f7\2")
        buf.write("\u056e\u056d\3\2\2\2\u056f\u0572\3\2\2\2\u0570\u056e\3")
        buf.write("\2\2\2\u0570\u0571\3\2\2\2\u0571\u0085\3\2\2\2\u0572\u0570")
        buf.write("\3\2\2\2\u0573\u0575\5\u01e8\u00f5\2\u0574\u0576\5\u0084")
        buf.write("C\2\u0575\u0574\3\2\2\2\u0575\u0576\3\2\2\2\u0576\u0577")
        buf.write("\3\2\2\2\u0577\u0578\5\u01ea\u00f6\2\u0578\u0087\3\2\2")
        buf.write("\2\u0579\u0581\5\u0086D\2\u057a\u057c\5\u01e8\u00f5\2")
        buf.write("\u057b\u057d\5\u0180\u00c1\2\u057c\u057b\3\2\2\2\u057c")
        buf.write("\u057d\3\2\2\2\u057d\u057e\3\2\2\2\u057e\u057f\5\u01ea")
        buf.write("\u00f6\2\u057f\u0581\3\2\2\2\u0580\u0579\3\2\2\2\u0580")
        buf.write("\u057a\3\2\2\2\u0581\u0089\3\2\2\2\u0582\u0583\7\35\2")
        buf.write("\2\u0583\u0584\5\u0088E\2\u0584\u008b\3\2\2\2\u0585\u058b")
        buf.write("\5\u008eH\2\u0586\u0587\5\u01ec\u00f7\2\u0587\u0588\5")
        buf.write("\u008eH\2\u0588\u058a\3\2\2\2\u0589\u0586\3\2\2\2\u058a")
        buf.write("\u058d\3\2\2\2\u058b\u0589\3\2\2\2\u058b\u058c\3\2\2\2")
        buf.write("\u058c\u058f\3\2\2\2\u058d\u058b\3\2\2\2\u058e\u0590\5")
        buf.write("\u01ec\u00f7\2\u058f\u058e\3\2\2\2\u058f\u0590\3\2\2\2")
        buf.write("\u0590\u008d\3\2\2\2\u0591\u0593\5\u0200\u0101\2\u0592")
        buf.write("\u0594\5\u0092J\2\u0593\u0592\3\2\2\2\u0593\u0594\3\2")
        buf.write("\2\2\u0594\u0596\3\2\2\2\u0595\u0597\5\u0094K\2\u0596")
        buf.write("\u0595\3\2\2\2\u0596\u0597\3\2\2\2\u0597\u0598\3\2\2\2")
        buf.write("\u0598\u0599\5\u0128\u0095\2\u0599\u059a\7j\2\2\u059a")
        buf.write("\u059b\5\u0126\u0094\2\u059b\u008f\3\2\2\2\u059c\u059f")
        buf.write("\7`\2\2\u059d\u059f\5\u01d8\u00ed\2\u059e\u059c\3\2\2")
        buf.write("\2\u059e\u059d\3\2\2\2\u059f\u0091\3\2\2\2\u05a0\u05a1")
        buf.write("\7|\2\2\u05a1\u05a2\5\u01fa\u00fe\2\u05a2\u05a3\7}\2\2")
        buf.write("\u05a3\u05ae\3\2\2\2\u05a4\u05a5\7|\2\2\u05a5\u05a6\5")
        buf.write("\u0090I\2\u05a6\u05a7\5\u01fa\u00fe\2\u05a7\u05a8\7}\2")
        buf.write("\2\u05a8\u05ae\3\2\2\2\u05a9\u05aa\7|\2\2\u05aa\u05ab")
        buf.write("\5\u0090I\2\u05ab\u05ac\7}\2\2\u05ac\u05ae\3\2\2\2\u05ad")
        buf.write("\u05a0\3\2\2\2\u05ad\u05a4\3\2\2\2\u05ad\u05a9\3\2\2\2")
        buf.write("\u05ae\u0093\3\2\2\2\u05af\u05b1\7\37\2\2\u05b0\u05b2")
        buf.write("\5\u0096L\2\u05b1\u05b0\3\2\2\2\u05b1\u05b2\3\2\2\2\u05b2")
        buf.write("\u05b3\3\2\2\2\u05b3\u05b9\7e\2\2\u05b4\u05b6\7\37\2\2")
        buf.write("\u05b5\u05b7\5\u0096L\2\u05b6\u05b5\3\2\2\2\u05b6\u05b7")
        buf.write("\3\2\2\2\u05b7\u05b8\3\2\2\2\u05b8\u05ba\7e\2\2\u05b9")
        buf.write("\u05b4\3\2\2\2\u05b9\u05ba\3\2\2\2\u05ba\u0095\3\2\2\2")
        buf.write("\u05bb\u05bd\5\u0098M\2\u05bc\u05bb\3\2\2\2\u05bd\u05be")
        buf.write("\3\2\2\2\u05be\u05bc\3\2\2\2\u05be\u05bf\3\2\2\2\u05bf")
        buf.write("\u0097\3\2\2\2\u05c0\u05c8\5\u01d2\u00ea\2\u05c1\u05c2")
        buf.write("\7z\2\2\u05c2\u05c3\5\u01d2\u00ea\2\u05c3\u05c4\7M\2\2")
        buf.write("\u05c4\u05c5\5\u00c4c\2\u05c5\u05c6\7{\2\2\u05c6\u05c8")
        buf.write("\3\2\2\2\u05c7\u05c0\3\2\2\2\u05c7\u05c1\3\2\2\2\u05c8")
        buf.write("\u0099\3\2\2\2\u05c9\u05cf\5\u009cO\2\u05ca\u05cb\5\u01ec")
        buf.write("\u00f7\2\u05cb\u05cc\5\u009cO\2\u05cc\u05ce\3\2\2\2\u05cd")
        buf.write("\u05ca\3\2\2\2\u05ce\u05d1\3\2\2\2\u05cf\u05cd\3\2\2\2")
        buf.write("\u05cf\u05d0\3\2\2\2\u05d0\u05d3\3\2\2\2\u05d1\u05cf\3")
        buf.write("\2\2\2\u05d2\u05d4\5\u01ec\u00f7\2\u05d3\u05d2\3\2\2\2")
        buf.write("\u05d3\u05d4\3\2\2\2\u05d4\u009b\3\2\2\2\u05d5\u05d6\5")
        buf.write("\u018c\u00c7\2\u05d6\u05d7\5\u00a2R\2\u05d7\u009d\3\2")
        buf.write("\2\2\u05d8\u05de\5\u00a0Q\2\u05d9\u05da\5\u01ec\u00f7")
        buf.write("\2\u05da\u05db\5\u00a0Q\2\u05db\u05dd\3\2\2\2\u05dc\u05d9")
        buf.write("\3\2\2\2\u05dd\u05e0\3\2\2\2\u05de\u05dc\3\2\2\2\u05de")
        buf.write("\u05df\3\2\2\2\u05df\u05e2\3\2\2\2\u05e0\u05de\3\2\2\2")
        buf.write("\u05e1\u05e3\5\u01ec\u00f7\2\u05e2\u05e1\3\2\2\2\u05e2")
        buf.write("\u05e3\3\2\2\2\u05e3\u009f\3\2\2\2\u05e4\u05e5\5\u018c")
        buf.write("\u00c7\2\u05e5\u05e6\5\u00a2R\2\u05e6\u00a1\3\2\2\2\u05e7")
        buf.write("\u05ee\5\u0200\u0101\2\u05e8\u05ea\7|\2\2\u05e9\u05eb")
        buf.write("\5\u00a4S\2\u05ea\u05e9\3\2\2\2\u05ea\u05eb\3\2\2\2\u05eb")
        buf.write("\u05ec\3\2\2\2\u05ec\u05ee\7}\2\2\u05ed\u05e7\3\2\2\2")
        buf.write("\u05ed\u05e8\3\2\2\2\u05ee\u00a3\3\2\2\2\u05ef\u05f4\5")
        buf.write("\u0200\u0101\2\u05f0\u05f1\7h\2\2\u05f1\u05f3\5\u0200")
        buf.write("\u0101\2\u05f2\u05f0\3\2\2\2\u05f3\u05f6\3\2\2\2\u05f4")
        buf.write("\u05f2\3\2\2\2\u05f4\u05f5\3\2\2\2\u05f5\u00a5\3\2\2\2")
        buf.write("\u05f6\u05f4\3\2\2\2\u05f7\u05f8\7\u0082\2\2\u05f8\u05f9")
        buf.write("\7C\2\2\u05f9\u05fa\5\u018e\u00c8\2\u05fa\u05fb\5\u0130")
        buf.write("\u0099\2\u05fb\u05fc\7\u0083\2\2\u05fc\u060a\3\2\2\2\u05fd")
        buf.write("\u05fe\7\u0082\2\2\u05fe\u05ff\7C\2\2\u05ff\u0600\5\u01ae")
        buf.write("\u00d8\2\u0600\u0601\5\u0130\u0099\2\u0601\u0602\7\u0083")
        buf.write("\2\2\u0602\u060a\3\2\2\2\u0603\u0604\7\u0082\2\2\u0604")
        buf.write("\u0605\7C\2\2\u0605\u0606\7\27\2\2\u0606\u0607\5\u0130")
        buf.write("\u0099\2\u0607\u0608\7\u0083\2\2\u0608\u060a\3\2\2\2\u0609")
        buf.write("\u05f7\3\2\2\2\u0609\u05fd\3\2\2\2\u0609\u0603\3\2\2\2")
        buf.write("\u060a\u00a7\3\2\2\2\u060b\u060c\7\20\2\2\u060c\u060e")
        buf.write("\5\u00aaV\2\u060d\u060f\5\u00acW\2\u060e\u060d\3\2\2\2")
        buf.write("\u060e\u060f\3\2\2\2\u060f\u0610\3\2\2\2\u0610\u0611\5")
        buf.write("\u00aeX\2\u0611\u0617\3\2\2\2\u0612\u0613\7!\2\2\u0613")
        buf.write("\u0614\5\u00aaV\2\u0614\u0615\5\u00aeX\2\u0615\u0617\3")
        buf.write("\2\2\2\u0616\u060b\3\2\2\2\u0616\u0612\3\2\2\2\u0617\u00a9")
        buf.write("\3\2\2\2\u0618\u0619\t\4\2\2\u0619\u00ab\3\2\2\2\u061a")
        buf.write("\u061b\t\5\2\2\u061b\u00ad\3\2\2\2\u061c\u061e\5\u0200")
        buf.write("\u0101\2\u061d\u061c\3\2\2\2\u061d\u061e\3\2\2\2\u061e")
        buf.write("\u061f\3\2\2\2\u061f\u0620\5\u01cc\u00e7\2\u0620\u0621")
        buf.write("\7M\2\2\u0621\u0622\5\u00b6\\\2\u0622\u00af\3\2\2\2\u0623")
        buf.write("\u0624\7M\2\2\u0624\u0625\5\u00b4[\2\u0625\u00b1\3\2\2")
        buf.write("\2\u0626\u0627\7M\2\2\u0627\u0628\5\u01a4\u00d3\2\u0628")
        buf.write("\u00b3\3\2\2\2\u0629\u062a\5\u00c4c\2\u062a\u00b5\3\2")
        buf.write("\2\2\u062b\u062c\5\u00c6d\2\u062c\u00b7\3\2\2\2\u062d")
        buf.write("\u0632\5\u01cc\u00e7\2\u062e\u062f\7h\2\2\u062f\u0631")
        buf.write("\5\u01cc\u00e7\2\u0630\u062e\3\2\2\2\u0631\u0634\3\2\2")
        buf.write("\2\u0632\u0630\3\2\2\2\u0632\u0633\3\2\2\2\u0633\u00b9")
        buf.write("\3\2\2\2\u0634\u0632\3\2\2\2\u0635\u063a\5\u00b4[\2\u0636")
        buf.write("\u0637\7h\2\2\u0637\u0639\5\u00b4[\2\u0638\u0636\3\2\2")
        buf.write("\2\u0639\u063c\3\2\2\2\u063a\u0638\3\2\2\2\u063a\u063b")
        buf.write("\3\2\2\2\u063b\u00bb\3\2\2\2\u063c\u063a\3\2\2\2\u063d")
        buf.write("\u063e\7\u0082\2\2\u063e\u063f\7A\2\2\u063f\u0644\7\u0083")
        buf.write("\2\2\u0640\u0641\7\u0082\2\2\u0641\u0642\7B\2\2\u0642")
        buf.write("\u0644\7\u0083\2\2\u0643\u063d\3\2\2\2\u0643\u0640\3\2")
        buf.write("\2\2\u0644\u00bd\3\2\2\2\u0645\u0646\t\6\2\2\u0646\u00bf")
        buf.write("\3\2\2\2\u0647\u064d\5\u00c4c\2\u0648\u0649\5\u00c4c\2")
        buf.write("\u0649\u064a\7M\2\2\u064a\u064b\5\u00f4{\2\u064b\u064d")
        buf.write("\3\2\2\2\u064c\u0647\3\2\2\2\u064c\u0648\3\2\2\2\u064d")
        buf.write("\u00c1\3\2\2\2\u064e\u0654\5\u00c6d\2\u064f\u0650\5\u00c6")
        buf.write("d\2\u0650\u0651\7M\2\2\u0651\u0652\5\u00f4{\2\u0652\u0654")
        buf.write("\3\2\2\2\u0653\u064e\3\2\2\2\u0653\u064f\3\2\2\2\u0654")
        buf.write("\u00c3\3\2\2\2\u0655\u0657\7\37\2\2\u0656\u0658\5\u00e6")
        buf.write("t\2\u0657\u0656\3\2\2\2\u0657\u0658\3\2\2\2\u0658\u0659")
        buf.write("\3\2\2\2\u0659\u065a\5\u00be`\2\u065a\u065b\5\u00c4c\2")
        buf.write("\u065b\u0666\3\2\2\2\u065c\u065d\5\u00d6l\2\u065d\u065e")
        buf.write("\7L\2\2\u065e\u065f\5\u00c4c\2\u065f\u0666\3\2\2\2\u0660")
        buf.write("\u0661\5\u01cc\u00e7\2\u0661\u0662\7M\2\2\u0662\u0663")
        buf.write("\5\u00ccg\2\u0663\u0666\3\2\2\2\u0664\u0666\5\u00ccg\2")
        buf.write("\u0665\u0655\3\2\2\2\u0665\u065c\3\2\2\2\u0665\u0660\3")
        buf.write("\2\2\2\u0665\u0664\3\2\2\2\u0666\u00c5\3\2\2\2\u0667\u0669")
        buf.write("\7\37\2\2\u0668\u066a\5\u00e6t\2\u0669\u0668\3\2\2\2\u0669")
        buf.write("\u066a\3\2\2\2\u066a\u066b\3\2\2\2\u066b\u066c\5\u00be")
        buf.write("`\2\u066c\u066d\5\u00c6d\2\u066d\u0678\3\2\2\2\u066e\u066f")
        buf.write("\5\u00c8e\2\u066f\u0670\7L\2\2\u0670\u0671\5\u00c6d\2")
        buf.write("\u0671\u0678\3\2\2\2\u0672\u0673\5\u01cc\u00e7\2\u0673")
        buf.write("\u0674\7M\2\2\u0674\u0675\5\u00ccg\2\u0675\u0678\3\2\2")
        buf.write("\2\u0676\u0678\5\u00ceh\2\u0677\u0667\3\2\2\2\u0677\u066e")
        buf.write("\3\2\2\2\u0677\u0672\3\2\2\2\u0677\u0676\3\2\2\2\u0678")
        buf.write("\u00c7\3\2\2\2\u0679\u067a\5\u00d6l\2\u067a\u00c9\3\2")
        buf.write("\2\2\u067b\u067c\5\u00d0i\2\u067c\u00cb\3\2\2\2\u067d")
        buf.write("\u0683\5\u00d6l\2\u067e\u067f\5\u00d6l\2\u067f\u0680\7")
        buf.write("N\2\2\u0680\u0681\5\u00c4c\2\u0681\u0683\3\2\2\2\u0682")
        buf.write("\u067d\3\2\2\2\u0682\u067e\3\2\2\2\u0683\u00cd\3\2\2\2")
        buf.write("\u0684\u068a\5\u00d6l\2\u0685\u0686\5\u00d6l\2\u0686\u0687")
        buf.write("\7N\2\2\u0687\u0688\5\u00c6d\2\u0688\u068a\3\2\2\2\u0689")
        buf.write("\u0684\3\2\2\2\u0689\u0685\3\2\2\2\u068a\u00cf\3\2\2\2")
        buf.write("\u068b\u068c\5\u00d2j\2\u068c\u00d1\3\2\2\2\u068d\u068f")
        buf.write("\5\u00d4k\2\u068e\u068d\3\2\2\2\u068f\u0690\3\2\2\2\u0690")
        buf.write("\u068e\3\2\2\2\u0690\u0691\3\2\2\2\u0691\u00d3\3\2\2\2")
        buf.write("\u0692\u0693\5\u00dan\2\u0693\u00d5\3\2\2\2\u0694\u0695")
        buf.write("\5\u00d8m\2\u0695\u00d7\3\2\2\2\u0696\u0698\5\u00dan\2")
        buf.write("\u0697\u0696\3\2\2\2\u0698\u0699\3\2\2\2\u0699\u0697\3")
        buf.write("\2\2\2\u0699\u069a\3\2\2\2\u069a\u00d9\3\2\2\2\u069b\u06a6")
        buf.write("\5\u00dco\2\u069c\u069d\7a\2\2\u069d\u06a6\5\u00dco\2")
        buf.write("\u069e\u06a6\5\u01aa\u00d6\2\u069f\u06a6\5\u01c4\u00e3")
        buf.write("\2\u06a0\u06a1\7k\2\2\u06a1\u06a6\5\u01a0\u00d1\2\u06a2")
        buf.write("\u06a3\7k\2\2\u06a3\u06a6\5\u01b6\u00dc\2\u06a4\u06a6")
        buf.write("\5\u00bc_\2\u06a5\u069b\3\2\2\2\u06a5\u069c\3\2\2\2\u06a5")
        buf.write("\u069e\3\2\2\2\u06a5\u069f\3\2\2\2\u06a5\u06a0\3\2\2\2")
        buf.write("\u06a5\u06a2\3\2\2\2\u06a5\u06a4\3\2\2\2\u06a6\u00db\3")
        buf.write("\2\2\2\u06a7\u06ea\5\u01a6\u00d4\2\u06a8\u06ea\5\u01c2")
        buf.write("\u00e2\2\u06a9\u06ea\7]\2\2\u06aa\u06ab\7`\2\2\u06ab\u06ea")
        buf.write("\5\u00dco\2\u06ac\u06ad\7Y\2\2\u06ad\u06ea\5\u00dco\2")
        buf.write("\u06ae\u06b0\7\u0086\2\2\u06af\u06b1\5\u0108\u0085\2\u06b0")
        buf.write("\u06af\3\2\2\2\u06b0\u06b1\3\2\2\2\u06b1\u06b2\3\2\2\2")
        buf.write("\u06b2\u06ea\7\u0087\2\2\u06b3\u06b4\7z\2\2\u06b4\u06ea")
        buf.write("\7{\2\2\u06b5\u06b6\7z\2\2\u06b6\u06b7\5\u00c0a\2\u06b7")
        buf.write("\u06b8\7h\2\2\u06b8\u06b9\5\u00e2r\2\u06b9\u06ba\7{\2")
        buf.write("\2\u06ba\u06ea\3\2\2\2\u06bb\u06bc\7x\2\2\u06bc\u06ea")
        buf.write("\7y\2\2\u06bd\u06be\7x\2\2\u06be\u06bf\5\u00e2r\2\u06bf")
        buf.write("\u06c0\7y\2\2\u06c0\u06ea\3\2\2\2\u06c1\u06c2\7x\2\2\u06c2")
        buf.write("\u06c3\5\u00e4s\2\u06c3\u06c4\7y\2\2\u06c4\u06ea\3\2\2")
        buf.write("\2\u06c5\u06c6\7|\2\2\u06c6\u06c7\5\u00c0a\2\u06c7\u06c8")
        buf.write("\7}\2\2\u06c8\u06ea\3\2\2\2\u06c9\u06ca\7z\2\2\u06ca\u06cb")
        buf.write("\5\u00c0a\2\u06cb\u06cc\7{\2\2\u06cc\u06ea\3\2\2\2\u06cd")
        buf.write("\u06ea\5\u0124\u0093\2\u06ce\u06ea\5\u0138\u009d\2\u06cf")
        buf.write("\u06d0\7k\2\2\u06d0\u06ea\5\u0190\u00c9\2\u06d1\u06d2")
        buf.write("\7k\2\2\u06d2\u06d3\7z\2\2\u06d3\u06d4\5\u00c0a\2\u06d4")
        buf.write("\u06d5\7h\2\2\u06d5\u06d6\5\u00e2r\2\u06d6\u06d7\7{\2")
        buf.write("\2\u06d7\u06ea\3\2\2\2\u06d8\u06d9\7k\2\2\u06d9\u06db")
        buf.write("\7|\2\2\u06da\u06dc\5\u00e2r\2\u06db\u06da\3\2\2\2\u06db")
        buf.write("\u06dc\3\2\2\2\u06dc\u06dd\3\2\2\2\u06dd\u06ea\7}\2\2")
        buf.write("\u06de\u06df\7k\2\2\u06df\u06ea\5\u01cc\u00e7\2\u06e0")
        buf.write("\u06e1\7|\2\2\u06e1\u06e2\5\u00c0a\2\u06e2\u06e3\7h\2")
        buf.write("\2\u06e3\u06e4\5\u00e2r\2\u06e4\u06e5\7}\2\2\u06e5\u06ea")
        buf.write("\3\2\2\2\u06e6\u06ea\5\u01fa\u00fe\2\u06e7\u06ea\5\u0200")
        buf.write("\u0101\2\u06e8\u06ea\7\36\2\2\u06e9\u06a7\3\2\2\2\u06e9")
        buf.write("\u06a8\3\2\2\2\u06e9\u06a9\3\2\2\2\u06e9\u06aa\3\2\2\2")
        buf.write("\u06e9\u06ac\3\2\2\2\u06e9\u06ae\3\2\2\2\u06e9\u06b3\3")
        buf.write("\2\2\2\u06e9\u06b5\3\2\2\2\u06e9\u06bb\3\2\2\2\u06e9\u06bd")
        buf.write("\3\2\2\2\u06e9\u06c1\3\2\2\2\u06e9\u06c5\3\2\2\2\u06e9")
        buf.write("\u06c9\3\2\2\2\u06e9\u06cd\3\2\2\2\u06e9\u06ce\3\2\2\2")
        buf.write("\u06e9\u06cf\3\2\2\2\u06e9\u06d1\3\2\2\2\u06e9\u06d8\3")
        buf.write("\2\2\2\u06e9\u06de\3\2\2\2\u06e9\u06e0\3\2\2\2\u06e9\u06e6")
        buf.write("\3\2\2\2\u06e9\u06e7\3\2\2\2\u06e9\u06e8\3\2\2\2\u06ea")
        buf.write("\u00dd\3\2\2\2\u06eb\u06ec\5\u00b4[\2\u06ec\u00df\3\2")
        buf.write("\2\2\u06ed\u06f2\5\u00c2b\2\u06ee\u06ef\7h\2\2\u06ef\u06f1")
        buf.write("\5\u00c2b\2\u06f0\u06ee\3\2\2\2\u06f1\u06f4\3\2\2\2\u06f2")
        buf.write("\u06f0\3\2\2\2\u06f2\u06f3\3\2\2\2\u06f3\u00e1\3\2\2\2")
        buf.write("\u06f4\u06f2\3\2\2\2\u06f5\u06fa\5\u00c0a\2\u06f6\u06f7")
        buf.write("\7h\2\2\u06f7\u06f9\5\u00c0a\2\u06f8\u06f6\3\2\2\2\u06f9")
        buf.write("\u06fc\3\2\2\2\u06fa\u06f8\3\2\2\2\u06fa\u06fb\3\2\2\2")
        buf.write("\u06fb\u00e3\3\2\2\2\u06fc\u06fa\3\2\2\2\u06fd\u06fe\5")
        buf.write("\u00c0a\2\u06fe\u06ff\7X\2\2\u06ff\u0704\5\u00c0a\2\u0700")
        buf.write("\u0701\7X\2\2\u0701\u0703\5\u00c0a\2\u0702\u0700\3\2\2")
        buf.write("\2\u0703\u0706\3\2\2\2\u0704\u0702\3\2\2\2\u0704\u0705")
        buf.write("\3\2\2\2\u0705\u00e5\3\2\2\2\u0706\u0704\3\2\2\2\u0707")
        buf.write("\u0709\5\u00e8u\2\u0708\u0707\3\2\2\2\u0709\u070a\3\2")
        buf.write("\2\2\u070a\u0708\3\2\2\2\u070a\u070b\3\2\2\2\u070b\u00e7")
        buf.write("\3\2\2\2\u070c\u0718\5\u00eav\2\u070d\u070e\7\u0086\2")
        buf.write("\2\u070e\u070f\5\u01c2\u00e2\2\u070f\u0710\7\u0087\2\2")
        buf.write("\u0710\u0718\3\2\2\2\u0711\u0712\7\u0086\2\2\u0712\u0713")
        buf.write("\5\u01c2\u00e2\2\u0713\u0714\7M\2\2\u0714\u0715\5\u00f4")
        buf.write("{\2\u0715\u0716\7\u0087\2\2\u0716\u0718\3\2\2\2\u0717")
        buf.write("\u070c\3\2\2\2\u0717\u070d\3\2\2\2\u0717\u0711\3\2\2\2")
        buf.write("\u0718\u00e9\3\2\2\2\u0719\u0721\5\u01c2\u00e2\2\u071a")
        buf.write("\u071b\7z\2\2\u071b\u071c\5\u01c2\u00e2\2\u071c\u071d")
        buf.write("\7M\2\2\u071d\u071e\5\u00f4{\2\u071e\u071f\7{\2\2\u071f")
        buf.write("\u0721\3\2\2\2\u0720\u0719\3\2\2\2\u0720\u071a\3\2\2\2")
        buf.write("\u0721\u00eb\3\2\2\2\u0722\u0723\7X\2\2\u0723\u0724\5")
        buf.write("\u00eex\2\u0724\u00ed\3\2\2\2\u0725\u072a\5\u00f0y\2\u0726")
        buf.write("\u0727\7h\2\2\u0727\u0729\5\u00f0y\2\u0728\u0726\3\2\2")
        buf.write("\2\u0729\u072c\3\2\2\2\u072a\u0728\3\2\2\2\u072a\u072b")
        buf.write("\3\2\2\2\u072b\u00ef\3\2\2\2\u072c\u072a\3\2\2\2\u072d")
        buf.write("\u072f\5\u00f2z\2\u072e\u072d\3\2\2\2\u072e\u072f\3\2")
        buf.write("\2\2\u072f\u0730\3\2\2\2\u0730\u0732\7N\2\2\u0731\u0733")
        buf.write("\5\u00f2z\2\u0732\u0731\3\2\2\2\u0732\u0733\3\2\2\2\u0733")
        buf.write("\u00f1\3\2\2\2\u0734\u0736\5\u01c2\u00e2\2\u0735\u0734")
        buf.write("\3\2\2\2\u0736\u0737\3\2\2\2\u0737\u0735\3\2\2\2\u0737")
        buf.write("\u0738\3\2\2\2\u0738\u00f3\3\2\2\2\u0739\u073a\5\u00c4")
        buf.write("c\2\u073a\u00f5\3\2\2\2\u073b\u073c\7\35\2\2\u073c\u073e")
        buf.write("\5\u01e8\u00f5\2\u073d\u073f\5\u00f8}\2\u073e\u073d\3")
        buf.write("\2\2\2\u073e\u073f\3\2\2\2\u073f\u0743\3\2\2\2\u0740\u0742")
        buf.write("\5\u01ec\u00f7\2\u0741\u0740\3\2\2\2\u0742\u0745\3\2\2")
        buf.write("\2\u0743\u0741\3\2\2\2\u0743\u0744\3\2\2\2\u0744\u0746")
        buf.write("\3\2\2\2\u0745\u0743\3\2\2\2\u0746\u0747\5\u01ea\u00f6")
        buf.write("\2\u0747\u00f7\3\2\2\2\u0748\u074e\5\u00fa~\2\u0749\u074a")
        buf.write("\5\u01ec\u00f7\2\u074a\u074b\5\u00fa~\2\u074b\u074d\3")
        buf.write("\2\2\2\u074c\u0749\3\2\2\2\u074d\u0750\3\2\2\2\u074e\u074c")
        buf.write("\3\2\2\2\u074e\u074f\3\2\2\2\u074f\u00f9\3\2\2\2\u0750")
        buf.write("\u074e\3\2\2\2\u0751\u0752\5\u00fc\177\2\u0752\u00fb\3")
        buf.write("\2\2\2\u0753\u0754\5\u0198\u00cd\2\u0754\u0755\7M\2\2")
        buf.write("\u0755\u0756\5\u00b6\\\2\u0756\u00fd\3\2\2\2\u0757\u0758")
        buf.write("\7j\2\2\u0758\u0759\5\u0100\u0081\2\u0759\u00ff\3\2\2")
        buf.write("\2\u075a\u075f\5\u0102\u0082\2\u075b\u075c\7X\2\2\u075c")
        buf.write("\u075e\5\u0102\u0082\2\u075d\u075b\3\2\2\2\u075e\u0761")
        buf.write("\3\2\2\2\u075f\u075d\3\2\2\2\u075f\u0760\3\2\2\2\u0760")
        buf.write("\u0101\3\2\2\2\u0761\u075f\3\2\2\2\u0762\u0764\5\u0104")
        buf.write("\u0083\2\u0763\u0762\3\2\2\2\u0763\u0764\3\2\2\2\u0764")
        buf.write("\u0768\3\2\2\2\u0765\u0766\5\u00caf\2\u0766\u0767\7L\2")
        buf.write("\2\u0767\u0769\3\2\2\2\u0768\u0765\3\2\2\2\u0768\u0769")
        buf.write("\3\2\2\2\u0769\u076a\3\2\2\2\u076a\u076b\5\u0106\u0084")
        buf.write("\2\u076b\u0103\3\2\2\2\u076c\u076e\7\37\2\2\u076d\u076f")
        buf.write("\5\u00e6t\2\u076e\u076d\3\2\2\2\u076e\u076f\3\2\2\2\u076f")
        buf.write("\u0770\3\2\2\2\u0770\u0771\7e\2\2\u0771\u0105\3\2\2\2")
        buf.write("\u0772\u0773\5\u00d2j\2\u0773\u0107\3\2\2\2\u0774\u0779")
        buf.write("\5\u010a\u0086\2\u0775\u0776\7h\2\2\u0776\u0778\5\u010a")
        buf.write("\u0086\2\u0777\u0775\3\2\2\2\u0778\u077b\3\2\2\2\u0779")
        buf.write("\u0777\3\2\2\2\u0779\u077a\3\2\2\2\u077a\u0109\3\2\2\2")
        buf.write("\u077b\u0779\3\2\2\2\u077c\u077d\5\u00b8]\2\u077d\u077e")
        buf.write("\7M\2\2\u077e\u077f\5\u00c4c\2\u077f\u010b\3\2\2\2\u0780")
        buf.write("\u0782\5\u010e\u0088\2\u0781\u0780\3\2\2\2\u0782\u0783")
        buf.write("\3\2\2\2\u0783\u0781\3\2\2\2\u0783\u0784\3\2\2\2\u0784")
        buf.write("\u010d\3\2\2\2\u0785\u0786\7\13\2\2\u0786\u0790\5\u0110")
        buf.write("\u0089\2\u0787\u0788\7\13\2\2\u0788\u0789\5:\36\2\u0789")
        buf.write("\u078a\5\u0110\u0089\2\u078a\u0790\3\2\2\2\u078b\u078c")
        buf.write("\7\13\2\2\u078c\u078d\5\u0110\u0089\2\u078d\u078e\5<\37")
        buf.write("\2\u078e\u0790\3\2\2\2\u078f\u0785\3\2\2\2\u078f\u0787")
        buf.write("\3\2\2\2\u078f\u078b\3\2\2\2\u0790\u010f\3\2\2\2\u0791")
        buf.write("\u0799\5\u01ac\u00d7\2\u0792\u0793\7z\2\2\u0793\u0799")
        buf.write("\7{\2\2\u0794\u0795\7z\2\2\u0795\u0796\5\u00e0q\2\u0796")
        buf.write("\u0797\7{\2\2\u0797\u0799\3\2\2\2\u0798\u0791\3\2\2\2")
        buf.write("\u0798\u0792\3\2\2\2\u0798\u0794\3\2\2\2\u0799\u0111\3")
        buf.write("\2\2\2\u079a\u07a8\5\u011c\u008f\2\u079b\u079d\5\u0128")
        buf.write("\u0095\2\u079c\u079e\5\u00b0Y\2\u079d\u079c\3\2\2\2\u079d")
        buf.write("\u079e\3\2\2\2\u079e\u079f\3\2\2\2\u079f\u07a0\5\u0116")
        buf.write("\u008c\2\u07a0\u07a8\3\2\2\2\u07a1\u07a8\5h\65\2\u07a2")
        buf.write("\u07a4\5\u01ec\u00f7\2\u07a3\u07a2\3\2\2\2\u07a4\u07a5")
        buf.write("\3\2\2\2\u07a5\u07a3\3\2\2\2\u07a5\u07a6\3\2\2\2\u07a6")
        buf.write("\u07a8\3\2\2\2\u07a7\u079a\3\2\2\2\u07a7\u079b\3\2\2\2")
        buf.write("\u07a7\u07a1\3\2\2\2\u07a7\u07a3\3\2\2\2\u07a8\u0113\3")
        buf.write("\2\2\2\u07a9\u07b1\5\u0112\u008a\2\u07aa\u07b1\5\u0136")
        buf.write("\u009c\2\u07ab\u07ad\5\u01ec\u00f7\2\u07ac\u07ab\3\2\2")
        buf.write("\2\u07ad\u07ae\3\2\2\2\u07ae\u07ac\3\2\2\2\u07ae\u07af")
        buf.write("\3\2\2\2\u07af\u07b1\3\2\2\2\u07b0\u07a9\3\2\2\2\u07b0")
        buf.write("\u07aa\3\2\2\2\u07b0\u07ac\3\2\2\2\u07b1\u0115\3\2\2\2")
        buf.write("\u07b2\u07b3\7j\2\2\u07b3\u07b5\5\u0126\u0094\2\u07b4")
        buf.write("\u07b6\5\u008aF\2\u07b5\u07b4\3\2\2\2\u07b5\u07b6\3\2")
        buf.write("\2\2\u07b6\u07bc\3\2\2\2\u07b7\u07b9\5\u0118\u008d\2\u07b8")
        buf.write("\u07ba\5\u008aF\2\u07b9\u07b8\3\2\2\2\u07b9\u07ba\3\2")
        buf.write("\2\2\u07ba\u07bc\3\2\2\2\u07bb\u07b2\3\2\2\2\u07bb\u07b7")
        buf.write("\3\2\2\2\u07bc\u0117\3\2\2\2\u07bd\u07bf\5\u011a\u008e")
        buf.write("\2\u07be\u07bd\3\2\2\2\u07bf\u07c0\3\2\2\2\u07c0\u07be")
        buf.write("\3\2\2\2\u07c0\u07c1\3\2\2\2\u07c1\u0119\3\2\2\2\u07c2")
        buf.write("\u07c3\7X\2\2\u07c3\u07c4\5\u0158\u00ad\2\u07c4\u07c5")
        buf.write("\7j\2\2\u07c5\u07c6\5\u0126\u0094\2\u07c6\u011b\3\2\2")
        buf.write("\2\u07c7\u07c8\5\u0128\u0095\2\u07c8\u07c9\7M\2\2\u07c9")
        buf.write("\u07ca\5\u00b6\\\2\u07ca\u0817\3\2\2\2\u07cb\u07cc\5\u01cc")
        buf.write("\u00e7\2\u07cc\u07cd\7h\2\2\u07cd\u07ce\5\u00b8]\2\u07ce")
        buf.write("\u07cf\7M\2\2\u07cf\u07d0\5\u00b6\\\2\u07d0\u0817\3\2")
        buf.write("\2\2\u07d1\u07d3\5&\24\2\u07d2\u07d4\5\u01fa\u00fe\2\u07d3")
        buf.write("\u07d2\3\2\2\2\u07d3\u07d4\3\2\2\2\u07d4\u07d5\3\2\2\2")
        buf.write("\u07d5\u07d6\5(\25\2\u07d6\u0817\3\2\2\2\u07d7\u0817\5")
        buf.write("r:\2\u07d8\u07d9\7\u0082\2\2\u07d9\u07da\7J\2\2\u07da")
        buf.write("\u07dc\5\u0198\u00cd\2\u07db\u07dd\5\u00b2Z\2\u07dc\u07db")
        buf.write("\3\2\2\2\u07dc\u07dd\3\2\2\2\u07dd\u07de\3\2\2\2\u07de")
        buf.write("\u07df\7\u0083\2\2\u07df\u0817\3\2\2\2\u07e0\u07e1\7\u0082")
        buf.write("\2\2\u07e1\u07e3\78\2\2\u07e2\u07e4\5\u011e\u0090\2\u07e3")
        buf.write("\u07e2\3\2\2\2\u07e3\u07e4\3\2\2\2\u07e4\u07e5\3\2\2\2")
        buf.write("\u07e5\u07e6\5\u01ce\u00e8\2\u07e6\u07e7\7\u0083\2\2\u07e7")
        buf.write("\u0817\3\2\2\2\u07e8\u07e9\7\u0082\2\2\u07e9\u07ea\7>")
        buf.write("\2\2\u07ea\u07ec\5\u01ce\u00e8\2\u07eb\u07ed\5\u0200\u0101")
        buf.write("\2\u07ec\u07eb\3\2\2\2\u07ec\u07ed\3\2\2\2\u07ed\u07ee")
        buf.write("\3\2\2\2\u07ee\u07ef\7\u0083\2\2\u07ef\u0817\3\2\2\2\u07f0")
        buf.write("\u07f1\7\u0082\2\2\u07f1\u07f3\7:\2\2\u07f2\u07f4\5\u011e")
        buf.write("\u0090\2\u07f3\u07f2\3\2\2\2\u07f3\u07f4\3\2\2\2\u07f4")
        buf.write("\u07f5\3\2\2\2\u07f5\u07f6\5\u01ce\u00e8\2\u07f6\u07f7")
        buf.write("\7M\2\2\u07f7\u07f8\5\u00ba^\2\u07f8\u07f9\7\u0083\2\2")
        buf.write("\u07f9\u0817\3\2\2\2\u07fa\u07fb\7\u0082\2\2\u07fb\u07fd")
        buf.write("\7;\2\2\u07fc\u07fe\5\u011e\u0090\2\u07fd\u07fc\3\2\2")
        buf.write("\2\u07fd\u07fe\3\2\2\2\u07fe\u07ff\3\2\2\2\u07ff\u0800")
        buf.write("\5\u01ce\u00e8\2\u0800\u0801\7M\2\2\u0801\u0802\5\u00ba")
        buf.write("^\2\u0802\u0803\7\u0083\2\2\u0803\u0817\3\2\2\2\u0804")
        buf.write("\u0805\7\u0082\2\2\u0805\u0806\7:\2\2\u0806\u0807\7\25")
        buf.write("\2\2\u0807\u0808\5\u00dep\2\u0808\u0809\7\u0083\2\2\u0809")
        buf.write("\u0817\3\2\2\2\u080a\u080b\7\u0082\2\2\u080b\u080c\7D")
        buf.write("\2\2\u080c\u080e\7\u0083\2\2\u080d\u080f\5\u0184\u00c3")
        buf.write("\2\u080e\u080d\3\2\2\2\u080e\u080f\3\2\2\2\u080f\u0810")
        buf.write("\3\2\2\2\u0810\u0817\7\u0083\2\2\u0811\u0813\5\u01ec\u00f7")
        buf.write("\2\u0812\u0811\3\2\2\2\u0813\u0814\3\2\2\2\u0814\u0812")
        buf.write("\3\2\2\2\u0814\u0815\3\2\2\2\u0815\u0817\3\2\2\2\u0816")
        buf.write("\u07c7\3\2\2\2\u0816\u07cb\3\2\2\2\u0816\u07d1\3\2\2\2")
        buf.write("\u0816\u07d7\3\2\2\2\u0816\u07d8\3\2\2\2\u0816\u07e0\3")
        buf.write("\2\2\2\u0816\u07e8\3\2\2\2\u0816\u07f0\3\2\2\2\u0816\u07fa")
        buf.write("\3\2\2\2\u0816\u0804\3\2\2\2\u0816\u080a\3\2\2\2\u0816")
        buf.write("\u0812\3\2\2\2\u0817\u011d\3\2\2\2\u0818\u0819\7|\2\2")
        buf.write("\u0819\u081a\5\u01fa\u00fe\2\u081a\u081b\7}\2\2\u081b")
        buf.write("\u0822\3\2\2\2\u081c\u081d\7|\2\2\u081d\u081e\5\u0090")
        buf.write("I\2\u081e\u081f\5\u01fa\u00fe\2\u081f\u0820\7}\2\2\u0820")
        buf.write("\u0822\3\2\2\2\u0821\u0818\3\2\2\2\u0821\u081c\3\2\2\2")
        buf.write("\u0822\u011f\3\2\2\2\u0823\u0824\7|\2\2\u0824\u0825\5")
        buf.write("\u01d2\u00ea\2\u0825\u0826\7X\2\2\u0826\u0121\3\2\2\2")
        buf.write("\u0827\u0828\7|\2\2\u0828\u0829\5\u01d0\u00e9\2\u0829")
        buf.write("\u082a\7X\2\2\u082a\u0123\3\2\2\2\u082b\u082e\5\u0120")
        buf.write("\u0091\2\u082c\u082e\5\u0122\u0092\2\u082d\u082b\3\2\2")
        buf.write("\2\u082d\u082c\3\2\2\2\u082e\u0125\3\2\2\2\u082f\u0830")
        buf.write("\5\u0128\u0095\2\u0830\u0831\7M\2\2\u0831\u0832\5\u00b4")
        buf.write("[\2\u0832\u0845\3\2\2\2\u0833\u0834\5\u0128\u0095\2\u0834")
        buf.write("\u0835\7P\2\2\u0835\u0836\5\u0126\u0094\2\u0836\u0845")
        buf.write("\3\2\2\2\u0837\u0838\5\u0128\u0095\2\u0838\u0839\7Q\2")
        buf.write("\2\u0839\u083a\5\u0126\u0094\2\u083a\u0845\3\2\2\2\u083b")
        buf.write("\u083c\5\u0128\u0095\2\u083c\u083d\7R\2\2\u083d\u083e")
        buf.write("\5\u0126\u0094\2\u083e\u0845\3\2\2\2\u083f\u0840\5\u0128")
        buf.write("\u0095\2\u0840\u0841\7S\2\2\u0841\u0842\5\u0126\u0094")
        buf.write("\2\u0842\u0845\3\2\2\2\u0843\u0845\5\u0128\u0095\2\u0844")
        buf.write("\u082f\3\2\2\2\u0844\u0833\3\2\2\2\u0844\u0837\3\2\2\2")
        buf.write("\u0844\u083b\3\2\2\2\u0844\u083f\3\2\2\2\u0844\u0843\3")
        buf.write("\2\2\2\u0845\u0127\3\2\2\2\u0846\u084c\5\u012c\u0097\2")
        buf.write("\u0847\u0848\5\u01b8\u00dd\2\u0848\u0849\5\u012a\u0096")
        buf.write("\2\u0849\u084b\3\2\2\2\u084a\u0847\3\2\2\2\u084b\u084e")
        buf.write("\3\2\2\2\u084c\u084a\3\2\2\2\u084c\u084d\3\2\2\2\u084d")
        buf.write("\u0129\3\2\2\2\u084e\u084c\3\2\2\2\u084f\u0850\5\u012c")
        buf.write("\u0097\2\u0850\u012b\3\2\2\2\u0851\u0853\7\\\2\2\u0852")
        buf.write("\u0851\3\2\2\2\u0852\u0853\3\2\2\2\u0853\u0854\3\2\2\2")
        buf.write("\u0854\u0855\5\u012e\u0098\2\u0855\u012d\3\2\2\2\u0856")
        buf.write("\u0858\5\u0130\u0099\2\u0857\u0856\3\2\2\2\u0858\u0859")
        buf.write("\3\2\2\2\u0859\u0857\3\2\2\2\u0859\u085a\3\2\2\2\u085a")
        buf.write("\u085d\3\2\2\2\u085b\u085c\7a\2\2\u085c\u085e\5\u00dc")
        buf.write("o\2\u085d\u085b\3\2\2\2\u085d\u085e\3\2\2\2\u085e\u012f")
        buf.write("\3\2\2\2\u085f\u0860\5\u01ce\u00e8\2\u0860\u0861\7a\2")
        buf.write("\2\u0861\u0862\5\u0130\u0099\2\u0862\u088d\3\2\2\2\u0863")
        buf.write("\u0864\7`\2\2\u0864\u088d\5\u0130\u0099\2\u0865\u0866")
        buf.write("\7Y\2\2\u0866\u088d\5\u0130\u0099\2\u0867\u0868\7m\2\2")
        buf.write("\u0868\u0869\5\u0170\u00b9\2\u0869\u086a\7N\2\2\u086a")
        buf.write("\u086b\5\u0126\u0094\2\u086b\u088d\3\2\2\2\u086c\u086d")
        buf.write("\7\26\2\2\u086d\u086e\5\u0086D\2\u086e\u086f\7\21\2\2")
        buf.write("\u086f\u0870\5\u0126\u0094\2\u0870\u088d\3\2\2\2\u0871")
        buf.write("\u0872\7K\2\2\u0872\u088d\5\u015c\u00af\2\u0873\u0874")
        buf.write("\7\17\2\2\u0874\u0876\5\u0126\u0094\2\u0875\u0877\5\u01ec")
        buf.write("\u00f7\2\u0876\u0875\3\2\2\2\u0876\u0877\3\2\2\2\u0877")
        buf.write("\u0878\3\2\2\2\u0878\u0879\7\33\2\2\u0879\u087b\5\u0126")
        buf.write("\u0094\2\u087a\u087c\5\u01ec\u00f7\2\u087b\u087a\3\2\2")
        buf.write("\2\u087b\u087c\3\2\2\2\u087c\u087d\3\2\2\2\u087d\u087e")
        buf.write("\7\r\2\2\u087e\u087f\5\u0126\u0094\2\u087f\u088d\3\2\2")
        buf.write("\2\u0880\u0881\7\17\2\2\u0881\u088d\5\u0166\u00b4\2\u0882")
        buf.write("\u0883\7\7\2\2\u0883\u0884\5\u0126\u0094\2\u0884\u0885")
        buf.write("\7\31\2\2\u0885\u0886\5\u015c\u00af\2\u0886\u088d\3\2")
        buf.write("\2\2\u0887\u0888\7\f\2\2\u0888\u088d\5\u0174\u00bb\2\u0889")
        buf.write("\u088a\7%\2\2\u088a\u088d\5\u0174\u00bb\2\u088b\u088d")
        buf.write("\5\u0132\u009a\2\u088c\u085f\3\2\2\2\u088c\u0863\3\2\2")
        buf.write("\2\u088c\u0865\3\2\2\2\u088c\u0867\3\2\2\2\u088c\u086c")
        buf.write("\3\2\2\2\u088c\u0871\3\2\2\2\u088c\u0873\3\2\2\2\u088c")
        buf.write("\u0880\3\2\2\2\u088c\u0882\3\2\2\2\u088c\u0887\3\2\2\2")
        buf.write("\u088c\u0889\3\2\2\2\u088c\u088b\3\2\2\2\u088d\u0131\3")
        buf.write("\2\2\2\u088e\u0896\5\u0134\u009b\2\u088f\u0891\7\u0086")
        buf.write("\2\2\u0890\u0892\5\u017c\u00bf\2\u0891\u0890\3\2\2\2\u0891")
        buf.write("\u0892\3\2\2\2\u0892\u0893\3\2\2\2\u0893\u0895\7\u0087")
        buf.write("\2\2\u0894\u088f\3\2\2\2\u0895\u0898\3\2\2\2\u0896\u0894")
        buf.write("\3\2\2\2\u0896\u0897\3\2\2\2\u0897\u0133\3\2\2\2\u0898")
        buf.write("\u0896\3\2\2\2\u0899\u08dd\5\u01ce\u00e8\2\u089a\u08dd")
        buf.write("\5\u0192\u00ca\2\u089b\u08dd\5\u01d2\u00ea\2\u089c\u08dd")
        buf.write("\5\u01e6\u00f4\2\u089d\u08dd\5\u0200\u0101\2\u089e\u08dd")
        buf.write("\5\u01fa\u00fe\2\u089f\u08dd\5\u01fc\u00ff\2\u08a0\u08a1")
        buf.write("\7z\2\2\u08a1\u08a2\5\u0144\u00a3\2\u08a2\u08a3\7{\2\2")
        buf.write("\u08a3\u08dd\3\2\2\2\u08a4\u08a5\7z\2\2\u08a5\u08a6\5")
        buf.write("\u0146\u00a4\2\u08a6\u08a7\7{\2\2\u08a7\u08dd\3\2\2\2")
        buf.write("\u08a8\u08a9\7x\2\2\u08a9\u08aa\5\u0144\u00a3\2\u08aa")
        buf.write("\u08ab\7y\2\2\u08ab\u08dd\3\2\2\2\u08ac\u08ad\7x\2\2\u08ad")
        buf.write("\u08ae\5\u0146\u00a4\2\u08ae\u08af\7y\2\2\u08af\u08dd")
        buf.write("\3\2\2\2\u08b0\u08b1\7|\2\2\u08b1\u08b2\5\u014c\u00a7")
        buf.write("\2\u08b2\u08b3\7}\2\2\u08b3\u08dd\3\2\2\2\u08b4\u08dd")
        buf.write("\7\36\2\2\u08b5\u08dd\5\u0138\u009d\2\u08b6\u08dd\5\u013a")
        buf.write("\u009e\2\u08b7\u08b8\7k\2\2\u08b8\u08dd\5\u01ce\u00e8")
        buf.write("\2\u08b9\u08ba\7k\2\2\u08ba\u08dd\5\u0192\u00ca\2\u08bb")
        buf.write("\u08bc\7l\2\2\u08bc\u08dd\5\u01c2\u00e2\2\u08bd\u08be")
        buf.write("\7l\2\2\u08be\u08dd\5\u01a4\u00d3\2\u08bf\u08dd\7l\2\2")
        buf.write("\u08c0\u08c1\7s\2\2\u08c1\u08c2\5\u0126\u0094\2\u08c2")
        buf.write("\u08c3\7w\2\2\u08c3\u08dd\3\2\2\2\u08c4\u08c5\7q\2\2\u08c5")
        buf.write("\u08c6\5\u0126\u0094\2\u08c6\u08c7\7r\2\2\u08c7\u08dd")
        buf.write("\3\2\2\2\u08c8\u08c9\7u\2\2\u08c9\u08ca\5\u00c0a\2\u08ca")
        buf.write("\u08cb\7w\2\2\u08cb\u08dd\3\2\2\2\u08cc\u08cd\7t\2\2\u08cd")
        buf.write("\u08ce\5\u0128\u0095\2\u08ce\u08cf\7w\2\2\u08cf\u08dd")
        buf.write("\3\2\2\2\u08d0\u08d1\7v\2\2\u08d1\u08d2\5\u0140\u00a1")
        buf.write("\2\u08d2\u08d3\7w\2\2\u08d3\u08dd\3\2\2\2\u08d4\u08dd")
        buf.write("\5\u0124\u0093\2\u08d5\u08d6\7o\2\2\u08d6\u08d8\5\u0130")
        buf.write("\u0099\2\u08d7\u08d9\5\u013c\u009f\2\u08d8\u08d7\3\2\2")
        buf.write("\2\u08d8\u08d9\3\2\2\2\u08d9\u08da\3\2\2\2\u08da\u08db")
        buf.write("\7o\2\2\u08db\u08dd\3\2\2\2\u08dc\u0899\3\2\2\2\u08dc")
        buf.write("\u089a\3\2\2\2\u08dc\u089b\3\2\2\2\u08dc\u089c\3\2\2\2")
        buf.write("\u08dc\u089d\3\2\2\2\u08dc\u089e\3\2\2\2\u08dc\u089f\3")
        buf.write("\2\2\2\u08dc\u08a0\3\2\2\2\u08dc\u08a4\3\2\2\2\u08dc\u08a8")
        buf.write("\3\2\2\2\u08dc\u08ac\3\2\2\2\u08dc\u08b0\3\2\2\2\u08dc")
        buf.write("\u08b4\3\2\2\2\u08dc\u08b5\3\2\2\2\u08dc\u08b6\3\2\2\2")
        buf.write("\u08dc\u08b7\3\2\2\2\u08dc\u08b9\3\2\2\2\u08dc\u08bb\3")
        buf.write("\2\2\2\u08dc\u08bd\3\2\2\2\u08dc\u08bf\3\2\2\2\u08dc\u08c0")
        buf.write("\3\2\2\2\u08dc\u08c4\3\2\2\2\u08dc\u08c8\3\2\2\2\u08dc")
        buf.write("\u08cc\3\2\2\2\u08dc\u08d0\3\2\2\2\u08dc\u08d4\3\2\2\2")
        buf.write("\u08dc\u08d5\3\2\2\2\u08dd\u0135\3\2\2\2\u08de\u08e1\5")
        buf.write("\u013a\u009e\2\u08df\u08e1\5\u0138\u009d\2\u08e0\u08de")
        buf.write("\3\2\2\2\u08e0\u08df\3\2\2\2\u08e1\u0137\3\2\2\2\u08e2")
        buf.write("\u08e3\7c\2\2\u08e3\u08e4\5\u0130\u0099\2\u08e4\u0139")
        buf.write("\3\2\2\2\u08e5\u08e6\7b\2\2\u08e6\u08e7\5\u0130\u0099")
        buf.write("\2\u08e7\u013b\3\2\2\2\u08e8\u08ea\5\u013e\u00a0\2\u08e9")
        buf.write("\u08e8\3\2\2\2\u08ea\u08eb\3\2\2\2\u08eb\u08e9\3\2\2\2")
        buf.write("\u08eb\u08ec\3\2\2\2\u08ec\u013d\3\2\2\2\u08ed\u08ee\5")
        buf.write("\u0130\u0099\2\u08ee\u013f\3\2\2\2\u08ef\u08f1\5\u01e8")
        buf.write("\u00f5\2\u08f0\u08f2\5\u0142\u00a2\2\u08f1\u08f0\3\2\2")
        buf.write("\2\u08f1\u08f2\3\2\2\2\u08f2\u08f3\3\2\2\2\u08f3\u08f4")
        buf.write("\5\u01ea\u00f6\2\u08f4\u0141\3\2\2\2\u08f5\u08f9\5*\26")
        buf.write("\2\u08f6\u08f8\5\u01ec\u00f7\2\u08f7\u08f6\3\2\2\2\u08f8")
        buf.write("\u08fb\3\2\2\2\u08f9\u08f7\3\2\2\2\u08f9\u08fa\3\2\2\2")
        buf.write("\u08fa\u0143\3\2\2\2\u08fb\u08f9\3\2\2\2\u08fc\u0908\5")
        buf.write("\u0126\u0094\2\u08fd\u08fe\5\u0128\u0095\2\u08fe\u08ff")
        buf.write("\5\u01b8\u00dd\2\u08ff\u0908\3\2\2\2\u0900\u0901\5\u01ba")
        buf.write("\u00de\2\u0901\u0902\5\u0128\u0095\2\u0902\u0908\3\2\2")
        buf.write("\2\u0903\u0904\5\u0126\u0094\2\u0904\u0905\7N\2\2\u0905")
        buf.write("\u0906\5\u0144\u00a3\2\u0906\u0908\3\2\2\2\u0907\u08fc")
        buf.write("\3\2\2\2\u0907\u08fd\3\2\2\2\u0907\u0900\3\2\2\2\u0907")
        buf.write("\u0903\3\2\2\2\u0908\u0145\3\2\2\2\u0909\u090a\5\u0144")
        buf.write("\u00a3\2\u090a\u090b\5\u0148\u00a5\2\u090b\u0919\3\2\2")
        buf.write("\2\u090c\u090d\5\u0144\u00a3\2\u090d\u090e\5\u01f2\u00fa")
        buf.write("\2\u090e\u0919\3\2\2\2\u090f\u0911\5\u01f0\u00f9\2\u0910")
        buf.write("\u0912\5\u014a\u00a6\2\u0911\u0910\3\2\2\2\u0911\u0912")
        buf.write("\3\2\2\2\u0912\u0919\3\2\2\2\u0913\u0914\5\u01f2\u00fa")
        buf.write("\2\u0914\u0916\5\u0144\u00a3\2\u0915\u0917\5\u01f2\u00fa")
        buf.write("\2\u0916\u0915\3\2\2\2\u0916\u0917\3\2\2\2\u0917\u0919")
        buf.write("\3\2\2\2\u0918\u0909\3\2\2\2\u0918\u090c\3\2\2\2\u0918")
        buf.write("\u090f\3\2\2\2\u0918\u0913\3\2\2\2\u0919\u0147\3\2\2\2")
        buf.write("\u091a\u091c\5\u01f0\u00f9\2\u091b\u091d\5\u014a\u00a6")
        buf.write("\2\u091c\u091b\3\2\2\2\u091c\u091d\3\2\2\2\u091d\u0149")
        buf.write("\3\2\2\2\u091e\u091f\5\u0144\u00a3\2\u091f\u0920\5\u0148")
        buf.write("\u00a5\2\u0920\u0923\3\2\2\2\u0921\u0923\5\u0144\u00a3")
        buf.write("\2\u0922\u091e\3\2\2\2\u0922\u0921\3\2\2\2\u0923\u014b")
        buf.write("\3\2\2\2\u0924\u093d\5\u0144\u00a3\2\u0925\u093d\5\u014e")
        buf.write("\u00a8\2\u0926\u0927\5\u0144\u00a3\2\u0927\u0928\7d\2")
        buf.write("\2\u0928\u093d\3\2\2\2\u0929\u092a\5\u0144\u00a3\2\u092a")
        buf.write("\u092b\7h\2\2\u092b\u092c\5\u0126\u0094\2\u092c\u092d")
        buf.write("\7d\2\2\u092d\u093d\3\2\2\2\u092e\u092f\5\u0144\u00a3")
        buf.write("\2\u092f\u0930\7d\2\2\u0930\u0931\5\u0126\u0094\2\u0931")
        buf.write("\u093d\3\2\2\2\u0932\u0933\5\u0144\u00a3\2\u0933\u0934")
        buf.write("\7h\2\2\u0934\u0935\5\u0126\u0094\2\u0935\u0936\7d\2\2")
        buf.write("\u0936\u0937\5\u0126\u0094\2\u0937\u093d\3\2\2\2\u0938")
        buf.write("\u0939\5\u0144\u00a3\2\u0939\u093a\7X\2\2\u093a\u093b")
        buf.write("\5\u0150\u00a9\2\u093b\u093d\3\2\2\2\u093c\u0924\3\2\2")
        buf.write("\2\u093c\u0925\3\2\2\2\u093c\u0926\3\2\2\2\u093c\u0929")
        buf.write("\3\2\2\2\u093c\u092e\3\2\2\2\u093c\u0932\3\2\2\2\u093c")
        buf.write("\u0938\3\2\2\2\u093d\u014d\3\2\2\2\u093e\u093f\5\u0144")
        buf.write("\u00a3\2\u093f\u0940\7h\2\2\u0940\u0945\5\u0144\u00a3")
        buf.write("\2\u0941\u0942\7h\2\2\u0942\u0944\5\u0144\u00a3\2\u0943")
        buf.write("\u0941\3\2\2\2\u0944\u0947\3\2\2\2\u0945\u0943\3\2\2\2")
        buf.write("\u0945\u0946\3\2\2\2\u0946\u014f\3\2\2\2\u0947\u0945\3")
        buf.write("\2\2\2\u0948\u0949\5\u0152\u00aa\2\u0949\u0151\3\2\2\2")
        buf.write("\u094a\u094f\5\u0154\u00ab\2\u094b\u094c\7X\2\2\u094c")
        buf.write("\u094e\5\u0154\u00ab\2\u094d\u094b\3\2\2\2\u094e\u0951")
        buf.write("\3\2\2\2\u094f\u094d\3\2\2\2\u094f\u0950\3\2\2\2\u0950")
        buf.write("\u0153\3\2\2\2\u0951\u094f\3\2\2\2\u0952\u0957\5\u0156")
        buf.write("\u00ac\2\u0953\u0954\7h\2\2\u0954\u0956\5\u0156\u00ac")
        buf.write("\2\u0955\u0953\3\2\2\2\u0956\u0959\3\2\2\2\u0957\u0955")
        buf.write("\3\2\2\2\u0957\u0958\3\2\2\2\u0958\u0973\3\2\2\2\u0959")
        buf.write("\u0957\3\2\2\2\u095a\u095f\5\u0156\u00ac\2\u095b\u095c")
        buf.write("\7h\2\2\u095c\u095e\5\u017a\u00be\2\u095d\u095b\3\2\2")
        buf.write("\2\u095e\u0961\3\2\2\2\u095f\u095d\3\2\2\2\u095f\u0960")
        buf.write("\3\2\2\2\u0960\u0973\3\2\2\2\u0961\u095f\3\2\2\2\u0962")
        buf.write("\u0967\5\u017a\u00be\2\u0963\u0964\7h\2\2\u0964\u0966")
        buf.write("\5\u0156\u00ac\2\u0965\u0963\3\2\2\2\u0966\u0969\3\2\2")
        buf.write("\2\u0967\u0965\3\2\2\2\u0967\u0968\3\2\2\2\u0968\u0973")
        buf.write("\3\2\2\2\u0969\u0967\3\2\2\2\u096a\u096f\5\u017a\u00be")
        buf.write("\2\u096b\u096c\7h\2\2\u096c\u096e\5\u017a\u00be\2\u096d")
        buf.write("\u096b\3\2\2\2\u096e\u0971\3\2\2\2\u096f\u096d\3\2\2\2")
        buf.write("\u096f\u0970\3\2\2\2\u0970\u0973\3\2\2\2\u0971\u096f\3")
        buf.write("\2\2\2\u0972\u0952\3\2\2\2\u0972\u095a\3\2\2\2\u0972\u0962")
        buf.write("\3\2\2\2\u0972\u096a\3\2\2\2\u0973\u0155\3\2\2\2\u0974")
        buf.write("\u0975\7\33\2\2\u0975\u0987\5\u0126\u0094\2\u0976\u0977")
        buf.write("\7\33\2\2\u0977\u0978\5\u0126\u0094\2\u0978\u0979\7/\2")
        buf.write("\2\u0979\u097a\5\u0126\u0094\2\u097a\u0987\3\2\2\2\u097b")
        buf.write("\u097c\7\33\2\2\u097c\u097d\7.\2\2\u097d\u097e\7\60\2")
        buf.write("\2\u097e\u0987\5\u0126\u0094\2\u097f\u0980\7\33\2\2\u0980")
        buf.write("\u0981\7.\2\2\u0981\u0982\7/\2\2\u0982\u0983\5\u0126\u0094")
        buf.write("\2\u0983\u0984\7\60\2\2\u0984\u0985\5\u0126\u0094\2\u0985")
        buf.write("\u0987\3\2\2\2\u0986\u0974\3\2\2\2\u0986\u0976\3\2\2\2")
        buf.write("\u0986\u097b\3\2\2\2\u0986\u097f\3\2\2\2\u0987\u0157\3")
        buf.write("\2\2\2\u0988\u098d\5\u015a\u00ae\2\u0989\u098a\7h\2\2")
        buf.write("\u098a\u098c\5\u015a\u00ae\2\u098b\u0989\3\2\2\2\u098c")
        buf.write("\u098f\3\2\2\2\u098d\u098b\3\2\2\2\u098d\u098e\3\2\2\2")
        buf.write("\u098e\u0159\3\2\2\2\u098f\u098d\3\2\2\2\u0990\u0991\5")
        buf.write("\u016a\u00b6\2\u0991\u0992\7O\2\2\u0992\u0993\5\u0128")
        buf.write("\u0095\2\u0993\u0998\3\2\2\2\u0994\u0995\7\26\2\2\u0995")
        buf.write("\u0998\5\u0086D\2\u0996\u0998\5\u0128\u0095\2\u0997\u0990")
        buf.write("\3\2\2\2\u0997\u0994\3\2\2\2\u0997\u0996\3\2\2\2\u0998")
        buf.write("\u015b\3\2\2\2\u0999\u09a1\5\u01e8\u00f5\2\u099a\u099e")
        buf.write("\5\u015e\u00b0\2\u099b\u099d\5\u01ec\u00f7\2\u099c\u099b")
        buf.write("\3\2\2\2\u099d\u09a0\3\2\2\2\u099e\u099c\3\2\2\2\u099e")
        buf.write("\u099f\3\2\2\2\u099f\u09a2\3\2\2\2\u09a0\u099e\3\2\2\2")
        buf.write("\u09a1\u099a\3\2\2\2\u09a2\u09a3\3\2\2\2\u09a3\u09a1\3")
        buf.write("\2\2\2\u09a3\u09a4\3\2\2\2\u09a4\u09a5\3\2\2\2\u09a5\u09a6")
        buf.write("\5\u01ea\u00f6\2\u09a6\u09ab\3\2\2\2\u09a7\u09a8\5\u01e8")
        buf.write("\u00f5\2\u09a8\u09a9\5\u01ea\u00f6\2\u09a9\u09ab\3\2\2")
        buf.write("\2\u09aa\u0999\3\2\2\2\u09aa\u09a7\3\2\2\2\u09ab\u015d")
        buf.write("\3\2\2\2\u09ac\u09ad\5\u016a\u00b6\2\u09ad\u09ae\5\u0160")
        buf.write("\u00b1\2\u09ae\u015f\3\2\2\2\u09af\u09b1\5\u0162\u00b2")
        buf.write("\2\u09b0\u09b2\5\u008aF\2\u09b1\u09b0\3\2\2\2\u09b1\u09b2")
        buf.write("\3\2\2\2\u09b2\u0161\3\2\2\2\u09b3\u09b4\7N\2\2\u09b4")
        buf.write("\u09b7\5\u0126\u0094\2\u09b5\u09b7\5\u0164\u00b3\2\u09b6")
        buf.write("\u09b3\3\2\2\2\u09b6\u09b5\3\2\2\2\u09b7\u0163\3\2\2\2")
        buf.write("\u09b8\u09ba\5\u0168\u00b5\2\u09b9\u09b8\3\2\2\2\u09ba")
        buf.write("\u09bb\3\2\2\2\u09bb\u09b9\3\2\2\2\u09bb\u09bc\3\2\2\2")
        buf.write("\u09bc\u0165\3\2\2\2\u09bd\u09be\7\u0086\2\2\u09be\u09bf")
        buf.write("\5\u0164\u00b3\2\u09bf\u09c0\7\u0087\2\2\u09c0\u09c3\3")
        buf.write("\2\2\2\u09c1\u09c3\5\u0164\u00b3\2\u09c2\u09bd\3\2\2\2")
        buf.write("\u09c2\u09c1\3\2\2\2\u09c3\u0167\3\2\2\2\u09c4\u09c5\7")
        buf.write("X\2\2\u09c5\u09c6\5\u0158\u00ad\2\u09c6\u09c7\7N\2\2\u09c7")
        buf.write("\u09c8\5\u0126\u0094\2\u09c8\u0169\3\2\2\2\u09c9\u09ca")
        buf.write("\5\u0126\u0094\2\u09ca\u016b\3\2\2\2\u09cb\u09cc\5\u0126")
        buf.write("\u0094\2\u09cc\u016d\3\2\2\2\u09cd\u09ce\5\u0130\u0099")
        buf.write("\2\u09ce\u016f\3\2\2\2\u09cf\u09d1\5\u016e\u00b8\2\u09d0")
        buf.write("\u09cf\3\2\2\2\u09d1\u09d2\3\2\2\2\u09d2\u09d0\3\2\2\2")
        buf.write("\u09d2\u09d3\3\2\2\2\u09d3\u0171\3\2\2\2\u09d4\u09d5\5")
        buf.write("\u01ce\u00e8\2\u09d5\u09d6\7j\2\2\u09d6\u09d7\5\u016a")
        buf.write("\u00b6\2\u09d7\u0173\3\2\2\2\u09d8\u09da\5\u01e8\u00f5")
        buf.write("\2\u09d9\u09db\5\u0176\u00bc\2\u09da\u09d9\3\2\2\2\u09da")
        buf.write("\u09db\3\2\2\2\u09db\u09dc\3\2\2\2\u09dc\u09dd\5\u01ea")
        buf.write("\u00f6\2\u09dd\u0175\3\2\2\2\u09de\u09e8\5\u0178\u00bd")
        buf.write("\2\u09df\u09e1\5\u01ec\u00f7\2\u09e0\u09df\3\2\2\2\u09e1")
        buf.write("\u09e2\3\2\2\2\u09e2\u09e0\3\2\2\2\u09e2\u09e3\3\2\2\2")
        buf.write("\u09e3\u09e4\3\2\2\2\u09e4\u09e5\5\u0178\u00bd\2\u09e5")
        buf.write("\u09e7\3\2\2\2\u09e6\u09e0\3\2\2\2\u09e7\u09ea\3\2\2\2")
        buf.write("\u09e8\u09e6\3\2\2\2\u09e8\u09e9\3\2\2\2\u09e9\u09ee\3")
        buf.write("\2\2\2\u09ea\u09e8\3\2\2\2\u09eb\u09ed\5\u01ec\u00f7\2")
        buf.write("\u09ec\u09eb\3\2\2\2\u09ed\u09f0\3\2\2\2\u09ee\u09ec\3")
        buf.write("\2\2\2\u09ee\u09ef\3\2\2\2\u09ef\u0177\3\2\2\2\u09f0\u09ee")
        buf.write("\3\2\2\2\u09f1\u09fa\5\u017a\u00be\2\u09f2\u09f3\7-\2")
        buf.write("\2\u09f3\u09fa\5\u0174\u00bb\2\u09f4\u09f6\5\u01ec\u00f7")
        buf.write("\2\u09f5\u09f4\3\2\2\2\u09f6\u09f7\3\2\2\2\u09f7\u09f5")
        buf.write("\3\2\2\2\u09f7\u09f8\3\2\2\2\u09f8\u09fa\3\2\2\2\u09f9")
        buf.write("\u09f1\3\2\2\2\u09f9\u09f2\3\2\2\2\u09f9\u09f5\3\2\2\2")
        buf.write("\u09fa\u0179\3\2\2\2\u09fb\u09fc\5\u016c\u00b7\2\u09fc")
        buf.write("\u09fd\7O\2\2\u09fd\u09fe\5\u0126\u0094\2\u09fe\u0a03")
        buf.write("\3\2\2\2\u09ff\u0a03\5\u0126\u0094\2\u0a00\u0a01\7\26")
        buf.write("\2\2\u0a01\u0a03\5\u0088E\2\u0a02\u09fb\3\2\2\2\u0a02")
        buf.write("\u09ff\3\2\2\2\u0a02\u0a00\3\2\2\2\u0a03\u017b\3\2\2\2")
        buf.write("\u0a04\u0a09\5\u017e\u00c0\2\u0a05\u0a06\7h\2\2\u0a06")
        buf.write("\u0a08\5\u017e\u00c0\2\u0a07\u0a05\3\2\2\2\u0a08\u0a0b")
        buf.write("\3\2\2\2\u0a09\u0a07\3\2\2\2\u0a09\u0a0a\3\2\2\2\u0a0a")
        buf.write("\u0a0e\3\2\2\2\u0a0b\u0a09\3\2\2\2\u0a0c\u0a0e\7d\2\2")
        buf.write("\u0a0d\u0a04\3\2\2\2\u0a0d\u0a0c\3\2\2\2\u0a0e\u017d\3")
        buf.write("\2\2\2\u0a0f\u0a10\5\u01ce\u00e8\2\u0a10\u0a11\7j\2\2")
        buf.write("\u0a11\u0a12\5\u0126\u0094\2\u0a12\u0a15\3\2\2\2\u0a13")
        buf.write("\u0a15\5\u01ce\u00e8\2\u0a14\u0a0f\3\2\2\2\u0a14\u0a13")
        buf.write("\3\2\2\2\u0a15\u017f\3\2\2\2\u0a16\u0a18\5\u0182\u00c2")
        buf.write("\2\u0a17\u0a19\5\u01ec\u00f7\2\u0a18\u0a17\3\2\2\2\u0a19")
        buf.write("\u0a1a\3\2\2\2\u0a1a\u0a18\3\2\2\2\u0a1a\u0a1b\3\2\2\2")
        buf.write("\u0a1b\u0a1c\3\2\2\2\u0a1c\u0a1d\5\u0182\u00c2\2\u0a1d")
        buf.write("\u0a21\3\2\2\2\u0a1e\u0a20\5\u01ec\u00f7\2\u0a1f\u0a1e")
        buf.write("\3\2\2\2\u0a20\u0a23\3\2\2\2\u0a21\u0a1f\3\2\2\2\u0a21")
        buf.write("\u0a22\3\2\2\2\u0a22\u0181\3\2\2\2\u0a23\u0a21\3\2\2\2")
        buf.write("\u0a24\u0a25\5\u01d2\u00ea\2\u0a25\u0a26\7j\2\2\u0a26")
        buf.write("\u0a27\5\u0126\u0094\2\u0a27\u0183\3\2\2\2\u0a28\u0a2d")
        buf.write("\5\u0186\u00c4\2\u0a29\u0a2a\7X\2\2\u0a2a\u0a2c\5\u0186")
        buf.write("\u00c4\2\u0a2b\u0a29\3\2\2\2\u0a2c\u0a2f\3\2\2\2\u0a2d")
        buf.write("\u0a2b\3\2\2\2\u0a2d\u0a2e\3\2\2\2\u0a2e\u0185\3\2\2\2")
        buf.write("\u0a2f\u0a2d\3\2\2\2\u0a30\u0a31\5\u0188\u00c5\2\u0a31")
        buf.write("\u0187\3\2\2\2\u0a32\u0a37\5\u018a\u00c6\2\u0a33\u0a34")
        buf.write("\7h\2\2\u0a34\u0a36\5\u018a\u00c6\2\u0a35\u0a33\3\2\2")
        buf.write("\2\u0a36\u0a39\3\2\2\2\u0a37\u0a35\3\2\2\2\u0a37\u0a38")
        buf.write("\3\2\2\2\u0a38\u0189\3\2\2\2\u0a39\u0a37\3\2\2\2\u0a3a")
        buf.write("\u0a3b\7z\2\2\u0a3b\u0a3c\5\u0184\u00c3\2\u0a3c\u0a3d")
        buf.write("\7{\2\2\u0a3d\u0a40\3\2\2\2\u0a3e\u0a40\5\u018e\u00c8")
        buf.write("\2\u0a3f\u0a3a\3\2\2\2\u0a3f\u0a3e\3\2\2\2\u0a40\u018b")
        buf.write("\3\2\2\2\u0a41\u0a46\5\u018e\u00c8\2\u0a42\u0a43\7h\2")
        buf.write("\2\u0a43\u0a45\5\u018e\u00c8\2\u0a44\u0a42\3\2\2\2\u0a45")
        buf.write("\u0a48\3\2\2\2\u0a46\u0a44\3\2\2\2\u0a46\u0a47\3\2\2\2")
        buf.write("\u0a47\u018d\3\2\2\2\u0a48\u0a46\3\2\2\2\u0a49\u0a4c\5")
        buf.write("\u01cc\u00e7\2\u0a4a\u0a4c\5\u0196\u00cc\2\u0a4b\u0a49")
        buf.write("\3\2\2\2\u0a4b\u0a4a\3\2\2\2\u0a4c\u018f\3\2\2\2\u0a4d")
        buf.write("\u0a50\5\u0194\u00cb\2\u0a4e\u0a50\5\u019a\u00ce\2\u0a4f")
        buf.write("\u0a4d\3\2\2\2\u0a4f\u0a4e\3\2\2\2\u0a50\u0191\3\2\2\2")
        buf.write("\u0a51\u0a54\5\u0194\u00cb\2\u0a52\u0a54\5\u019c\u00cf")
        buf.write("\2\u0a53\u0a51\3\2\2\2\u0a53\u0a52\3\2\2\2\u0a54\u0193")
        buf.write("\3\2\2\2\u0a55\u0a5b\5\u01de\u00f0\2\u0a56\u0a57\7z\2")
        buf.write("\2\u0a57\u0a58\5\u01e2\u00f2\2\u0a58\u0a59\7{\2\2\u0a59")
        buf.write("\u0a5b\3\2\2\2\u0a5a\u0a55\3\2\2\2\u0a5a\u0a56\3\2\2\2")
        buf.write("\u0a5b\u0195\3\2\2\2\u0a5c\u0a63\5\u01e0\u00f1\2\u0a5d")
        buf.write("\u0a5e\7z\2\2\u0a5e\u0a5f\5\u01e4\u00f3\2\u0a5f\u0a60")
        buf.write("\7{\2\2\u0a60\u0a63\3\2\2\2\u0a61\u0a63\5\u019c\u00cf")
        buf.write("\2\u0a62\u0a5c\3\2\2\2\u0a62\u0a5d\3\2\2\2\u0a62\u0a61")
        buf.write("\3\2\2\2\u0a63\u0197\3\2\2\2\u0a64\u0a69\5\u0196\u00cc")
        buf.write("\2\u0a65\u0a66\7h\2\2\u0a66\u0a68\5\u0196\u00cc\2\u0a67")
        buf.write("\u0a65\3\2\2\2\u0a68\u0a6b\3\2\2\2\u0a69\u0a67\3\2\2\2")
        buf.write("\u0a69\u0a6a\3\2\2\2\u0a6a\u0199\3\2\2\2\u0a6b\u0a69\3")
        buf.write("\2\2\2\u0a6c\u0a6d\7z\2\2\u0a6d\u0a79\7{\2\2\u0a6e\u0a6f")
        buf.write("\7z\2\2\u0a6f\u0a70\5\u01f0\u00f9\2\u0a70\u0a71\7{\2\2")
        buf.write("\u0a71\u0a79\3\2\2\2\u0a72\u0a73\7x\2\2\u0a73\u0a79\7")
        buf.write("y\2\2\u0a74\u0a75\7x\2\2\u0a75\u0a76\5\u01f0\u00f9\2\u0a76")
        buf.write("\u0a77\7y\2\2\u0a77\u0a79\3\2\2\2\u0a78\u0a6c\3\2\2\2")
        buf.write("\u0a78\u0a6e\3\2\2\2\u0a78\u0a72\3\2\2\2\u0a78\u0a74\3")
        buf.write("\2\2\2\u0a79\u019b\3\2\2\2\u0a7a\u0a7e\5\u019a\u00ce\2")
        buf.write("\u0a7b\u0a7c\7|\2\2\u0a7c\u0a7e\7}\2\2\u0a7d\u0a7a\3\2")
        buf.write("\2\2\u0a7d\u0a7b\3\2\2\2\u0a7e\u019d\3\2\2\2\u0a7f\u0a85")
        buf.write("\5\u01e4\u00f3\2\u0a80\u0a81\7n\2\2\u0a81\u0a82\5\u01e0")
        buf.write("\u00f1\2\u0a82\u0a83\7n\2\2\u0a83\u0a85\3\2\2\2\u0a84")
        buf.write("\u0a7f\3\2\2\2\u0a84\u0a80\3\2\2\2\u0a85\u019f\3\2\2\2")
        buf.write("\u0a86\u0a8c\5\u01a2\u00d2\2\u0a87\u0a88\7n\2\2\u0a88")
        buf.write("\u0a89\5\u01de\u00f0\2\u0a89\u0a8a\7n\2\2\u0a8a\u0a8c")
        buf.write("\3\2\2\2\u0a8b\u0a86\3\2\2\2\u0a8b\u0a87\3\2\2\2\u0a8c")
        buf.write("\u01a1\3\2\2\2\u0a8d\u0a90\7i\2\2\u0a8e\u0a90\5\u01e2")
        buf.write("\u00f2\2\u0a8f\u0a8d\3\2\2\2\u0a8f\u0a8e\3\2\2\2\u0a90")
        buf.write("\u01a3\3\2\2\2\u0a91\u0a97\5\u01a6\u00d4\2\u0a92\u0a93")
        buf.write("\7z\2\2\u0a93\u0a97\7{\2\2\u0a94\u0a95\7x\2\2\u0a95\u0a97")
        buf.write("\7y\2\2\u0a96\u0a91\3\2\2\2\u0a96\u0a92\3\2\2\2\u0a96")
        buf.write("\u0a94\3\2\2\2\u0a97\u01a5\3\2\2\2\u0a98\u0aa7\5\u01a8")
        buf.write("\u00d5\2\u0a99\u0a9a\7z\2\2\u0a9a\u0a9b\5\u01f0\u00f9")
        buf.write("\2\u0a9b\u0a9c\7{\2\2\u0a9c\u0aa7\3\2\2\2\u0a9d\u0a9e")
        buf.write("\7x\2\2\u0a9e\u0a9f\5\u01f0\u00f9\2\u0a9f\u0aa0\7y\2\2")
        buf.write("\u0aa0\u0aa7\3\2\2\2\u0aa1\u0aa2\7z\2\2\u0aa2\u0aa3\7")
        buf.write("N\2\2\u0aa3\u0aa7\7{\2\2\u0aa4\u0aa5\7|\2\2\u0aa5\u0aa7")
        buf.write("\7}\2\2\u0aa6\u0a98\3\2\2\2\u0aa6\u0a99\3\2\2\2\u0aa6")
        buf.write("\u0a9d\3\2\2\2\u0aa6\u0aa1\3\2\2\2\u0aa6\u0aa4\3\2\2\2")
        buf.write("\u0aa7\u01a7\3\2\2\2\u0aa8\u0aae\5\u01ac\u00d7\2\u0aa9")
        buf.write("\u0aaa\7z\2\2\u0aaa\u0aab\5\u01b0\u00d9\2\u0aab\u0aac")
        buf.write("\7{\2\2\u0aac\u0aae\3\2\2\2\u0aad\u0aa8\3\2\2\2\u0aad")
        buf.write("\u0aa9\3\2\2\2\u0aae\u01a9\3\2\2\2\u0aaf\u0ab5\5\u01b0")
        buf.write("\u00d9\2\u0ab0\u0ab1\7n\2\2\u0ab1\u0ab2\5\u01ac\u00d7")
        buf.write("\2\u0ab2\u0ab3\7n\2\2\u0ab3\u0ab5\3\2\2\2\u0ab4\u0aaf")
        buf.write("\3\2\2\2\u0ab4\u0ab0\3\2\2\2\u0ab5\u01ab\3\2\2\2\u0ab6")
        buf.write("\u0ab7\5\u01ee\u00f8\2\u0ab7\u0ab8\7e\2\2\u0ab8\u0aba")
        buf.write("\3\2\2\2\u0ab9\u0ab6\3\2\2\2\u0ab9\u0aba\3\2\2\2\u0aba")
        buf.write("\u0abb\3\2\2\2\u0abb\u0abc\5\u01ae\u00d8\2\u0abc\u01ad")
        buf.write("\3\2\2\2\u0abd\u0abe\5\u01e0\u00f1\2\u0abe\u01af\3\2\2")
        buf.write("\2\u0abf\u0ac3\5\u01e2\u00f2\2\u0ac0\u0ac3\5\u01d4\u00eb")
        buf.write("\2\u0ac1\u0ac3\5\u01b2\u00da\2\u0ac2\u0abf\3\2\2\2\u0ac2")
        buf.write("\u0ac0\3\2\2\2\u0ac2\u0ac1\3\2\2\2\u0ac3\u01b1\3\2\2\2")
        buf.write("\u0ac4\u0aca\5\u01e4\u00f3\2\u0ac5\u0aca\5\u01d8\u00ed")
        buf.write("\2\u0ac6\u0aca\7i\2\2\u0ac7\u0aca\7\\\2\2\u0ac8\u0aca")
        buf.write("\7e\2\2\u0ac9\u0ac4\3\2\2\2\u0ac9\u0ac5\3\2\2\2\u0ac9")
        buf.write("\u0ac6\3\2\2\2\u0ac9\u0ac7\3\2\2\2\u0ac9\u0ac8\3\2\2\2")
        buf.write("\u0aca\u01b3\3\2\2\2\u0acb\u0ace\5\u01b6\u00dc\2\u0acc")
        buf.write("\u0ace\5\u019e\u00d0\2\u0acd\u0acb\3\2\2\2\u0acd\u0acc")
        buf.write("\3\2\2\2\u0ace\u01b5\3\2\2\2\u0acf\u0ad5\5\u01d8\u00ed")
        buf.write("\2\u0ad0\u0ad1\7n\2\2\u0ad1\u0ad2\5\u01d2\u00ea\2\u0ad2")
        buf.write("\u0ad3\7n\2\2\u0ad3\u0ad5\3\2\2\2\u0ad4\u0acf\3\2\2\2")
        buf.write("\u0ad4\u0ad0\3\2\2\2\u0ad5\u01b7\3\2\2\2\u0ad6\u0ad9\5")
        buf.write("\u01be\u00e0\2\u0ad7\u0ad9\5\u01a0\u00d1\2\u0ad8\u0ad6")
        buf.write("\3\2\2\2\u0ad8\u0ad7\3\2\2\2\u0ad9\u01b9\3\2\2\2\u0ada")
        buf.write("\u0ade\5\u01c0\u00e1\2\u0adb\u0ade\5\u01a0\u00d1\2\u0adc")
        buf.write("\u0ade\5\u01bc\u00df\2\u0add\u0ada\3\2\2\2\u0add\u0adb")
        buf.write("\3\2\2\2\u0add\u0adc\3\2\2\2\u0ade\u01bb\3\2\2\2\u0adf")
        buf.write("\u0ae0\7n\2\2\u0ae0\u0ae1\7\36\2\2\u0ae1\u0ae2\7n\2\2")
        buf.write("\u0ae2\u01bd\3\2\2\2\u0ae3\u0ae9\5\u01d4\u00eb\2\u0ae4")
        buf.write("\u0ae5\7n\2\2\u0ae5\u0ae6\5\u01d0\u00e9\2\u0ae6\u0ae7")
        buf.write("\7n\2\2\u0ae7\u0ae9\3\2\2\2\u0ae8\u0ae3\3\2\2\2\u0ae8")
        buf.write("\u0ae4\3\2\2\2\u0ae9\u01bf\3\2\2\2\u0aea\u0af0\5\u01d6")
        buf.write("\u00ec\2\u0aeb\u0aec\7n\2\2\u0aec\u0aed\5\u01d0\u00e9")
        buf.write("\2\u0aed\u0aee\7n\2\2\u0aee\u0af0\3\2\2\2\u0aef\u0aea")
        buf.write("\3\2\2\2\u0aef\u0aeb\3\2\2\2\u0af0\u01c1\3\2\2\2\u0af1")
        buf.write("\u0af2\5\u01d2\u00ea\2\u0af2\u01c3\3\2\2\2\u0af3\u0af4")
        buf.write("\7n\2\2\u0af4\u0af5\5\u01c6\u00e4\2\u0af5\u0af6\7n\2\2")
        buf.write("\u0af6\u01c5\3\2\2\2\u0af7\u0afd\5\u01d2\u00ea\2\u0af8")
        buf.write("\u0afd\5\u01dc\u00ef\2\u0af9\u0afd\7$\2\2\u0afa\u0afd")
        buf.write("\7\"\2\2\u0afb\u0afd\7#\2\2\u0afc\u0af7\3\2\2\2\u0afc")
        buf.write("\u0af8\3\2\2\2\u0afc\u0af9\3\2\2\2\u0afc\u0afa\3\2\2\2")
        buf.write("\u0afc\u0afb\3\2\2\2\u0afd\u01c7\3\2\2\2\u0afe\u0aff\5")
        buf.write("\u01e0\u00f1\2\u0aff\u01c9\3\2\2\2\u0b00\u0b01\5\u01ee")
        buf.write("\u00f8\2\u0b01\u0b02\7e\2\2\u0b02\u0b04\3\2\2\2\u0b03")
        buf.write("\u0b00\3\2\2\2\u0b03\u0b04\3\2\2\2\u0b04\u0b05\3\2\2\2")
        buf.write("\u0b05\u0b06\5\u01c8\u00e5\2\u0b06\u01cb\3\2\2\2\u0b07")
        buf.write("\u0b0d\5\u01d2\u00ea\2\u0b08\u0b09\7z\2\2\u0b09\u0b0a")
        buf.write("\5\u01d8\u00ed\2\u0b0a\u0b0b\7{\2\2\u0b0b\u0b0d\3\2\2")
        buf.write("\2\u0b0c\u0b07\3\2\2\2\u0b0c\u0b08\3\2\2\2\u0b0d\u01cd")
        buf.write("\3\2\2\2\u0b0e\u0b14\5\u01d0\u00e9\2\u0b0f\u0b10\7z\2")
        buf.write("\2\u0b10\u0b11\5\u01d4\u00eb\2\u0b11\u0b12\7{\2\2\u0b12")
        buf.write("\u0b14\3\2\2\2\u0b13\u0b0e\3\2\2\2\u0b13\u0b0f\3\2\2\2")
        buf.write("\u0b14\u01cf\3\2\2\2\u0b15\u0b16\5\u01ee\u00f8\2\u0b16")
        buf.write("\u0b17\7e\2\2\u0b17\u0b19\3\2\2\2\u0b18\u0b15\3\2\2\2")
        buf.write("\u0b18\u0b19\3\2\2\2\u0b19\u0b1a\3\2\2\2\u0b1a\u0b1b\5")
        buf.write("\u01d2\u00ea\2\u0b1b\u01d1\3\2\2\2\u0b1c\u0b1f\7\u0080")
        buf.write("\2\2\u0b1d\u0b1f\5\u01dc\u00ef\2\u0b1e\u0b1c\3\2\2\2\u0b1e")
        buf.write("\u0b1d\3\2\2\2\u0b1f\u0b23\3\2\2\2\u0b20\u0b22\7T\2\2")
        buf.write("\u0b21\u0b20\3\2\2\2\u0b22\u0b25\3\2\2\2\u0b23\u0b21\3")
        buf.write("\2\2\2\u0b23\u0b24\3\2\2\2\u0b24\u01d3\3\2\2\2\u0b25\u0b23")
        buf.write("\3\2\2\2\u0b26\u0b27\5\u01ee\u00f8\2\u0b27\u0b28\7e\2")
        buf.write("\2\u0b28\u0b2a\3\2\2\2\u0b29\u0b26\3\2\2\2\u0b29\u0b2a")
        buf.write("\3\2\2\2\u0b2a\u0b2b\3\2\2\2\u0b2b\u0b2c\5\u01d8\u00ed")
        buf.write("\2\u0b2c\u01d5\3\2\2\2\u0b2d\u0b30\5\u01da\u00ee\2\u0b2e")
        buf.write("\u0b30\5\u01d4\u00eb\2\u0b2f\u0b2d\3\2\2\2\u0b2f\u0b2e")
        buf.write("\3\2\2\2\u0b30\u01d7\3\2\2\2\u0b31\u0b34\5\u01da\u00ee")
        buf.write("\2\u0b32\u0b34\7\\\2\2\u0b33\u0b31\3\2\2\2\u0b33\u0b32")
        buf.write("\3\2\2\2\u0b34\u01d9\3\2\2\2\u0b35\u0b37\5\u01f8\u00fd")
        buf.write("\2\u0b36\u0b35\3\2\2\2\u0b37\u0b38\3\2\2\2\u0b38\u0b36")
        buf.write("\3\2\2\2\u0b38\u0b39\3\2\2\2\u0b39\u01db\3\2\2\2\u0b3a")
        buf.write("\u0b3b\t\7\2\2\u0b3b\u01dd\3\2\2\2\u0b3c\u0b3d\5\u01ee")
        buf.write("\u00f8\2\u0b3d\u0b3e\7e\2\2\u0b3e\u0b40\3\2\2\2\u0b3f")
        buf.write("\u0b3c\3\2\2\2\u0b3f\u0b40\3\2\2\2\u0b40\u0b41\3\2\2\2")
        buf.write("\u0b41\u0b42\5\u01e0\u00f1\2\u0b42\u01df\3\2\2\2\u0b43")
        buf.write("\u0b47\7\u0081\2\2\u0b44\u0b46\7T\2\2\u0b45\u0b44\3\2")
        buf.write("\2\2\u0b46\u0b49\3\2\2\2\u0b47\u0b45\3\2\2\2\u0b47\u0b48")
        buf.write("\3\2\2\2\u0b48\u01e1\3\2\2\2\u0b49\u0b47\3\2\2\2\u0b4a")
        buf.write("\u0b4b\5\u01ee\u00f8\2\u0b4b\u0b4c\7e\2\2\u0b4c\u0b4e")
        buf.write("\3\2\2\2\u0b4d\u0b4a\3\2\2\2\u0b4d\u0b4e\3\2\2\2\u0b4e")
        buf.write("\u0b4f\3\2\2\2\u0b4f\u0b50\5\u01e4\u00f3\2\u0b50\u01e3")
        buf.write("\3\2\2\2\u0b51\u0b55\7i\2\2\u0b52\u0b54\5\u01f8\u00fd")
        buf.write("\2\u0b53\u0b52\3\2\2\2\u0b54\u0b57\3\2\2\2\u0b55\u0b53")
        buf.write("\3\2\2\2\u0b55\u0b56\3\2\2\2\u0b56\u01e5\3\2\2\2\u0b57")
        buf.write("\u0b55\3\2\2\2\u0b58\u0b5d\5\u01fa\u00fe\2\u0b59\u0b5d")
        buf.write("\5\u01fc\u00ff\2\u0b5a\u0b5d\5\u01fe\u0100\2\u0b5b\u0b5d")
        buf.write("\5\u0200\u0101\2\u0b5c\u0b58\3\2\2\2\u0b5c\u0b59\3\2\2")
        buf.write("\2\u0b5c\u0b5a\3\2\2\2\u0b5c\u0b5b\3\2\2\2\u0b5d\u01e7")
        buf.write("\3\2\2\2\u0b5e\u0b5f\t\b\2\2\u0b5f\u01e9\3\2\2\2\u0b60")
        buf.write("\u0b61\t\t\2\2\u0b61\u01eb\3\2\2\2\u0b62\u0b63\t\n\2\2")
        buf.write("\u0b63\u01ed\3\2\2\2\u0b64\u0b65\5\u01e0\u00f1\2\u0b65")
        buf.write("\u0b66\7e\2\2\u0b66\u0b68\3\2\2\2\u0b67\u0b64\3\2\2\2")
        buf.write("\u0b68\u0b6b\3\2\2\2\u0b69\u0b67\3\2\2\2\u0b69\u0b6a\3")
        buf.write("\2\2\2\u0b6a\u0b6c\3\2\2\2\u0b6b\u0b69\3\2\2\2\u0b6c\u0b6d")
        buf.write("\5\u01e0\u00f1\2\u0b6d\u01ef\3\2\2\2\u0b6e\u0b70\7h\2")
        buf.write("\2\u0b6f\u0b6e\3\2\2\2\u0b70\u0b71\3\2\2\2\u0b71\u0b6f")
        buf.write("\3\2\2\2\u0b71\u0b72\3\2\2\2\u0b72\u01f1\3\2\2\2\u0b73")
        buf.write("\u0b75\7X\2\2\u0b74\u0b73\3\2\2\2\u0b75\u0b76\3\2\2\2")
        buf.write("\u0b76\u0b74\3\2\2\2\u0b76\u0b77\3\2\2\2\u0b77\u01f3\3")
        buf.write("\2\2\2\u0b78\u0b79\t\13\2\2\u0b79\u01f5\3\2\2\2\u0b7a")
        buf.write("\u0b7b\5\u01f8\u00fd\2\u0b7b\u01f7\3\2\2\2\u0b7c\u0b7d")
        buf.write("\t\f\2\2\u0b7d\u01f9\3\2\2\2\u0b7e\u0b7f\t\r\2\2\u0b7f")
        buf.write("\u01fb\3\2\2\2\u0b80\u0b81\7\u008e\2\2\u0b81\u01fd\3\2")
        buf.write("\2\2\u0b82\u0b83\7~\2\2\u0b83\u01ff\3\2\2\2\u0b84\u0b85")
        buf.write("\7\177\2\2\u0b85\u0201\3\2\2\2\u0159\u0203\u0208\u020c")
        buf.write("\u0211\u0216\u0219\u021c\u0223\u0230\u0236\u023b\u0244")
        buf.write("\u0249\u0250\u0254\u0259\u0260\u0264\u0269\u0272\u0277")
        buf.write("\u0279\u0281\u0284\u0287\u0296\u0299\u029c\u02a8\u02ab")
        buf.write("\u02ae\u02b2\u02b6\u02bb\u02be\u02c3\u02cb\u02cf\u02d1")
        buf.write("\u02db\u02df\u02e1\u02e4\u02f1\u02f4\u02f7\u02ff\u0302")
        buf.write("\u0304\u0308\u0311\u0318\u031c\u031e\u0329\u0331\u0337")
        buf.write("\u033d\u0343\u0348\u034b\u0356\u0359\u035c\u0360\u0365")
        buf.write("\u0369\u036e\u0372\u0376\u0379\u037c\u0380\u0384\u0387")
        buf.write("\u038a\u0390\u0392\u039e\u03a3\u03a7\u03af\u03b3\u03b8")
        buf.write("\u03bc\u03c1\u03c5\u03c8\u03cb\u03d0\u03d4\u03d7\u03da")
        buf.write("\u03dc\u03ea\u03f5\u0401\u0408\u0413\u0419\u041f\u0425")
        buf.write("\u042a\u0435\u0439\u043d\u0441\u0445\u0449\u044c\u0450")
        buf.write("\u0455\u0458\u045d\u0461\u0464\u0469\u046d\u0470\u0474")
        buf.write("\u0477\u047a\u047e\u0481\u0485\u0488\u048b\u048d\u0499")
        buf.write("\u04a2\u04a9\u04ad\u04b6\u04bf\u04ca\u04ce\u04d2\u04da")
        buf.write("\u04df\u04e3\u04ef\u04f1\u04f5\u0500\u0505\u050c\u0512")
        buf.write("\u0522\u0528\u052e\u0534\u0539\u0542\u0548\u054e\u0554")
        buf.write("\u0559\u0564\u056a\u0570\u0575\u057c\u0580\u058b\u058f")
        buf.write("\u0593\u0596\u059e\u05ad\u05b1\u05b6\u05b9\u05be\u05c7")
        buf.write("\u05cf\u05d3\u05de\u05e2\u05ea\u05ed\u05f4\u0609\u060e")
        buf.write("\u0616\u061d\u0632\u063a\u0643\u064c\u0653\u0657\u0665")
        buf.write("\u0669\u0677\u0682\u0689\u0690\u0699\u06a5\u06b0\u06db")
        buf.write("\u06e9\u06f2\u06fa\u0704\u070a\u0717\u0720\u072a\u072e")
        buf.write("\u0732\u0737\u073e\u0743\u074e\u075f\u0763\u0768\u076e")
        buf.write("\u0779\u0783\u078f\u0798\u079d\u07a5\u07a7\u07ae\u07b0")
        buf.write("\u07b5\u07b9\u07bb\u07c0\u07d3\u07dc\u07e3\u07ec\u07f3")
        buf.write("\u07fd\u080e\u0814\u0816\u0821\u082d\u0844\u084c\u0852")
        buf.write("\u0859\u085d\u0876\u087b\u088c\u0891\u0896\u08d8\u08dc")
        buf.write("\u08e0\u08eb\u08f1\u08f9\u0907\u0911\u0916\u0918\u091c")
        buf.write("\u0922\u093c\u0945\u094f\u0957\u095f\u0967\u096f\u0972")
        buf.write("\u0986\u098d\u0997\u099e\u09a3\u09aa\u09b1\u09b6\u09bb")
        buf.write("\u09c2\u09d2\u09da\u09e2\u09e8\u09ee\u09f7\u09f9\u0a02")
        buf.write("\u0a09\u0a0d\u0a14\u0a1a\u0a21\u0a2d\u0a37\u0a3f\u0a46")
        buf.write("\u0a4b\u0a4f\u0a53\u0a5a\u0a62\u0a69\u0a78\u0a7d\u0a84")
        buf.write("\u0a8b\u0a8f\u0a96\u0aa6\u0aad\u0ab4\u0ab9\u0ac2\u0ac9")
        buf.write("\u0acd\u0ad4\u0ad8\u0add\u0ae8\u0aef\u0afc\u0b03\u0b0c")
        buf.write("\u0b13\u0b18\u0b1e\u0b23\u0b29\u0b2f\u0b33\u0b38\u0b3f")
        buf.write("\u0b47\u0b4d\u0b55\u0b5c\u0b69\u0b71\u0b76")
        return buf.getvalue()


class HaskellParser ( Parser ):

    grammarFileName = "HaskellParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'as'", "'case'", "'class'", "'data'", "'default'", 
                     "'deriving'", "'do'", "'else'", "'hiding'", "'if'", 
                     "'import'", "'in'", "'infix'", "'infixl'", "'infixr'", 
                     "'instance'", "'let'", "'module'", "'newtype'", "'of'", 
                     "'qualified'", "'then'", "'type'", "'where'", "'_'", 
                     "'forall'", "'foreign'", "'export'", "'safe'", "'interruptible'", 
                     "'unsafe'", "'mdo'", "'family'", "'role'", "'stdcall'", 
                     "'ccall'", "'capi'", "'cplusplus'", "'javascript'", 
                     "'rec'", "'group'", "'by'", "'using'", "'pattern'", 
                     "'stock'", "'anyclass'", "'via'", "'LANGUAGE'", "'OPTIONS_GHC'", 
                     "'OPTIONS'", "'INLINE'", "'NOINLINE'", "'SPECIALISE'", 
                     "'SPECIALISE_INLINE'", "'SOURCE'", "'RULES'", "'SCC'", 
                     "'DEPRECATED'", "'WARNING'", "'UNPACK'", "'NOUNPACK'", 
                     "'ANN'", "'MINIMAL'", "'CTYPE'", "'OVERLAPPING'", "'OVERLAPPABLE'", 
                     "'OVERLAPS'", "'INCOHERENT'", "'COMPLETE'", "<INVALID>", 
                     "'=>'", "'::'", "'->'", "'<-'", "'-<'", "'>-'", "'-<<'", 
                     "'>>-'", "'#'", "'<'", "'>'", "'&'", "'|'", "'!'", 
                     "'^'", "'+'", "'-'", "'*'", "'%'", "'/'", "'~'", "'@'", 
                     "'$$'", "'$'", "'..'", "'.'", "';'", "'?'", "','", 
                     "':'", "'='", "'''", "''''", "'\\'", "'`'", "<INVALID>", 
                     "<INVALID>", "'[||'", "'||]'", "'[|'", "'[p|'", "'[t|'", 
                     "'[d|'", "'|]'", "'(#'", "'#)'", "'('", "')'", "'['", 
                     "']'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'{-#'", "'#-}'", "<INVALID>", "<INVALID>", "'{'", 
                     "'}'", "'VOCURLY'", "'VCCURLY'", "'SEMI'" ]

    symbolicNames = [ "<INVALID>", "NEWLINE", "TAB", "WS", "AS", "CASE", 
                      "CLASS", "DATA", "DEFAULT", "DERIVING", "DO", "ELSE", 
                      "HIDING", "IF", "IMPORT", "IN", "INFIX", "INFIXL", 
                      "INFIXR", "INSTANCE", "LET", "MODULE", "NEWTYPE", 
                      "OF", "QUALIFIED", "THEN", "TYPE", "WHERE", "WILDCARD", 
                      "FORALL", "FOREIGN", "EXPORT", "SAFE", "INTERRUPTIBLE", 
                      "UNSAFE", "MDO", "FAMILY", "ROLE", "STDCALL", "CCALL", 
                      "CAPI", "CPPCALL", "JSCALL", "REC", "GROUP", "BY", 
                      "USING", "PATTERN", "STOCK", "ANYCLASS", "VIA", "LANGUAGE", 
                      "OPTIONS_GHC", "OPTIONS", "INLINE", "NOINLINE", "SPECIALISE", 
                      "SPECINLINE", "SOURCE", "RULES", "SCC", "DEPRECATED", 
                      "WARNING", "UNPACK", "NOUNPACK", "ANN", "MINIMAL", 
                      "CTYPE", "OVERLAPPING", "OVERLAPPABLE", "OVERLAPS", 
                      "INCOHERENT", "COMPLETE", "LCASE", "DoubleArrow", 
                      "DoubleColon", "Arrow", "Revarrow", "LarrowTail", 
                      "RarrowTail", "LLarrowTail", "RRarrowTail", "Hash", 
                      "Less", "Greater", "Ampersand", "Pipe", "Bang", "Caret", 
                      "Plus", "Minus", "Asterisk", "Percent", "Divide", 
                      "Tilde", "Atsign", "DDollar", "Dollar", "DoubleDot", 
                      "Dot", "Semi", "QuestionMark", "Comma", "Colon", "Eq", 
                      "Quote", "DoubleQuote", "ReverseSlash", "BackQuote", 
                      "AopenParen", "AcloseParen", "TopenTexpQuote", "TcloseTExpQoute", 
                      "TopenExpQuote", "TopenPatQuote", "TopenTypQoute", 
                      "TopenDecQoute", "TcloseQoute", "OpenBoxParen", "CloseBoxParen", 
                      "OpenRoundBracket", "CloseRoundBracket", "OpenSquareBracket", 
                      "CloseSquareBracket", "CHAR", "STRING", "VARID", "CONID", 
                      "OpenPragmaBracket", "ClosePragmaBracket", "COMMENT", 
                      "NCOMMENT", "OCURLY", "CCURLY", "VOCURLY", "VCCURLY", 
                      "SEMI", "DECIMAL", "OCTAL", "HEXADECIMAL", "FLOAT", 
                      "EXPONENT" ]

    RULE_module = 0
    RULE_module_content = 1
    RULE_where_module = 2
    RULE_module_body = 3
    RULE_pragmas = 4
    RULE_pragma = 5
    RULE_language_pragma = 6
    RULE_options_ghc = 7
    RULE_simple_options = 8
    RULE_extension = 9
    RULE_body = 10
    RULE_impdecls = 11
    RULE_exports = 12
    RULE_exprt = 13
    RULE_impdecl = 14
    RULE_impspec = 15
    RULE_himport = 16
    RULE_cname = 17
    RULE_fixity = 18
    RULE_ops = 19
    RULE_topdecls = 20
    RULE_topdecl = 21
    RULE_cl_decl = 22
    RULE_ty_decl = 23
    RULE_standalone_kind_sig = 24
    RULE_sks_vars = 25
    RULE_inst_decl = 26
    RULE_overlap_pragma = 27
    RULE_deriv_strategy_no_via = 28
    RULE_deriv_strategy_via = 29
    RULE_deriv_standalone_strategy = 30
    RULE_opt_injective_info = 31
    RULE_injectivity_cond = 32
    RULE_inj_varids = 33
    RULE_where_type_family = 34
    RULE_ty_fam_inst_eqn_list = 35
    RULE_ty_fam_inst_eqns = 36
    RULE_ty_fam_inst_eqn = 37
    RULE_at_decl_cls = 38
    RULE_at_decl_inst = 39
    RULE_opt_kind_sig = 40
    RULE_opt_datafam_kind_sig = 41
    RULE_opt_tyfam_kind_sig = 42
    RULE_opt_at_kind_inj_sig = 43
    RULE_tycl_hdr = 44
    RULE_tycl_hdr_inst = 45
    RULE_capi_ctype = 46
    RULE_standalone_deriving = 47
    RULE_role_annot = 48
    RULE_roles = 49
    RULE_role = 50
    RULE_pattern_synonym_decl = 51
    RULE_pattern_synonym_lhs = 52
    RULE_hvars = 53
    RULE_cvars = 54
    RULE_where_decls = 55
    RULE_pattern_synonym_sig = 56
    RULE_decl_cls = 57
    RULE_decls_cls = 58
    RULE_decllist_cls = 59
    RULE_where_cls = 60
    RULE_decl_inst = 61
    RULE_decls_inst = 62
    RULE_decllist_inst = 63
    RULE_where_inst = 64
    RULE_decls = 65
    RULE_decllist = 66
    RULE_binds = 67
    RULE_wherebinds = 68
    RULE_rules = 69
    RULE_pragma_rule = 70
    RULE_rule_activation_marker = 71
    RULE_rule_activation = 72
    RULE_rule_foralls = 73
    RULE_rule_vars = 74
    RULE_rule_var = 75
    RULE_warnings = 76
    RULE_pragma_warning = 77
    RULE_deprecations = 78
    RULE_pragma_deprecation = 79
    RULE_strings = 80
    RULE_stringlist = 81
    RULE_annotation = 82
    RULE_fdecl = 83
    RULE_callconv = 84
    RULE_safety = 85
    RULE_fspec = 86
    RULE_opt_sig = 87
    RULE_opt_tyconsig = 88
    RULE_sigtype = 89
    RULE_sigtypedoc = 90
    RULE_sig_vars = 91
    RULE_sigtypes1 = 92
    RULE_unpackedness = 93
    RULE_forall_vis_flag = 94
    RULE_ktype = 95
    RULE_ktypedoc = 96
    RULE_ctype = 97
    RULE_ctypedoc = 98
    RULE_tycl_context = 99
    RULE_constr_context = 100
    RULE_htype = 101
    RULE_typedoc = 102
    RULE_constr_btype = 103
    RULE_constr_tyapps = 104
    RULE_constr_tyapp = 105
    RULE_btype = 106
    RULE_tyapps = 107
    RULE_tyapp = 108
    RULE_atype = 109
    RULE_inst_type = 110
    RULE_deriv_types = 111
    RULE_comma_types = 112
    RULE_bar_types2 = 113
    RULE_tv_bndrs = 114
    RULE_tv_bndr = 115
    RULE_tv_bndr_no_braces = 116
    RULE_fds = 117
    RULE_fds1 = 118
    RULE_fd = 119
    RULE_varids0 = 120
    RULE_kind = 121
    RULE_gadt_constrlist = 122
    RULE_gadt_constrs = 123
    RULE_gadt_constr_with_doc = 124
    RULE_gadt_constr = 125
    RULE_constrs = 126
    RULE_constrs1 = 127
    RULE_constr = 128
    RULE_forall = 129
    RULE_constr_stuff = 130
    RULE_fielddecls = 131
    RULE_fielddecl = 132
    RULE_derivings = 133
    RULE_deriving = 134
    RULE_deriv_clause_types = 135
    RULE_decl_no_th = 136
    RULE_decl = 137
    RULE_rhs = 138
    RULE_gdrhs = 139
    RULE_gdrh = 140
    RULE_sigdecl = 141
    RULE_activation = 142
    RULE_th_quasiquote = 143
    RULE_th_qquasiquote = 144
    RULE_quasiquote = 145
    RULE_exp = 146
    RULE_infixexp = 147
    RULE_exp10p = 148
    RULE_exp10 = 149
    RULE_fexp = 150
    RULE_aexp = 151
    RULE_aexp1 = 152
    RULE_aexp2 = 153
    RULE_splice_exp = 154
    RULE_splice_untyped = 155
    RULE_splice_typed = 156
    RULE_cmdargs = 157
    RULE_acmd = 158
    RULE_cvtopbody = 159
    RULE_cvtopdecls0 = 160
    RULE_texp = 161
    RULE_tup_exprs = 162
    RULE_commas_tup_tail = 163
    RULE_tup_tail = 164
    RULE_lst = 165
    RULE_lexps = 166
    RULE_flattenedpquals = 167
    RULE_pquals = 168
    RULE_squals = 169
    RULE_transformqual = 170
    RULE_guards = 171
    RULE_guard = 172
    RULE_alts = 173
    RULE_alt = 174
    RULE_alt_rhs = 175
    RULE_ralt = 176
    RULE_gdpats = 177
    RULE_ifgdpats = 178
    RULE_gdpat = 179
    RULE_pat = 180
    RULE_bindpat = 181
    RULE_apat = 182
    RULE_apats = 183
    RULE_fpat = 184
    RULE_stmtlist = 185
    RULE_stmts = 186
    RULE_stmt = 187
    RULE_qual = 188
    RULE_fbinds = 189
    RULE_fbind = 190
    RULE_dbinds = 191
    RULE_dbind = 192
    RULE_name_boolformula_opt = 193
    RULE_name_boolformula_and = 194
    RULE_name_boolformula_and_list = 195
    RULE_name_boolformula_atom = 196
    RULE_namelist = 197
    RULE_name_var = 198
    RULE_qcon_nowiredlist = 199
    RULE_qcon = 200
    RULE_gen_qcon = 201
    RULE_con = 202
    RULE_con_list = 203
    RULE_sysdcon_nolist = 204
    RULE_sysdcon = 205
    RULE_conop = 206
    RULE_qconop = 207
    RULE_gconsym = 208
    RULE_gtycon = 209
    RULE_ntgtycon = 210
    RULE_oqtycon = 211
    RULE_qtyconop = 212
    RULE_qtycon = 213
    RULE_tycon = 214
    RULE_qtyconsym = 215
    RULE_tyconsym = 216
    RULE_op = 217
    RULE_varop = 218
    RULE_qop = 219
    RULE_qopm = 220
    RULE_hole_op = 221
    RULE_qvarop = 222
    RULE_qvaropm = 223
    RULE_tyvar = 224
    RULE_tyvarop = 225
    RULE_tyvarid = 226
    RULE_tycls = 227
    RULE_qtycls = 228
    RULE_var = 229
    RULE_qvar = 230
    RULE_qvarid = 231
    RULE_varid = 232
    RULE_qvarsym = 233
    RULE_qvarsym_no_minus = 234
    RULE_varsym = 235
    RULE_varsym_no_minus = 236
    RULE_special_id = 237
    RULE_qconid = 238
    RULE_conid = 239
    RULE_qconsym = 240
    RULE_consym = 241
    RULE_literal = 242
    RULE_opn = 243
    RULE_close = 244
    RULE_semi = 245
    RULE_modid = 246
    RULE_commas = 247
    RULE_bars = 248
    RULE_special = 249
    RULE_symbol = 250
    RULE_ascSymbol = 251
    RULE_integer = 252
    RULE_pfloat = 253
    RULE_pchar = 254
    RULE_pstring = 255

    ruleNames =  [ "module", "module_content", "where_module", "module_body", 
                   "pragmas", "pragma", "language_pragma", "options_ghc", 
                   "simple_options", "extension", "body", "impdecls", "exports", 
                   "exprt", "impdecl", "impspec", "himport", "cname", "fixity", 
                   "ops", "topdecls", "topdecl", "cl_decl", "ty_decl", "standalone_kind_sig", 
                   "sks_vars", "inst_decl", "overlap_pragma", "deriv_strategy_no_via", 
                   "deriv_strategy_via", "deriv_standalone_strategy", "opt_injective_info", 
                   "injectivity_cond", "inj_varids", "where_type_family", 
                   "ty_fam_inst_eqn_list", "ty_fam_inst_eqns", "ty_fam_inst_eqn", 
                   "at_decl_cls", "at_decl_inst", "opt_kind_sig", "opt_datafam_kind_sig", 
                   "opt_tyfam_kind_sig", "opt_at_kind_inj_sig", "tycl_hdr", 
                   "tycl_hdr_inst", "capi_ctype", "standalone_deriving", 
                   "role_annot", "roles", "role", "pattern_synonym_decl", 
                   "pattern_synonym_lhs", "hvars", "cvars", "where_decls", 
                   "pattern_synonym_sig", "decl_cls", "decls_cls", "decllist_cls", 
                   "where_cls", "decl_inst", "decls_inst", "decllist_inst", 
                   "where_inst", "decls", "decllist", "binds", "wherebinds", 
                   "rules", "pragma_rule", "rule_activation_marker", "rule_activation", 
                   "rule_foralls", "rule_vars", "rule_var", "warnings", 
                   "pragma_warning", "deprecations", "pragma_deprecation", 
                   "strings", "stringlist", "annotation", "fdecl", "callconv", 
                   "safety", "fspec", "opt_sig", "opt_tyconsig", "sigtype", 
                   "sigtypedoc", "sig_vars", "sigtypes1", "unpackedness", 
                   "forall_vis_flag", "ktype", "ktypedoc", "ctype", "ctypedoc", 
                   "tycl_context", "constr_context", "htype", "typedoc", 
                   "constr_btype", "constr_tyapps", "constr_tyapp", "btype", 
                   "tyapps", "tyapp", "atype", "inst_type", "deriv_types", 
                   "comma_types", "bar_types2", "tv_bndrs", "tv_bndr", "tv_bndr_no_braces", 
                   "fds", "fds1", "fd", "varids0", "kind", "gadt_constrlist", 
                   "gadt_constrs", "gadt_constr_with_doc", "gadt_constr", 
                   "constrs", "constrs1", "constr", "forall", "constr_stuff", 
                   "fielddecls", "fielddecl", "derivings", "deriving", "deriv_clause_types", 
                   "decl_no_th", "decl", "rhs", "gdrhs", "gdrh", "sigdecl", 
                   "activation", "th_quasiquote", "th_qquasiquote", "quasiquote", 
                   "exp", "infixexp", "exp10p", "exp10", "fexp", "aexp", 
                   "aexp1", "aexp2", "splice_exp", "splice_untyped", "splice_typed", 
                   "cmdargs", "acmd", "cvtopbody", "cvtopdecls0", "texp", 
                   "tup_exprs", "commas_tup_tail", "tup_tail", "lst", "lexps", 
                   "flattenedpquals", "pquals", "squals", "transformqual", 
                   "guards", "guard", "alts", "alt", "alt_rhs", "ralt", 
                   "gdpats", "ifgdpats", "gdpat", "pat", "bindpat", "apat", 
                   "apats", "fpat", "stmtlist", "stmts", "stmt", "qual", 
                   "fbinds", "fbind", "dbinds", "dbind", "name_boolformula_opt", 
                   "name_boolformula_and", "name_boolformula_and_list", 
                   "name_boolformula_atom", "namelist", "name_var", "qcon_nowiredlist", 
                   "qcon", "gen_qcon", "con", "con_list", "sysdcon_nolist", 
                   "sysdcon", "conop", "qconop", "gconsym", "gtycon", "ntgtycon", 
                   "oqtycon", "qtyconop", "qtycon", "tycon", "qtyconsym", 
                   "tyconsym", "op", "varop", "qop", "qopm", "hole_op", 
                   "qvarop", "qvaropm", "tyvar", "tyvarop", "tyvarid", "tycls", 
                   "qtycls", "var", "qvar", "qvarid", "varid", "qvarsym", 
                   "qvarsym_no_minus", "varsym", "varsym_no_minus", "special_id", 
                   "qconid", "conid", "qconsym", "consym", "literal", "opn", 
                   "close", "semi", "modid", "commas", "bars", "special", 
                   "symbol", "ascSymbol", "integer", "pfloat", "pchar", 
                   "pstring" ]

    EOF = Token.EOF
    NEWLINE=1
    TAB=2
    WS=3
    AS=4
    CASE=5
    CLASS=6
    DATA=7
    DEFAULT=8
    DERIVING=9
    DO=10
    ELSE=11
    HIDING=12
    IF=13
    IMPORT=14
    IN=15
    INFIX=16
    INFIXL=17
    INFIXR=18
    INSTANCE=19
    LET=20
    MODULE=21
    NEWTYPE=22
    OF=23
    QUALIFIED=24
    THEN=25
    TYPE=26
    WHERE=27
    WILDCARD=28
    FORALL=29
    FOREIGN=30
    EXPORT=31
    SAFE=32
    INTERRUPTIBLE=33
    UNSAFE=34
    MDO=35
    FAMILY=36
    ROLE=37
    STDCALL=38
    CCALL=39
    CAPI=40
    CPPCALL=41
    JSCALL=42
    REC=43
    GROUP=44
    BY=45
    USING=46
    PATTERN=47
    STOCK=48
    ANYCLASS=49
    VIA=50
    LANGUAGE=51
    OPTIONS_GHC=52
    OPTIONS=53
    INLINE=54
    NOINLINE=55
    SPECIALISE=56
    SPECINLINE=57
    SOURCE=58
    RULES=59
    SCC=60
    DEPRECATED=61
    WARNING=62
    UNPACK=63
    NOUNPACK=64
    ANN=65
    MINIMAL=66
    CTYPE=67
    OVERLAPPING=68
    OVERLAPPABLE=69
    OVERLAPS=70
    INCOHERENT=71
    COMPLETE=72
    LCASE=73
    DoubleArrow=74
    DoubleColon=75
    Arrow=76
    Revarrow=77
    LarrowTail=78
    RarrowTail=79
    LLarrowTail=80
    RRarrowTail=81
    Hash=82
    Less=83
    Greater=84
    Ampersand=85
    Pipe=86
    Bang=87
    Caret=88
    Plus=89
    Minus=90
    Asterisk=91
    Percent=92
    Divide=93
    Tilde=94
    Atsign=95
    DDollar=96
    Dollar=97
    DoubleDot=98
    Dot=99
    Semi=100
    QuestionMark=101
    Comma=102
    Colon=103
    Eq=104
    Quote=105
    DoubleQuote=106
    ReverseSlash=107
    BackQuote=108
    AopenParen=109
    AcloseParen=110
    TopenTexpQuote=111
    TcloseTExpQoute=112
    TopenExpQuote=113
    TopenPatQuote=114
    TopenTypQoute=115
    TopenDecQoute=116
    TcloseQoute=117
    OpenBoxParen=118
    CloseBoxParen=119
    OpenRoundBracket=120
    CloseRoundBracket=121
    OpenSquareBracket=122
    CloseSquareBracket=123
    CHAR=124
    STRING=125
    VARID=126
    CONID=127
    OpenPragmaBracket=128
    ClosePragmaBracket=129
    COMMENT=130
    NCOMMENT=131
    OCURLY=132
    CCURLY=133
    VOCURLY=134
    VCCURLY=135
    SEMI=136
    DECIMAL=137
    OCTAL=138
    HEXADECIMAL=139
    FLOAT=140
    EXPONENT=141

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ModuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(HaskellParser.EOF, 0)

        def module_content(self):
            return self.getTypedRuleContext(HaskellParser.Module_contentContext,0)


        def body(self):
            return self.getTypedRuleContext(HaskellParser.BodyContext,0)


        def OCURLY(self):
            return self.getToken(HaskellParser.OCURLY, 0)

        def semi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.SemiContext)
            else:
                return self.getTypedRuleContext(HaskellParser.SemiContext,i)


        def pragmas(self):
            return self.getTypedRuleContext(HaskellParser.PragmasContext,0)


        def CCURLY(self):
            return self.getToken(HaskellParser.CCURLY, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_module

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModule" ):
                listener.enterModule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModule" ):
                listener.exitModule(self)




    def module(self):

        localctx = HaskellParser.ModuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HaskellParser.OCURLY:
                self.state = 512
                self.match(HaskellParser.OCURLY)


            self.state = 518
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 515
                    self.semi() 
                self.state = 520
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

            self.state = 522
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 521
                self.pragmas()


            self.state = 527
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 524
                    self.semi() 
                self.state = 529
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

            self.state = 532
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.MODULE]:
                self.state = 530
                self.module_content()
                pass
            elif token in [HaskellParser.NEWLINE, HaskellParser.AS, HaskellParser.CASE, HaskellParser.CLASS, HaskellParser.DATA, HaskellParser.DEFAULT, HaskellParser.DERIVING, HaskellParser.DO, HaskellParser.HIDING, HaskellParser.IF, HaskellParser.IMPORT, HaskellParser.INFIX, HaskellParser.INFIXL, HaskellParser.INFIXR, HaskellParser.INSTANCE, HaskellParser.LET, HaskellParser.NEWTYPE, HaskellParser.QUALIFIED, HaskellParser.TYPE, HaskellParser.WILDCARD, HaskellParser.FOREIGN, HaskellParser.EXPORT, HaskellParser.MDO, HaskellParser.STDCALL, HaskellParser.CCALL, HaskellParser.CAPI, HaskellParser.JSCALL, HaskellParser.PATTERN, HaskellParser.STOCK, HaskellParser.ANYCLASS, HaskellParser.VIA, HaskellParser.LCASE, HaskellParser.Bang, HaskellParser.Minus, HaskellParser.Tilde, HaskellParser.DDollar, HaskellParser.Dollar, HaskellParser.Semi, HaskellParser.Quote, HaskellParser.DoubleQuote, HaskellParser.ReverseSlash, HaskellParser.AopenParen, HaskellParser.TopenTexpQuote, HaskellParser.TopenExpQuote, HaskellParser.TopenPatQuote, HaskellParser.TopenTypQoute, HaskellParser.TopenDecQoute, HaskellParser.OpenBoxParen, HaskellParser.OpenRoundBracket, HaskellParser.OpenSquareBracket, HaskellParser.CHAR, HaskellParser.STRING, HaskellParser.VARID, HaskellParser.CONID, HaskellParser.OpenPragmaBracket, HaskellParser.SEMI, HaskellParser.DECIMAL, HaskellParser.OCTAL, HaskellParser.HEXADECIMAL, HaskellParser.FLOAT]:
                self.state = 531
                self.body()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 535
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HaskellParser.CCURLY:
                self.state = 534
                self.match(HaskellParser.CCURLY)


            self.state = 538
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HaskellParser.Semi or _la==HaskellParser.SEMI:
                self.state = 537
                self.semi()


            self.state = 540
            self.match(HaskellParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Module_contentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MODULE(self):
            return self.getToken(HaskellParser.MODULE, 0)

        def modid(self):
            return self.getTypedRuleContext(HaskellParser.ModidContext,0)


        def where_module(self):
            return self.getTypedRuleContext(HaskellParser.Where_moduleContext,0)


        def exports(self):
            return self.getTypedRuleContext(HaskellParser.ExportsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_module_content

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModule_content" ):
                listener.enterModule_content(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModule_content" ):
                listener.exitModule_content(self)




    def module_content(self):

        localctx = HaskellParser.Module_contentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_module_content)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.match(HaskellParser.MODULE)
            self.state = 543
            self.modid()
            self.state = 545
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HaskellParser.OpenRoundBracket:
                self.state = 544
                self.exports()


            self.state = 547
            self.where_module()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Where_moduleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(HaskellParser.WHERE, 0)

        def module_body(self):
            return self.getTypedRuleContext(HaskellParser.Module_bodyContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_where_module

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_module" ):
                listener.enterWhere_module(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_module" ):
                listener.exitWhere_module(self)




    def where_module(self):

        localctx = HaskellParser.Where_moduleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_where_module)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            self.match(HaskellParser.WHERE)
            self.state = 550
            self.module_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Module_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opn(self):
            return self.getTypedRuleContext(HaskellParser.OpnContext,0)


        def body(self):
            return self.getTypedRuleContext(HaskellParser.BodyContext,0)


        def close(self):
            return self.getTypedRuleContext(HaskellParser.CloseContext,0)


        def semi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.SemiContext)
            else:
                return self.getTypedRuleContext(HaskellParser.SemiContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_module_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModule_body" ):
                listener.enterModule_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModule_body" ):
                listener.exitModule_body(self)




    def module_body(self):

        localctx = HaskellParser.Module_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_module_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 552
            self.opn()
            self.state = 553
            self.body()
            self.state = 554
            self.close()
            self.state = 558
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 555
                    self.semi() 
                self.state = 560
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PragmasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pragma(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.PragmaContext)
            else:
                return self.getTypedRuleContext(HaskellParser.PragmaContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_pragmas

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPragmas" ):
                listener.enterPragmas(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPragmas" ):
                listener.exitPragmas(self)




    def pragmas(self):

        localctx = HaskellParser.PragmasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_pragmas)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 561
                    self.pragma()

                else:
                    raise NoViableAltException(self)
                self.state = 564 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PragmaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def language_pragma(self):
            return self.getTypedRuleContext(HaskellParser.Language_pragmaContext,0)


        def options_ghc(self):
            return self.getTypedRuleContext(HaskellParser.Options_ghcContext,0)


        def simple_options(self):
            return self.getTypedRuleContext(HaskellParser.Simple_optionsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_pragma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPragma" ):
                listener.enterPragma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPragma" ):
                listener.exitPragma(self)




    def pragma(self):

        localctx = HaskellParser.PragmaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_pragma)
        try:
            self.state = 569
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 566
                self.language_pragma()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 567
                self.options_ghc()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 568
                self.simple_options()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Language_pragmaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenPragmaBracket(self):
            return self.getToken(HaskellParser.OpenPragmaBracket, 0)

        def LANGUAGE(self):
            return self.getToken(HaskellParser.LANGUAGE, 0)

        def extension(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.ExtensionContext)
            else:
                return self.getTypedRuleContext(HaskellParser.ExtensionContext,i)


        def ClosePragmaBracket(self):
            return self.getToken(HaskellParser.ClosePragmaBracket, 0)

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Comma)
            else:
                return self.getToken(HaskellParser.Comma, i)

        def semi(self):
            return self.getTypedRuleContext(HaskellParser.SemiContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_language_pragma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLanguage_pragma" ):
                listener.enterLanguage_pragma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLanguage_pragma" ):
                listener.exitLanguage_pragma(self)




    def language_pragma(self):

        localctx = HaskellParser.Language_pragmaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_language_pragma)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 571
            self.match(HaskellParser.OpenPragmaBracket)
            self.state = 572
            self.match(HaskellParser.LANGUAGE)
            self.state = 573
            self.extension()
            self.state = 578
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Comma:
                self.state = 574
                self.match(HaskellParser.Comma)
                self.state = 575
                self.extension()
                self.state = 580
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 581
            self.match(HaskellParser.ClosePragmaBracket)
            self.state = 583
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 582
                self.semi()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Options_ghcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenPragmaBracket(self):
            return self.getToken(HaskellParser.OpenPragmaBracket, 0)

        def OPTIONS_GHC(self):
            return self.getToken(HaskellParser.OPTIONS_GHC, 0)

        def ClosePragmaBracket(self):
            return self.getToken(HaskellParser.ClosePragmaBracket, 0)

        def Minus(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Minus)
            else:
                return self.getToken(HaskellParser.Minus, i)

        def semi(self):
            return self.getTypedRuleContext(HaskellParser.SemiContext,0)


        def varid(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.VaridContext)
            else:
                return self.getTypedRuleContext(HaskellParser.VaridContext,i)


        def conid(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.ConidContext)
            else:
                return self.getTypedRuleContext(HaskellParser.ConidContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_options_ghc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptions_ghc" ):
                listener.enterOptions_ghc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptions_ghc" ):
                listener.exitOptions_ghc(self)




    def options_ghc(self):

        localctx = HaskellParser.Options_ghcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_options_ghc)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            self.match(HaskellParser.OpenPragmaBracket)
            self.state = 586
            self.match(HaskellParser.OPTIONS_GHC)
            self.state = 594
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Minus:
                self.state = 587
                self.match(HaskellParser.Minus)
                self.state = 590
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [HaskellParser.AS, HaskellParser.HIDING, HaskellParser.QUALIFIED, HaskellParser.EXPORT, HaskellParser.STDCALL, HaskellParser.CCALL, HaskellParser.CAPI, HaskellParser.JSCALL, HaskellParser.STOCK, HaskellParser.ANYCLASS, HaskellParser.VIA, HaskellParser.VARID]:
                    self.state = 588
                    self.varid()
                    pass
                elif token in [HaskellParser.CONID]:
                    self.state = 589
                    self.conid()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 596
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 597
            self.match(HaskellParser.ClosePragmaBracket)
            self.state = 599
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 598
                self.semi()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_optionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenPragmaBracket(self):
            return self.getToken(HaskellParser.OpenPragmaBracket, 0)

        def OPTIONS(self):
            return self.getToken(HaskellParser.OPTIONS, 0)

        def ClosePragmaBracket(self):
            return self.getToken(HaskellParser.ClosePragmaBracket, 0)

        def Minus(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Minus)
            else:
                return self.getToken(HaskellParser.Minus, i)

        def semi(self):
            return self.getTypedRuleContext(HaskellParser.SemiContext,0)


        def varid(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.VaridContext)
            else:
                return self.getTypedRuleContext(HaskellParser.VaridContext,i)


        def conid(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.ConidContext)
            else:
                return self.getTypedRuleContext(HaskellParser.ConidContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_simple_options

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_options" ):
                listener.enterSimple_options(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_options" ):
                listener.exitSimple_options(self)




    def simple_options(self):

        localctx = HaskellParser.Simple_optionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_simple_options)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 601
            self.match(HaskellParser.OpenPragmaBracket)
            self.state = 602
            self.match(HaskellParser.OPTIONS)
            self.state = 610
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Minus:
                self.state = 603
                self.match(HaskellParser.Minus)
                self.state = 606
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [HaskellParser.AS, HaskellParser.HIDING, HaskellParser.QUALIFIED, HaskellParser.EXPORT, HaskellParser.STDCALL, HaskellParser.CCALL, HaskellParser.CAPI, HaskellParser.JSCALL, HaskellParser.STOCK, HaskellParser.ANYCLASS, HaskellParser.VIA, HaskellParser.VARID]:
                    self.state = 604
                    self.varid()
                    pass
                elif token in [HaskellParser.CONID]:
                    self.state = 605
                    self.conid()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 612
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 613
            self.match(HaskellParser.ClosePragmaBracket)
            self.state = 615
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 614
                self.semi()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExtensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONID(self):
            return self.getToken(HaskellParser.CONID, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_extension

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtension" ):
                listener.enterExtension(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtension" ):
                listener.exitExtension(self)




    def extension(self):

        localctx = HaskellParser.ExtensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_extension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 617
            self.match(HaskellParser.CONID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def impdecls(self):
            return self.getTypedRuleContext(HaskellParser.ImpdeclsContext,0)


        def topdecls(self):
            return self.getTypedRuleContext(HaskellParser.TopdeclsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBody" ):
                listener.enterBody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBody" ):
                listener.exitBody(self)




    def body(self):

        localctx = HaskellParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_body)
        try:
            self.state = 624
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 619
                self.impdecls()
                self.state = 620
                self.topdecls()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 622
                self.impdecls()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 623
                self.topdecls()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImpdeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def impdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.ImpdeclContext)
            else:
                return self.getTypedRuleContext(HaskellParser.ImpdeclContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.NEWLINE)
            else:
                return self.getToken(HaskellParser.NEWLINE, i)

        def semi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.SemiContext)
            else:
                return self.getTypedRuleContext(HaskellParser.SemiContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_impdecls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImpdecls" ):
                listener.enterImpdecls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImpdecls" ):
                listener.exitImpdecls(self)




    def impdecls(self):

        localctx = HaskellParser.ImpdeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_impdecls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 629 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 629
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [HaskellParser.IMPORT]:
                        self.state = 626
                        self.impdecl()
                        pass
                    elif token in [HaskellParser.NEWLINE]:
                        self.state = 627
                        self.match(HaskellParser.NEWLINE)
                        pass
                    elif token in [HaskellParser.Semi, HaskellParser.SEMI]:
                        self.state = 628
                        self.semi()
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 631 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExportsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenRoundBracket(self):
            return self.getToken(HaskellParser.OpenRoundBracket, 0)

        def CloseRoundBracket(self):
            return self.getToken(HaskellParser.CloseRoundBracket, 0)

        def exprt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.ExprtContext)
            else:
                return self.getTypedRuleContext(HaskellParser.ExprtContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Comma)
            else:
                return self.getToken(HaskellParser.Comma, i)

        def getRuleIndex(self):
            return HaskellParser.RULE_exports

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExports" ):
                listener.enterExports(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExports" ):
                listener.exitExports(self)




    def exports(self):

        localctx = HaskellParser.ExportsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exports)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 633
            self.match(HaskellParser.OpenRoundBracket)
            self.state = 642
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.MODULE) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 120)) & ~0x3f) == 0 and ((1 << (_la - 120)) & ((1 << (HaskellParser.OpenRoundBracket - 120)) | (1 << (HaskellParser.VARID - 120)) | (1 << (HaskellParser.CONID - 120)))) != 0):
                self.state = 634
                self.exprt()
                self.state = 639
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 635
                        self.match(HaskellParser.Comma)
                        self.state = 636
                        self.exprt() 
                    self.state = 641
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)



            self.state = 645
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HaskellParser.Comma:
                self.state = 644
                self.match(HaskellParser.Comma)


            self.state = 647
            self.match(HaskellParser.CloseRoundBracket)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qvar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.QvarContext)
            else:
                return self.getTypedRuleContext(HaskellParser.QvarContext,i)


        def qtycon(self):
            return self.getTypedRuleContext(HaskellParser.QtyconContext,0)


        def OpenRoundBracket(self):
            return self.getToken(HaskellParser.OpenRoundBracket, 0)

        def DoubleDot(self):
            return self.getToken(HaskellParser.DoubleDot, 0)

        def CloseRoundBracket(self):
            return self.getToken(HaskellParser.CloseRoundBracket, 0)

        def cname(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.CnameContext)
            else:
                return self.getTypedRuleContext(HaskellParser.CnameContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Comma)
            else:
                return self.getToken(HaskellParser.Comma, i)

        def qtycls(self):
            return self.getTypedRuleContext(HaskellParser.QtyclsContext,0)


        def MODULE(self):
            return self.getToken(HaskellParser.MODULE, 0)

        def modid(self):
            return self.getTypedRuleContext(HaskellParser.ModidContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_exprt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprt" ):
                listener.enterExprt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprt" ):
                listener.exitExprt(self)




    def exprt(self):

        localctx = HaskellParser.ExprtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_exprt)
        self._la = 0 # Token type
        try:
            self.state = 688
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 649
                self.qvar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 650
                self.qtycon()
                self.state = 666
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 651
                    self.match(HaskellParser.OpenRoundBracket)
                    self.state = 652
                    self.match(HaskellParser.DoubleDot)
                    self.state = 653
                    self.match(HaskellParser.CloseRoundBracket)

                elif la_ == 2:
                    self.state = 654
                    self.match(HaskellParser.OpenRoundBracket)
                    self.state = 663
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 118)) & ~0x3f) == 0 and ((1 << (_la - 118)) & ((1 << (HaskellParser.OpenBoxParen - 118)) | (1 << (HaskellParser.OpenRoundBracket - 118)) | (1 << (HaskellParser.OpenSquareBracket - 118)) | (1 << (HaskellParser.VARID - 118)) | (1 << (HaskellParser.CONID - 118)))) != 0):
                        self.state = 655
                        self.cname()
                        self.state = 660
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==HaskellParser.Comma:
                            self.state = 656
                            self.match(HaskellParser.Comma)
                            self.state = 657
                            self.cname()
                            self.state = 662
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)



                    self.state = 665
                    self.match(HaskellParser.CloseRoundBracket)


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 668
                self.qtycls()
                self.state = 684
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 669
                    self.match(HaskellParser.OpenRoundBracket)
                    self.state = 670
                    self.match(HaskellParser.DoubleDot)
                    self.state = 671
                    self.match(HaskellParser.CloseRoundBracket)

                elif la_ == 2:
                    self.state = 672
                    self.match(HaskellParser.OpenRoundBracket)
                    self.state = 681
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 120)) & ~0x3f) == 0 and ((1 << (_la - 120)) & ((1 << (HaskellParser.OpenRoundBracket - 120)) | (1 << (HaskellParser.VARID - 120)) | (1 << (HaskellParser.CONID - 120)))) != 0):
                        self.state = 673
                        self.qvar()
                        self.state = 678
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==HaskellParser.Comma:
                            self.state = 674
                            self.match(HaskellParser.Comma)
                            self.state = 675
                            self.qvar()
                            self.state = 680
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)



                    self.state = 683
                    self.match(HaskellParser.CloseRoundBracket)


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 686
                self.match(HaskellParser.MODULE)
                self.state = 687
                self.modid()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImpdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(HaskellParser.IMPORT, 0)

        def modid(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.ModidContext)
            else:
                return self.getTypedRuleContext(HaskellParser.ModidContext,i)


        def QUALIFIED(self):
            return self.getToken(HaskellParser.QUALIFIED, 0)

        def AS(self):
            return self.getToken(HaskellParser.AS, 0)

        def impspec(self):
            return self.getTypedRuleContext(HaskellParser.ImpspecContext,0)


        def semi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.SemiContext)
            else:
                return self.getTypedRuleContext(HaskellParser.SemiContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_impdecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImpdecl" ):
                listener.enterImpdecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImpdecl" ):
                listener.exitImpdecl(self)




    def impdecl(self):

        localctx = HaskellParser.ImpdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_impdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 690
            self.match(HaskellParser.IMPORT)
            self.state = 692
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HaskellParser.QUALIFIED:
                self.state = 691
                self.match(HaskellParser.QUALIFIED)


            self.state = 694
            self.modid()
            self.state = 697
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HaskellParser.AS:
                self.state = 695
                self.match(HaskellParser.AS)
                self.state = 696
                self.modid()


            self.state = 700
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HaskellParser.HIDING or _la==HaskellParser.OpenRoundBracket:
                self.state = 699
                self.impspec()


            self.state = 703 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 702
                    self.semi()

                else:
                    raise NoViableAltException(self)
                self.state = 705 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImpspecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenRoundBracket(self):
            return self.getToken(HaskellParser.OpenRoundBracket, 0)

        def CloseRoundBracket(self):
            return self.getToken(HaskellParser.CloseRoundBracket, 0)

        def himport(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.HimportContext)
            else:
                return self.getTypedRuleContext(HaskellParser.HimportContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Comma)
            else:
                return self.getToken(HaskellParser.Comma, i)

        def HIDING(self):
            return self.getToken(HaskellParser.HIDING, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_impspec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImpspec" ):
                listener.enterImpspec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImpspec" ):
                listener.exitImpspec(self)




    def impspec(self):

        localctx = HaskellParser.ImpspecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_impspec)
        self._la = 0 # Token type
        try:
            self.state = 738
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.OpenRoundBracket]:
                self.enterOuterAlt(localctx, 1)
                self.state = 707
                self.match(HaskellParser.OpenRoundBracket)
                self.state = 719
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 120)) & ~0x3f) == 0 and ((1 << (_la - 120)) & ((1 << (HaskellParser.OpenRoundBracket - 120)) | (1 << (HaskellParser.VARID - 120)) | (1 << (HaskellParser.CONID - 120)))) != 0):
                    self.state = 708
                    self.himport()
                    self.state = 713
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 709
                            self.match(HaskellParser.Comma)
                            self.state = 710
                            self.himport() 
                        self.state = 715
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

                    self.state = 717
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==HaskellParser.Comma:
                        self.state = 716
                        self.match(HaskellParser.Comma)




                self.state = 721
                self.match(HaskellParser.CloseRoundBracket)
                pass
            elif token in [HaskellParser.HIDING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 722
                self.match(HaskellParser.HIDING)
                self.state = 723
                self.match(HaskellParser.OpenRoundBracket)
                self.state = 735
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 120)) & ~0x3f) == 0 and ((1 << (_la - 120)) & ((1 << (HaskellParser.OpenRoundBracket - 120)) | (1 << (HaskellParser.VARID - 120)) | (1 << (HaskellParser.CONID - 120)))) != 0):
                    self.state = 724
                    self.himport()
                    self.state = 729
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt==1:
                            self.state = 725
                            self.match(HaskellParser.Comma)
                            self.state = 726
                            self.himport() 
                        self.state = 731
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

                    self.state = 733
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==HaskellParser.Comma:
                        self.state = 732
                        self.match(HaskellParser.Comma)




                self.state = 737
                self.match(HaskellParser.CloseRoundBracket)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HimportContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(HaskellParser.VarContext,0)


        def tycon(self):
            return self.getTypedRuleContext(HaskellParser.TyconContext,0)


        def OpenRoundBracket(self):
            return self.getToken(HaskellParser.OpenRoundBracket, 0)

        def DoubleDot(self):
            return self.getToken(HaskellParser.DoubleDot, 0)

        def CloseRoundBracket(self):
            return self.getToken(HaskellParser.CloseRoundBracket, 0)

        def cname(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.CnameContext)
            else:
                return self.getTypedRuleContext(HaskellParser.CnameContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Comma)
            else:
                return self.getToken(HaskellParser.Comma, i)

        def tycls(self):
            return self.getTypedRuleContext(HaskellParser.TyclsContext,0)


        def sig_vars(self):
            return self.getTypedRuleContext(HaskellParser.Sig_varsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_himport

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHimport" ):
                listener.enterHimport(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHimport" ):
                listener.exitHimport(self)




    def himport(self):

        localctx = HaskellParser.HimportContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_himport)
        self._la = 0 # Token type
        try:
            self.state = 770
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 740
                self.var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 741
                self.tycon()
                self.state = 757
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
                if la_ == 1:
                    self.state = 742
                    self.match(HaskellParser.OpenRoundBracket)
                    self.state = 743
                    self.match(HaskellParser.DoubleDot)
                    self.state = 744
                    self.match(HaskellParser.CloseRoundBracket)

                elif la_ == 2:
                    self.state = 745
                    self.match(HaskellParser.OpenRoundBracket)
                    self.state = 754
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 118)) & ~0x3f) == 0 and ((1 << (_la - 118)) & ((1 << (HaskellParser.OpenBoxParen - 118)) | (1 << (HaskellParser.OpenRoundBracket - 118)) | (1 << (HaskellParser.OpenSquareBracket - 118)) | (1 << (HaskellParser.VARID - 118)) | (1 << (HaskellParser.CONID - 118)))) != 0):
                        self.state = 746
                        self.cname()
                        self.state = 751
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while _la==HaskellParser.Comma:
                            self.state = 747
                            self.match(HaskellParser.Comma)
                            self.state = 748
                            self.cname()
                            self.state = 753
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)



                    self.state = 756
                    self.match(HaskellParser.CloseRoundBracket)


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 759
                self.tycls()
                self.state = 768
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                if la_ == 1:
                    self.state = 760
                    self.match(HaskellParser.OpenRoundBracket)
                    self.state = 761
                    self.match(HaskellParser.DoubleDot)
                    self.state = 762
                    self.match(HaskellParser.CloseRoundBracket)

                elif la_ == 2:
                    self.state = 763
                    self.match(HaskellParser.OpenRoundBracket)
                    self.state = 765
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or _la==HaskellParser.OpenRoundBracket or _la==HaskellParser.VARID:
                        self.state = 764
                        self.sig_vars()


                    self.state = 767
                    self.match(HaskellParser.CloseRoundBracket)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CnameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(HaskellParser.VarContext,0)


        def con(self):
            return self.getTypedRuleContext(HaskellParser.ConContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_cname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCname" ):
                listener.enterCname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCname" ):
                listener.exitCname(self)




    def cname(self):

        localctx = HaskellParser.CnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_cname)
        try:
            self.state = 774
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 772
                self.var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 773
                self.con()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FixityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INFIX(self):
            return self.getToken(HaskellParser.INFIX, 0)

        def INFIXL(self):
            return self.getToken(HaskellParser.INFIXL, 0)

        def INFIXR(self):
            return self.getToken(HaskellParser.INFIXR, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_fixity

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFixity" ):
                listener.enterFixity(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFixity" ):
                listener.exitFixity(self)




    def fixity(self):

        localctx = HaskellParser.FixityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_fixity)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 776
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.INFIX) | (1 << HaskellParser.INFIXL) | (1 << HaskellParser.INFIXR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def op(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.OpContext)
            else:
                return self.getTypedRuleContext(HaskellParser.OpContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Comma)
            else:
                return self.getToken(HaskellParser.Comma, i)

        def getRuleIndex(self):
            return HaskellParser.RULE_ops

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOps" ):
                listener.enterOps(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOps" ):
                listener.exitOps(self)




    def ops(self):

        localctx = HaskellParser.OpsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_ops)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 778
            self.op()
            self.state = 783
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Comma:
                self.state = 779
                self.match(HaskellParser.Comma)
                self.state = 780
                self.op()
                self.state = 785
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopdeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def topdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.TopdeclContext)
            else:
                return self.getTypedRuleContext(HaskellParser.TopdeclContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.NEWLINE)
            else:
                return self.getToken(HaskellParser.NEWLINE, i)

        def semi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.SemiContext)
            else:
                return self.getTypedRuleContext(HaskellParser.SemiContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_topdecls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopdecls" ):
                listener.enterTopdecls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopdecls" ):
                listener.exitTopdecls(self)




    def topdecls(self):

        localctx = HaskellParser.TopdeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_topdecls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 794 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 794
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
                    if la_ == 1:
                        self.state = 786
                        self.topdecl()
                        self.state = 788 
                        self._errHandler.sync(self)
                        _alt = 1
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt == 1:
                                self.state = 787
                                self.semi()

                            else:
                                raise NoViableAltException(self)
                            self.state = 790 
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

                        pass

                    elif la_ == 2:
                        self.state = 792
                        self.match(HaskellParser.NEWLINE)
                        pass

                    elif la_ == 3:
                        self.state = 793
                        self.semi()
                        pass



                else:
                    raise NoViableAltException(self)
                self.state = 796 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,53,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TopdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cl_decl(self):
            return self.getTypedRuleContext(HaskellParser.Cl_declContext,0)


        def ty_decl(self):
            return self.getTypedRuleContext(HaskellParser.Ty_declContext,0)


        def standalone_kind_sig(self):
            return self.getTypedRuleContext(HaskellParser.Standalone_kind_sigContext,0)


        def inst_decl(self):
            return self.getTypedRuleContext(HaskellParser.Inst_declContext,0)


        def standalone_deriving(self):
            return self.getTypedRuleContext(HaskellParser.Standalone_derivingContext,0)


        def role_annot(self):
            return self.getTypedRuleContext(HaskellParser.Role_annotContext,0)


        def DEFAULT(self):
            return self.getToken(HaskellParser.DEFAULT, 0)

        def OpenRoundBracket(self):
            return self.getToken(HaskellParser.OpenRoundBracket, 0)

        def CloseRoundBracket(self):
            return self.getToken(HaskellParser.CloseRoundBracket, 0)

        def comma_types(self):
            return self.getTypedRuleContext(HaskellParser.Comma_typesContext,0)


        def FOREIGN(self):
            return self.getToken(HaskellParser.FOREIGN, 0)

        def fdecl(self):
            return self.getTypedRuleContext(HaskellParser.FdeclContext,0)


        def OpenPragmaBracket(self):
            return self.getToken(HaskellParser.OpenPragmaBracket, 0)

        def DEPRECATED(self):
            return self.getToken(HaskellParser.DEPRECATED, 0)

        def ClosePragmaBracket(self):
            return self.getToken(HaskellParser.ClosePragmaBracket, 0)

        def deprecations(self):
            return self.getTypedRuleContext(HaskellParser.DeprecationsContext,0)


        def WARNING(self):
            return self.getToken(HaskellParser.WARNING, 0)

        def warnings(self):
            return self.getTypedRuleContext(HaskellParser.WarningsContext,0)


        def RULES(self):
            return self.getToken(HaskellParser.RULES, 0)

        def rules(self):
            return self.getTypedRuleContext(HaskellParser.RulesContext,0)


        def annotation(self):
            return self.getTypedRuleContext(HaskellParser.AnnotationContext,0)


        def decl_no_th(self):
            return self.getTypedRuleContext(HaskellParser.Decl_no_thContext,0)


        def infixexp(self):
            return self.getTypedRuleContext(HaskellParser.InfixexpContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_topdecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTopdecl" ):
                listener.enterTopdecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTopdecl" ):
                listener.exitTopdecl(self)




    def topdecl(self):

        localctx = HaskellParser.TopdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_topdecl)
        self._la = 0 # Token type
        try:
            self.state = 833
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 798
                self.cl_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 799
                self.ty_decl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 800
                self.standalone_kind_sig()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 801
                self.inst_decl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 802
                self.standalone_deriving()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 803
                self.role_annot()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 804
                self.match(HaskellParser.DEFAULT)
                self.state = 805
                self.match(HaskellParser.OpenRoundBracket)
                self.state = 807
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.WILDCARD) | (1 << HaskellParser.FORALL) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 82)) & ~0x3f) == 0 and ((1 << (_la - 82)) & ((1 << (HaskellParser.Hash - 82)) | (1 << (HaskellParser.Less - 82)) | (1 << (HaskellParser.Greater - 82)) | (1 << (HaskellParser.Ampersand - 82)) | (1 << (HaskellParser.Pipe - 82)) | (1 << (HaskellParser.Bang - 82)) | (1 << (HaskellParser.Caret - 82)) | (1 << (HaskellParser.Plus - 82)) | (1 << (HaskellParser.Minus - 82)) | (1 << (HaskellParser.Asterisk - 82)) | (1 << (HaskellParser.Percent - 82)) | (1 << (HaskellParser.Divide - 82)) | (1 << (HaskellParser.Tilde - 82)) | (1 << (HaskellParser.Atsign - 82)) | (1 << (HaskellParser.Dollar - 82)) | (1 << (HaskellParser.Dot - 82)) | (1 << (HaskellParser.QuestionMark - 82)) | (1 << (HaskellParser.Colon - 82)) | (1 << (HaskellParser.Eq - 82)) | (1 << (HaskellParser.Quote - 82)) | (1 << (HaskellParser.ReverseSlash - 82)) | (1 << (HaskellParser.BackQuote - 82)) | (1 << (HaskellParser.OpenBoxParen - 82)) | (1 << (HaskellParser.OpenRoundBracket - 82)) | (1 << (HaskellParser.OpenSquareBracket - 82)) | (1 << (HaskellParser.STRING - 82)) | (1 << (HaskellParser.VARID - 82)) | (1 << (HaskellParser.CONID - 82)) | (1 << (HaskellParser.OpenPragmaBracket - 82)) | (1 << (HaskellParser.OCURLY - 82)) | (1 << (HaskellParser.DECIMAL - 82)) | (1 << (HaskellParser.OCTAL - 82)) | (1 << (HaskellParser.HEXADECIMAL - 82)))) != 0):
                    self.state = 806
                    self.comma_types()


                self.state = 809
                self.match(HaskellParser.CloseRoundBracket)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 810
                self.match(HaskellParser.FOREIGN)
                self.state = 811
                self.fdecl()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 812
                self.match(HaskellParser.OpenPragmaBracket)
                self.state = 813
                self.match(HaskellParser.DEPRECATED)
                self.state = 815
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 118)) & ~0x3f) == 0 and ((1 << (_la - 118)) & ((1 << (HaskellParser.OpenBoxParen - 118)) | (1 << (HaskellParser.OpenRoundBracket - 118)) | (1 << (HaskellParser.OpenSquareBracket - 118)) | (1 << (HaskellParser.VARID - 118)) | (1 << (HaskellParser.CONID - 118)))) != 0):
                    self.state = 814
                    self.deprecations()


                self.state = 817
                self.match(HaskellParser.ClosePragmaBracket)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 818
                self.match(HaskellParser.OpenPragmaBracket)
                self.state = 819
                self.match(HaskellParser.WARNING)
                self.state = 821
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 118)) & ~0x3f) == 0 and ((1 << (_la - 118)) & ((1 << (HaskellParser.OpenBoxParen - 118)) | (1 << (HaskellParser.OpenRoundBracket - 118)) | (1 << (HaskellParser.OpenSquareBracket - 118)) | (1 << (HaskellParser.VARID - 118)) | (1 << (HaskellParser.CONID - 118)))) != 0):
                    self.state = 820
                    self.warnings()


                self.state = 823
                self.match(HaskellParser.ClosePragmaBracket)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 824
                self.match(HaskellParser.OpenPragmaBracket)
                self.state = 825
                self.match(HaskellParser.RULES)
                self.state = 827
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.STRING:
                    self.state = 826
                    self.rules()


                self.state = 829
                self.match(HaskellParser.ClosePragmaBracket)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 830
                self.annotation()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 831
                self.decl_no_th()
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 832
                self.infixexp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cl_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(HaskellParser.CLASS, 0)

        def tycl_hdr(self):
            return self.getTypedRuleContext(HaskellParser.Tycl_hdrContext,0)


        def fds(self):
            return self.getTypedRuleContext(HaskellParser.FdsContext,0)


        def where_cls(self):
            return self.getTypedRuleContext(HaskellParser.Where_clsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_cl_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCl_decl" ):
                listener.enterCl_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCl_decl" ):
                listener.exitCl_decl(self)




    def cl_decl(self):

        localctx = HaskellParser.Cl_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_cl_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 835
            self.match(HaskellParser.CLASS)
            self.state = 836
            self.tycl_hdr()
            self.state = 838
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HaskellParser.Pipe:
                self.state = 837
                self.fds()


            self.state = 841
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HaskellParser.WHERE:
                self.state = 840
                self.where_cls()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ty_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(HaskellParser.TYPE, 0)

        def htype(self):
            return self.getTypedRuleContext(HaskellParser.HtypeContext,0)


        def Eq(self):
            return self.getToken(HaskellParser.Eq, 0)

        def ktypedoc(self):
            return self.getTypedRuleContext(HaskellParser.KtypedocContext,0)


        def FAMILY(self):
            return self.getToken(HaskellParser.FAMILY, 0)

        def opt_tyfam_kind_sig(self):
            return self.getTypedRuleContext(HaskellParser.Opt_tyfam_kind_sigContext,0)


        def opt_injective_info(self):
            return self.getTypedRuleContext(HaskellParser.Opt_injective_infoContext,0)


        def where_type_family(self):
            return self.getTypedRuleContext(HaskellParser.Where_type_familyContext,0)


        def DATA(self):
            return self.getToken(HaskellParser.DATA, 0)

        def tycl_hdr(self):
            return self.getTypedRuleContext(HaskellParser.Tycl_hdrContext,0)


        def constrs(self):
            return self.getTypedRuleContext(HaskellParser.ConstrsContext,0)


        def capi_ctype(self):
            return self.getTypedRuleContext(HaskellParser.Capi_ctypeContext,0)


        def derivings(self):
            return self.getTypedRuleContext(HaskellParser.DerivingsContext,0)


        def NEWTYPE(self):
            return self.getToken(HaskellParser.NEWTYPE, 0)

        def opt_kind_sig(self):
            return self.getTypedRuleContext(HaskellParser.Opt_kind_sigContext,0)


        def gadt_constrlist(self):
            return self.getTypedRuleContext(HaskellParser.Gadt_constrlistContext,0)


        def opt_datafam_kind_sig(self):
            return self.getTypedRuleContext(HaskellParser.Opt_datafam_kind_sigContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_ty_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTy_decl" ):
                listener.enterTy_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTy_decl" ):
                listener.exitTy_decl(self)




    def ty_decl(self):

        localctx = HaskellParser.Ty_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_ty_decl)
        self._la = 0 # Token type
        try:
            self.state = 912
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,77,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 843
                self.match(HaskellParser.TYPE)
                self.state = 844
                self.htype()
                self.state = 845
                self.match(HaskellParser.Eq)
                self.state = 846
                self.ktypedoc()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 848
                self.match(HaskellParser.TYPE)
                self.state = 849
                self.match(HaskellParser.FAMILY)
                self.state = 850
                self.htype()
                self.state = 852
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.DoubleColon or _la==HaskellParser.Eq:
                    self.state = 851
                    self.opt_tyfam_kind_sig()


                self.state = 855
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.Pipe:
                    self.state = 854
                    self.opt_injective_info()


                self.state = 858
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.WHERE:
                    self.state = 857
                    self.where_type_family()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 860
                self.match(HaskellParser.DATA)
                self.state = 862
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
                if la_ == 1:
                    self.state = 861
                    self.capi_ctype()


                self.state = 864
                self.tycl_hdr()
                self.state = 865
                self.constrs()
                self.state = 867
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.DERIVING:
                    self.state = 866
                    self.derivings()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 869
                self.match(HaskellParser.NEWTYPE)
                self.state = 871
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
                if la_ == 1:
                    self.state = 870
                    self.capi_ctype()


                self.state = 873
                self.tycl_hdr()
                self.state = 874
                self.constrs()
                self.state = 876
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.DERIVING:
                    self.state = 875
                    self.derivings()


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 878
                self.match(HaskellParser.DATA)
                self.state = 880
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
                if la_ == 1:
                    self.state = 879
                    self.capi_ctype()


                self.state = 882
                self.tycl_hdr()
                self.state = 884
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.DoubleColon:
                    self.state = 883
                    self.opt_kind_sig()


                self.state = 887
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.WHERE:
                    self.state = 886
                    self.gadt_constrlist()


                self.state = 890
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.DERIVING:
                    self.state = 889
                    self.derivings()


                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 892
                self.match(HaskellParser.NEWTYPE)
                self.state = 894
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,72,self._ctx)
                if la_ == 1:
                    self.state = 893
                    self.capi_ctype()


                self.state = 896
                self.tycl_hdr()
                self.state = 898
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.DoubleColon:
                    self.state = 897
                    self.opt_kind_sig()


                self.state = 901
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.WHERE:
                    self.state = 900
                    self.gadt_constrlist()


                self.state = 904
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.DERIVING:
                    self.state = 903
                    self.derivings()


                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 906
                self.match(HaskellParser.DATA)
                self.state = 907
                self.match(HaskellParser.FAMILY)
                self.state = 908
                self.htype()
                self.state = 910
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.DoubleColon:
                    self.state = 909
                    self.opt_datafam_kind_sig()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Standalone_kind_sigContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(HaskellParser.TYPE, 0)

        def sks_vars(self):
            return self.getTypedRuleContext(HaskellParser.Sks_varsContext,0)


        def DoubleColon(self):
            return self.getToken(HaskellParser.DoubleColon, 0)

        def ktypedoc(self):
            return self.getTypedRuleContext(HaskellParser.KtypedocContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_standalone_kind_sig

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStandalone_kind_sig" ):
                listener.enterStandalone_kind_sig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStandalone_kind_sig" ):
                listener.exitStandalone_kind_sig(self)




    def standalone_kind_sig(self):

        localctx = HaskellParser.Standalone_kind_sigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_standalone_kind_sig)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 914
            self.match(HaskellParser.TYPE)
            self.state = 915
            self.sks_vars()
            self.state = 916
            self.match(HaskellParser.DoubleColon)
            self.state = 917
            self.ktypedoc()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sks_varsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def oqtycon(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.OqtyconContext)
            else:
                return self.getTypedRuleContext(HaskellParser.OqtyconContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Comma)
            else:
                return self.getToken(HaskellParser.Comma, i)

        def getRuleIndex(self):
            return HaskellParser.RULE_sks_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSks_vars" ):
                listener.enterSks_vars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSks_vars" ):
                listener.exitSks_vars(self)




    def sks_vars(self):

        localctx = HaskellParser.Sks_varsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_sks_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 919
            self.oqtycon()
            self.state = 924
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Comma:
                self.state = 920
                self.match(HaskellParser.Comma)
                self.state = 921
                self.oqtycon()
                self.state = 926
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inst_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSTANCE(self):
            return self.getToken(HaskellParser.INSTANCE, 0)

        def inst_type(self):
            return self.getTypedRuleContext(HaskellParser.Inst_typeContext,0)


        def overlap_pragma(self):
            return self.getTypedRuleContext(HaskellParser.Overlap_pragmaContext,0)


        def where_inst(self):
            return self.getTypedRuleContext(HaskellParser.Where_instContext,0)


        def TYPE(self):
            return self.getToken(HaskellParser.TYPE, 0)

        def ty_fam_inst_eqn(self):
            return self.getTypedRuleContext(HaskellParser.Ty_fam_inst_eqnContext,0)


        def DATA(self):
            return self.getToken(HaskellParser.DATA, 0)

        def tycl_hdr_inst(self):
            return self.getTypedRuleContext(HaskellParser.Tycl_hdr_instContext,0)


        def capi_ctype(self):
            return self.getTypedRuleContext(HaskellParser.Capi_ctypeContext,0)


        def derivings(self):
            return self.getTypedRuleContext(HaskellParser.DerivingsContext,0)


        def NEWTYPE(self):
            return self.getToken(HaskellParser.NEWTYPE, 0)

        def opt_kind_sig(self):
            return self.getTypedRuleContext(HaskellParser.Opt_kind_sigContext,0)


        def gadt_constrlist(self):
            return self.getTypedRuleContext(HaskellParser.Gadt_constrlistContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_inst_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInst_decl" ):
                listener.enterInst_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInst_decl" ):
                listener.exitInst_decl(self)




    def inst_decl(self):

        localctx = HaskellParser.Inst_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_inst_decl)
        self._la = 0 # Token type
        try:
            self.state = 986
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,93,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 927
                self.match(HaskellParser.INSTANCE)
                self.state = 929
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
                if la_ == 1:
                    self.state = 928
                    self.overlap_pragma()


                self.state = 931
                self.inst_type()
                self.state = 933
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.WHERE:
                    self.state = 932
                    self.where_inst()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 935
                self.match(HaskellParser.TYPE)
                self.state = 936
                self.match(HaskellParser.INSTANCE)
                self.state = 937
                self.ty_fam_inst_eqn()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 938
                self.match(HaskellParser.DATA)
                self.state = 939
                self.match(HaskellParser.INSTANCE)
                self.state = 941
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,81,self._ctx)
                if la_ == 1:
                    self.state = 940
                    self.capi_ctype()


                self.state = 943
                self.tycl_hdr_inst()
                self.state = 945
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.DERIVING:
                    self.state = 944
                    self.derivings()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 947
                self.match(HaskellParser.NEWTYPE)
                self.state = 948
                self.match(HaskellParser.INSTANCE)
                self.state = 950
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,83,self._ctx)
                if la_ == 1:
                    self.state = 949
                    self.capi_ctype()


                self.state = 952
                self.tycl_hdr_inst()
                self.state = 954
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.DERIVING:
                    self.state = 953
                    self.derivings()


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 956
                self.match(HaskellParser.DATA)
                self.state = 957
                self.match(HaskellParser.INSTANCE)
                self.state = 959
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,85,self._ctx)
                if la_ == 1:
                    self.state = 958
                    self.capi_ctype()


                self.state = 961
                self.tycl_hdr_inst()
                self.state = 963
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.DoubleColon:
                    self.state = 962
                    self.opt_kind_sig()


                self.state = 966
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.WHERE:
                    self.state = 965
                    self.gadt_constrlist()


                self.state = 969
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.DERIVING:
                    self.state = 968
                    self.derivings()


                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 971
                self.match(HaskellParser.NEWTYPE)
                self.state = 972
                self.match(HaskellParser.INSTANCE)
                self.state = 974
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,89,self._ctx)
                if la_ == 1:
                    self.state = 973
                    self.capi_ctype()


                self.state = 976
                self.tycl_hdr_inst()
                self.state = 978
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.DoubleColon:
                    self.state = 977
                    self.opt_kind_sig()


                self.state = 981
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.WHERE:
                    self.state = 980
                    self.gadt_constrlist()


                self.state = 984
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.DERIVING:
                    self.state = 983
                    self.derivings()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Overlap_pragmaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenPragmaBracket(self):
            return self.getToken(HaskellParser.OpenPragmaBracket, 0)

        def OVERLAPPABLE(self):
            return self.getToken(HaskellParser.OVERLAPPABLE, 0)

        def ClosePragmaBracket(self):
            return self.getToken(HaskellParser.ClosePragmaBracket, 0)

        def OVERLAPPING(self):
            return self.getToken(HaskellParser.OVERLAPPING, 0)

        def OVERLAPS(self):
            return self.getToken(HaskellParser.OVERLAPS, 0)

        def INCOHERENT(self):
            return self.getToken(HaskellParser.INCOHERENT, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_overlap_pragma

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOverlap_pragma" ):
                listener.enterOverlap_pragma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOverlap_pragma" ):
                listener.exitOverlap_pragma(self)




    def overlap_pragma(self):

        localctx = HaskellParser.Overlap_pragmaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_overlap_pragma)
        try:
            self.state = 1000
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,94,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 988
                self.match(HaskellParser.OpenPragmaBracket)
                self.state = 989
                self.match(HaskellParser.OVERLAPPABLE)
                self.state = 990
                self.match(HaskellParser.ClosePragmaBracket)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 991
                self.match(HaskellParser.OpenPragmaBracket)
                self.state = 992
                self.match(HaskellParser.OVERLAPPING)
                self.state = 993
                self.match(HaskellParser.ClosePragmaBracket)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 994
                self.match(HaskellParser.OpenPragmaBracket)
                self.state = 995
                self.match(HaskellParser.OVERLAPS)
                self.state = 996
                self.match(HaskellParser.ClosePragmaBracket)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 997
                self.match(HaskellParser.OpenPragmaBracket)
                self.state = 998
                self.match(HaskellParser.INCOHERENT)
                self.state = 999
                self.match(HaskellParser.ClosePragmaBracket)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Deriv_strategy_no_viaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STOCK(self):
            return self.getToken(HaskellParser.STOCK, 0)

        def ANYCLASS(self):
            return self.getToken(HaskellParser.ANYCLASS, 0)

        def NEWTYPE(self):
            return self.getToken(HaskellParser.NEWTYPE, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_deriv_strategy_no_via

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeriv_strategy_no_via" ):
                listener.enterDeriv_strategy_no_via(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeriv_strategy_no_via" ):
                listener.exitDeriv_strategy_no_via(self)




    def deriv_strategy_no_via(self):

        localctx = HaskellParser.Deriv_strategy_no_viaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_deriv_strategy_no_via)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1002
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.NEWTYPE) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Deriv_strategy_viaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VIA(self):
            return self.getToken(HaskellParser.VIA, 0)

        def ktype(self):
            return self.getTypedRuleContext(HaskellParser.KtypeContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_deriv_strategy_via

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeriv_strategy_via" ):
                listener.enterDeriv_strategy_via(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeriv_strategy_via" ):
                listener.exitDeriv_strategy_via(self)




    def deriv_strategy_via(self):

        localctx = HaskellParser.Deriv_strategy_viaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_deriv_strategy_via)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1004
            self.match(HaskellParser.VIA)
            self.state = 1005
            self.ktype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Deriv_standalone_strategyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STOCK(self):
            return self.getToken(HaskellParser.STOCK, 0)

        def ANYCLASS(self):
            return self.getToken(HaskellParser.ANYCLASS, 0)

        def NEWTYPE(self):
            return self.getToken(HaskellParser.NEWTYPE, 0)

        def deriv_strategy_via(self):
            return self.getTypedRuleContext(HaskellParser.Deriv_strategy_viaContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_deriv_standalone_strategy

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeriv_standalone_strategy" ):
                listener.enterDeriv_standalone_strategy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeriv_standalone_strategy" ):
                listener.exitDeriv_standalone_strategy(self)




    def deriv_standalone_strategy(self):

        localctx = HaskellParser.Deriv_standalone_strategyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_deriv_standalone_strategy)
        try:
            self.state = 1011
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.STOCK]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1007
                self.match(HaskellParser.STOCK)
                pass
            elif token in [HaskellParser.ANYCLASS]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1008
                self.match(HaskellParser.ANYCLASS)
                pass
            elif token in [HaskellParser.NEWTYPE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1009
                self.match(HaskellParser.NEWTYPE)
                pass
            elif token in [HaskellParser.VIA]:
                self.enterOuterAlt(localctx, 4)
                self.state = 1010
                self.deriv_strategy_via()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Opt_injective_infoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Pipe(self):
            return self.getToken(HaskellParser.Pipe, 0)

        def injectivity_cond(self):
            return self.getTypedRuleContext(HaskellParser.Injectivity_condContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_opt_injective_info

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpt_injective_info" ):
                listener.enterOpt_injective_info(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpt_injective_info" ):
                listener.exitOpt_injective_info(self)




    def opt_injective_info(self):

        localctx = HaskellParser.Opt_injective_infoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_opt_injective_info)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1013
            self.match(HaskellParser.Pipe)
            self.state = 1014
            self.injectivity_cond()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Injectivity_condContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tyvarid(self):
            return self.getTypedRuleContext(HaskellParser.TyvaridContext,0)


        def Arrow(self):
            return self.getToken(HaskellParser.Arrow, 0)

        def inj_varids(self):
            return self.getTypedRuleContext(HaskellParser.Inj_varidsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_injectivity_cond

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInjectivity_cond" ):
                listener.enterInjectivity_cond(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInjectivity_cond" ):
                listener.exitInjectivity_cond(self)




    def injectivity_cond(self):

        localctx = HaskellParser.Injectivity_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_injectivity_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1016
            self.tyvarid()
            self.state = 1017
            self.match(HaskellParser.Arrow)
            self.state = 1018
            self.inj_varids()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inj_varidsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tyvarid(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.TyvaridContext)
            else:
                return self.getTypedRuleContext(HaskellParser.TyvaridContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_inj_varids

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInj_varids" ):
                listener.enterInj_varids(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInj_varids" ):
                listener.exitInj_varids(self)




    def inj_varids(self):

        localctx = HaskellParser.Inj_varidsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_inj_varids)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1021 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1020
                self.tyvarid()
                self.state = 1023 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.SAFE) | (1 << HaskellParser.INTERRUPTIBLE) | (1 << HaskellParser.UNSAFE) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or _la==HaskellParser.VARID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Where_type_familyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(HaskellParser.WHERE, 0)

        def ty_fam_inst_eqn_list(self):
            return self.getTypedRuleContext(HaskellParser.Ty_fam_inst_eqn_listContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_where_type_family

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_type_family" ):
                listener.enterWhere_type_family(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_type_family" ):
                listener.exitWhere_type_family(self)




    def where_type_family(self):

        localctx = HaskellParser.Where_type_familyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_where_type_family)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1025
            self.match(HaskellParser.WHERE)
            self.state = 1026
            self.ty_fam_inst_eqn_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ty_fam_inst_eqn_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opn(self):
            return self.getTypedRuleContext(HaskellParser.OpnContext,0)


        def close(self):
            return self.getTypedRuleContext(HaskellParser.CloseContext,0)


        def ty_fam_inst_eqns(self):
            return self.getTypedRuleContext(HaskellParser.Ty_fam_inst_eqnsContext,0)


        def OCURLY(self):
            return self.getToken(HaskellParser.OCURLY, 0)

        def DoubleDot(self):
            return self.getToken(HaskellParser.DoubleDot, 0)

        def CCURLY(self):
            return self.getToken(HaskellParser.CCURLY, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_ty_fam_inst_eqn_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTy_fam_inst_eqn_list" ):
                listener.enterTy_fam_inst_eqn_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTy_fam_inst_eqn_list" ):
                listener.exitTy_fam_inst_eqn_list(self)




    def ty_fam_inst_eqn_list(self):

        localctx = HaskellParser.Ty_fam_inst_eqn_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_ty_fam_inst_eqn_list)
        self._la = 0 # Token type
        try:
            self.state = 1041
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,98,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1028
                self.opn()
                self.state = 1030
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.WILDCARD) | (1 << HaskellParser.FORALL) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 82)) & ~0x3f) == 0 and ((1 << (_la - 82)) & ((1 << (HaskellParser.Hash - 82)) | (1 << (HaskellParser.Less - 82)) | (1 << (HaskellParser.Greater - 82)) | (1 << (HaskellParser.Ampersand - 82)) | (1 << (HaskellParser.Pipe - 82)) | (1 << (HaskellParser.Bang - 82)) | (1 << (HaskellParser.Caret - 82)) | (1 << (HaskellParser.Plus - 82)) | (1 << (HaskellParser.Minus - 82)) | (1 << (HaskellParser.Asterisk - 82)) | (1 << (HaskellParser.Percent - 82)) | (1 << (HaskellParser.Divide - 82)) | (1 << (HaskellParser.Tilde - 82)) | (1 << (HaskellParser.Atsign - 82)) | (1 << (HaskellParser.Dollar - 82)) | (1 << (HaskellParser.Dot - 82)) | (1 << (HaskellParser.QuestionMark - 82)) | (1 << (HaskellParser.Colon - 82)) | (1 << (HaskellParser.Eq - 82)) | (1 << (HaskellParser.Quote - 82)) | (1 << (HaskellParser.ReverseSlash - 82)) | (1 << (HaskellParser.BackQuote - 82)) | (1 << (HaskellParser.OpenBoxParen - 82)) | (1 << (HaskellParser.OpenRoundBracket - 82)) | (1 << (HaskellParser.OpenSquareBracket - 82)) | (1 << (HaskellParser.STRING - 82)) | (1 << (HaskellParser.VARID - 82)) | (1 << (HaskellParser.CONID - 82)) | (1 << (HaskellParser.OpenPragmaBracket - 82)) | (1 << (HaskellParser.OCURLY - 82)) | (1 << (HaskellParser.DECIMAL - 82)) | (1 << (HaskellParser.OCTAL - 82)) | (1 << (HaskellParser.HEXADECIMAL - 82)))) != 0):
                    self.state = 1029
                    self.ty_fam_inst_eqns()


                self.state = 1032
                self.close()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1034
                self.match(HaskellParser.OCURLY)
                self.state = 1035
                self.match(HaskellParser.DoubleDot)
                self.state = 1036
                self.match(HaskellParser.CCURLY)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1037
                self.opn()
                self.state = 1038
                self.match(HaskellParser.DoubleDot)
                self.state = 1039
                self.close()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ty_fam_inst_eqnsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ty_fam_inst_eqn(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.Ty_fam_inst_eqnContext)
            else:
                return self.getTypedRuleContext(HaskellParser.Ty_fam_inst_eqnContext,i)


        def semi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.SemiContext)
            else:
                return self.getTypedRuleContext(HaskellParser.SemiContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_ty_fam_inst_eqns

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTy_fam_inst_eqns" ):
                listener.enterTy_fam_inst_eqns(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTy_fam_inst_eqns" ):
                listener.exitTy_fam_inst_eqns(self)




    def ty_fam_inst_eqns(self):

        localctx = HaskellParser.Ty_fam_inst_eqnsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_ty_fam_inst_eqns)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1043
            self.ty_fam_inst_eqn()
            self.state = 1053
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,100,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1045 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 1044
                        self.semi()
                        self.state = 1047 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==HaskellParser.Semi or _la==HaskellParser.SEMI):
                            break

                    self.state = 1049
                    self.ty_fam_inst_eqn() 
                self.state = 1055
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,100,self._ctx)

            self.state = 1059
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Semi or _la==HaskellParser.SEMI:
                self.state = 1056
                self.semi()
                self.state = 1061
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ty_fam_inst_eqnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FORALL(self):
            return self.getToken(HaskellParser.FORALL, 0)

        def Dot(self):
            return self.getToken(HaskellParser.Dot, 0)

        def htype(self):
            return self.getTypedRuleContext(HaskellParser.HtypeContext,0)


        def Eq(self):
            return self.getToken(HaskellParser.Eq, 0)

        def ktype(self):
            return self.getTypedRuleContext(HaskellParser.KtypeContext,0)


        def tv_bndrs(self):
            return self.getTypedRuleContext(HaskellParser.Tv_bndrsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_ty_fam_inst_eqn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTy_fam_inst_eqn" ):
                listener.enterTy_fam_inst_eqn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTy_fam_inst_eqn" ):
                listener.exitTy_fam_inst_eqn(self)




    def ty_fam_inst_eqn(self):

        localctx = HaskellParser.Ty_fam_inst_eqnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_ty_fam_inst_eqn)
        self._la = 0 # Token type
        try:
            self.state = 1075
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.FORALL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1062
                self.match(HaskellParser.FORALL)
                self.state = 1064
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 120)) & ~0x3f) == 0 and ((1 << (_la - 120)) & ((1 << (HaskellParser.OpenRoundBracket - 120)) | (1 << (HaskellParser.VARID - 120)) | (1 << (HaskellParser.OCURLY - 120)))) != 0):
                    self.state = 1063
                    self.tv_bndrs()


                self.state = 1066
                self.match(HaskellParser.Dot)
                self.state = 1067
                self.htype()
                self.state = 1068
                self.match(HaskellParser.Eq)
                self.state = 1069
                self.ktype()
                pass
            elif token in [HaskellParser.AS, HaskellParser.HIDING, HaskellParser.QUALIFIED, HaskellParser.WILDCARD, HaskellParser.EXPORT, HaskellParser.STDCALL, HaskellParser.CCALL, HaskellParser.CAPI, HaskellParser.JSCALL, HaskellParser.STOCK, HaskellParser.ANYCLASS, HaskellParser.VIA, HaskellParser.Hash, HaskellParser.Less, HaskellParser.Greater, HaskellParser.Ampersand, HaskellParser.Pipe, HaskellParser.Bang, HaskellParser.Caret, HaskellParser.Plus, HaskellParser.Minus, HaskellParser.Asterisk, HaskellParser.Percent, HaskellParser.Divide, HaskellParser.Tilde, HaskellParser.Atsign, HaskellParser.Dollar, HaskellParser.Dot, HaskellParser.QuestionMark, HaskellParser.Colon, HaskellParser.Eq, HaskellParser.Quote, HaskellParser.ReverseSlash, HaskellParser.BackQuote, HaskellParser.OpenBoxParen, HaskellParser.OpenRoundBracket, HaskellParser.OpenSquareBracket, HaskellParser.STRING, HaskellParser.VARID, HaskellParser.CONID, HaskellParser.OpenPragmaBracket, HaskellParser.OCURLY, HaskellParser.DECIMAL, HaskellParser.OCTAL, HaskellParser.HEXADECIMAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1071
                self.htype()
                self.state = 1072
                self.match(HaskellParser.Eq)
                self.state = 1073
                self.ktype()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class At_decl_clsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DATA(self):
            return self.getToken(HaskellParser.DATA, 0)

        def htype(self):
            return self.getTypedRuleContext(HaskellParser.HtypeContext,0)


        def FAMILY(self):
            return self.getToken(HaskellParser.FAMILY, 0)

        def opt_datafam_kind_sig(self):
            return self.getTypedRuleContext(HaskellParser.Opt_datafam_kind_sigContext,0)


        def TYPE(self):
            return self.getToken(HaskellParser.TYPE, 0)

        def opt_at_kind_inj_sig(self):
            return self.getTypedRuleContext(HaskellParser.Opt_at_kind_inj_sigContext,0)


        def ty_fam_inst_eqn(self):
            return self.getTypedRuleContext(HaskellParser.Ty_fam_inst_eqnContext,0)


        def INSTANCE(self):
            return self.getToken(HaskellParser.INSTANCE, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_at_decl_cls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAt_decl_cls" ):
                listener.enterAt_decl_cls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAt_decl_cls" ):
                listener.exitAt_decl_cls(self)




    def at_decl_cls(self):

        localctx = HaskellParser.At_decl_clsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_at_decl_cls)
        self._la = 0 # Token type
        try:
            self.state = 1098
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,109,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1077
                self.match(HaskellParser.DATA)
                self.state = 1079
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.FAMILY:
                    self.state = 1078
                    self.match(HaskellParser.FAMILY)


                self.state = 1081
                self.htype()
                self.state = 1083
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.DoubleColon:
                    self.state = 1082
                    self.opt_datafam_kind_sig()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1085
                self.match(HaskellParser.TYPE)
                self.state = 1087
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.FAMILY:
                    self.state = 1086
                    self.match(HaskellParser.FAMILY)


                self.state = 1089
                self.htype()
                self.state = 1091
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.DoubleColon or _la==HaskellParser.Eq:
                    self.state = 1090
                    self.opt_at_kind_inj_sig()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1093
                self.match(HaskellParser.TYPE)
                self.state = 1095
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.INSTANCE:
                    self.state = 1094
                    self.match(HaskellParser.INSTANCE)


                self.state = 1097
                self.ty_fam_inst_eqn()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class At_decl_instContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(HaskellParser.TYPE, 0)

        def ty_fam_inst_eqn(self):
            return self.getTypedRuleContext(HaskellParser.Ty_fam_inst_eqnContext,0)


        def INSTANCE(self):
            return self.getToken(HaskellParser.INSTANCE, 0)

        def DATA(self):
            return self.getToken(HaskellParser.DATA, 0)

        def tycl_hdr_inst(self):
            return self.getTypedRuleContext(HaskellParser.Tycl_hdr_instContext,0)


        def constrs(self):
            return self.getTypedRuleContext(HaskellParser.ConstrsContext,0)


        def capi_ctype(self):
            return self.getTypedRuleContext(HaskellParser.Capi_ctypeContext,0)


        def derivings(self):
            return self.getTypedRuleContext(HaskellParser.DerivingsContext,0)


        def NEWTYPE(self):
            return self.getToken(HaskellParser.NEWTYPE, 0)

        def opt_kind_sig(self):
            return self.getTypedRuleContext(HaskellParser.Opt_kind_sigContext,0)


        def gadt_constrlist(self):
            return self.getTypedRuleContext(HaskellParser.Gadt_constrlistContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_at_decl_inst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAt_decl_inst" ):
                listener.enterAt_decl_inst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAt_decl_inst" ):
                listener.exitAt_decl_inst(self)




    def at_decl_inst(self):

        localctx = HaskellParser.At_decl_instContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_at_decl_inst)
        self._la = 0 # Token type
        try:
            self.state = 1163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,127,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1100
                self.match(HaskellParser.TYPE)
                self.state = 1102
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.INSTANCE:
                    self.state = 1101
                    self.match(HaskellParser.INSTANCE)


                self.state = 1104
                self.ty_fam_inst_eqn()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1105
                self.match(HaskellParser.DATA)
                self.state = 1107
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.INSTANCE:
                    self.state = 1106
                    self.match(HaskellParser.INSTANCE)


                self.state = 1110
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,112,self._ctx)
                if la_ == 1:
                    self.state = 1109
                    self.capi_ctype()


                self.state = 1112
                self.tycl_hdr_inst()
                self.state = 1113
                self.constrs()
                self.state = 1115
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.DERIVING:
                    self.state = 1114
                    self.derivings()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1117
                self.match(HaskellParser.NEWTYPE)
                self.state = 1119
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.INSTANCE:
                    self.state = 1118
                    self.match(HaskellParser.INSTANCE)


                self.state = 1122
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,115,self._ctx)
                if la_ == 1:
                    self.state = 1121
                    self.capi_ctype()


                self.state = 1124
                self.tycl_hdr_inst()
                self.state = 1125
                self.constrs()
                self.state = 1127
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.DERIVING:
                    self.state = 1126
                    self.derivings()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1129
                self.match(HaskellParser.DATA)
                self.state = 1131
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.INSTANCE:
                    self.state = 1130
                    self.match(HaskellParser.INSTANCE)


                self.state = 1134
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,118,self._ctx)
                if la_ == 1:
                    self.state = 1133
                    self.capi_ctype()


                self.state = 1136
                self.tycl_hdr_inst()
                self.state = 1138
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.DoubleColon:
                    self.state = 1137
                    self.opt_kind_sig()


                self.state = 1141
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.WHERE:
                    self.state = 1140
                    self.gadt_constrlist()


                self.state = 1144
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.DERIVING:
                    self.state = 1143
                    self.derivings()


                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1146
                self.match(HaskellParser.NEWTYPE)
                self.state = 1148
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.INSTANCE:
                    self.state = 1147
                    self.match(HaskellParser.INSTANCE)


                self.state = 1151
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,123,self._ctx)
                if la_ == 1:
                    self.state = 1150
                    self.capi_ctype()


                self.state = 1153
                self.tycl_hdr_inst()
                self.state = 1155
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.DoubleColon:
                    self.state = 1154
                    self.opt_kind_sig()


                self.state = 1158
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.WHERE:
                    self.state = 1157
                    self.gadt_constrlist()


                self.state = 1161
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.DERIVING:
                    self.state = 1160
                    self.derivings()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Opt_kind_sigContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DoubleColon(self):
            return self.getToken(HaskellParser.DoubleColon, 0)

        def kind(self):
            return self.getTypedRuleContext(HaskellParser.KindContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_opt_kind_sig

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpt_kind_sig" ):
                listener.enterOpt_kind_sig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpt_kind_sig" ):
                listener.exitOpt_kind_sig(self)




    def opt_kind_sig(self):

        localctx = HaskellParser.Opt_kind_sigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_opt_kind_sig)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1165
            self.match(HaskellParser.DoubleColon)
            self.state = 1166
            self.kind()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Opt_datafam_kind_sigContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DoubleColon(self):
            return self.getToken(HaskellParser.DoubleColon, 0)

        def kind(self):
            return self.getTypedRuleContext(HaskellParser.KindContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_opt_datafam_kind_sig

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpt_datafam_kind_sig" ):
                listener.enterOpt_datafam_kind_sig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpt_datafam_kind_sig" ):
                listener.exitOpt_datafam_kind_sig(self)




    def opt_datafam_kind_sig(self):

        localctx = HaskellParser.Opt_datafam_kind_sigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_opt_datafam_kind_sig)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1168
            self.match(HaskellParser.DoubleColon)
            self.state = 1169
            self.kind()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Opt_tyfam_kind_sigContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DoubleColon(self):
            return self.getToken(HaskellParser.DoubleColon, 0)

        def kind(self):
            return self.getTypedRuleContext(HaskellParser.KindContext,0)


        def Eq(self):
            return self.getToken(HaskellParser.Eq, 0)

        def tv_bndr(self):
            return self.getTypedRuleContext(HaskellParser.Tv_bndrContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_opt_tyfam_kind_sig

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpt_tyfam_kind_sig" ):
                listener.enterOpt_tyfam_kind_sig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpt_tyfam_kind_sig" ):
                listener.exitOpt_tyfam_kind_sig(self)




    def opt_tyfam_kind_sig(self):

        localctx = HaskellParser.Opt_tyfam_kind_sigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_opt_tyfam_kind_sig)
        try:
            self.state = 1175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.DoubleColon]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1171
                self.match(HaskellParser.DoubleColon)
                self.state = 1172
                self.kind()
                pass
            elif token in [HaskellParser.Eq]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1173
                self.match(HaskellParser.Eq)
                self.state = 1174
                self.tv_bndr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Opt_at_kind_inj_sigContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DoubleColon(self):
            return self.getToken(HaskellParser.DoubleColon, 0)

        def kind(self):
            return self.getTypedRuleContext(HaskellParser.KindContext,0)


        def Eq(self):
            return self.getToken(HaskellParser.Eq, 0)

        def tv_bndr_no_braces(self):
            return self.getTypedRuleContext(HaskellParser.Tv_bndr_no_bracesContext,0)


        def Pipe(self):
            return self.getToken(HaskellParser.Pipe, 0)

        def injectivity_cond(self):
            return self.getTypedRuleContext(HaskellParser.Injectivity_condContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_opt_at_kind_inj_sig

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpt_at_kind_inj_sig" ):
                listener.enterOpt_at_kind_inj_sig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpt_at_kind_inj_sig" ):
                listener.exitOpt_at_kind_inj_sig(self)




    def opt_at_kind_inj_sig(self):

        localctx = HaskellParser.Opt_at_kind_inj_sigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_opt_at_kind_inj_sig)
        try:
            self.state = 1184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.DoubleColon]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1177
                self.match(HaskellParser.DoubleColon)
                self.state = 1178
                self.kind()
                pass
            elif token in [HaskellParser.Eq]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1179
                self.match(HaskellParser.Eq)
                self.state = 1180
                self.tv_bndr_no_braces()
                self.state = 1181
                self.match(HaskellParser.Pipe)
                self.state = 1182
                self.injectivity_cond()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tycl_hdrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tycl_context(self):
            return self.getTypedRuleContext(HaskellParser.Tycl_contextContext,0)


        def DoubleArrow(self):
            return self.getToken(HaskellParser.DoubleArrow, 0)

        def htype(self):
            return self.getTypedRuleContext(HaskellParser.HtypeContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_tycl_hdr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTycl_hdr" ):
                listener.enterTycl_hdr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTycl_hdr" ):
                listener.exitTycl_hdr(self)




    def tycl_hdr(self):

        localctx = HaskellParser.Tycl_hdrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_tycl_hdr)
        try:
            self.state = 1191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,130,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1186
                self.tycl_context()
                self.state = 1187
                self.match(HaskellParser.DoubleArrow)
                self.state = 1188
                self.htype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1190
                self.htype()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tycl_hdr_instContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FORALL(self):
            return self.getToken(HaskellParser.FORALL, 0)

        def Dot(self):
            return self.getToken(HaskellParser.Dot, 0)

        def tycl_context(self):
            return self.getTypedRuleContext(HaskellParser.Tycl_contextContext,0)


        def DoubleArrow(self):
            return self.getToken(HaskellParser.DoubleArrow, 0)

        def htype(self):
            return self.getTypedRuleContext(HaskellParser.HtypeContext,0)


        def tv_bndrs(self):
            return self.getTypedRuleContext(HaskellParser.Tv_bndrsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_tycl_hdr_inst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTycl_hdr_inst" ):
                listener.enterTycl_hdr_inst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTycl_hdr_inst" ):
                listener.exitTycl_hdr_inst(self)




    def tycl_hdr_inst(self):

        localctx = HaskellParser.Tycl_hdr_instContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_tycl_hdr_inst)
        self._la = 0 # Token type
        try:
            self.state = 1213
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,133,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1193
                self.match(HaskellParser.FORALL)
                self.state = 1195
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 120)) & ~0x3f) == 0 and ((1 << (_la - 120)) & ((1 << (HaskellParser.OpenRoundBracket - 120)) | (1 << (HaskellParser.VARID - 120)) | (1 << (HaskellParser.OCURLY - 120)))) != 0):
                    self.state = 1194
                    self.tv_bndrs()


                self.state = 1197
                self.match(HaskellParser.Dot)
                self.state = 1198
                self.tycl_context()
                self.state = 1199
                self.match(HaskellParser.DoubleArrow)
                self.state = 1200
                self.htype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1202
                self.match(HaskellParser.FORALL)
                self.state = 1204
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 120)) & ~0x3f) == 0 and ((1 << (_la - 120)) & ((1 << (HaskellParser.OpenRoundBracket - 120)) | (1 << (HaskellParser.VARID - 120)) | (1 << (HaskellParser.OCURLY - 120)))) != 0):
                    self.state = 1203
                    self.tv_bndrs()


                self.state = 1206
                self.match(HaskellParser.Dot)
                self.state = 1207
                self.htype()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1208
                self.tycl_context()
                self.state = 1209
                self.match(HaskellParser.DoubleArrow)
                self.state = 1210
                self.htype()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1212
                self.htype()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Capi_ctypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenPragmaBracket(self):
            return self.getToken(HaskellParser.OpenPragmaBracket, 0)

        def CTYPE(self):
            return self.getToken(HaskellParser.CTYPE, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.STRING)
            else:
                return self.getToken(HaskellParser.STRING, i)

        def ClosePragmaBracket(self):
            return self.getToken(HaskellParser.ClosePragmaBracket, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_capi_ctype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCapi_ctype" ):
                listener.enterCapi_ctype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCapi_ctype" ):
                listener.exitCapi_ctype(self)




    def capi_ctype(self):

        localctx = HaskellParser.Capi_ctypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_capi_ctype)
        try:
            self.state = 1224
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,134,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1215
                self.match(HaskellParser.OpenPragmaBracket)
                self.state = 1216
                self.match(HaskellParser.CTYPE)
                self.state = 1217
                self.match(HaskellParser.STRING)
                self.state = 1218
                self.match(HaskellParser.STRING)
                self.state = 1219
                self.match(HaskellParser.ClosePragmaBracket)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1220
                self.match(HaskellParser.OpenPragmaBracket)
                self.state = 1221
                self.match(HaskellParser.CTYPE)
                self.state = 1222
                self.match(HaskellParser.STRING)
                self.state = 1223
                self.match(HaskellParser.ClosePragmaBracket)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Standalone_derivingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DERIVING(self):
            return self.getToken(HaskellParser.DERIVING, 0)

        def INSTANCE(self):
            return self.getToken(HaskellParser.INSTANCE, 0)

        def inst_type(self):
            return self.getTypedRuleContext(HaskellParser.Inst_typeContext,0)


        def deriv_standalone_strategy(self):
            return self.getTypedRuleContext(HaskellParser.Deriv_standalone_strategyContext,0)


        def overlap_pragma(self):
            return self.getTypedRuleContext(HaskellParser.Overlap_pragmaContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_standalone_deriving

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStandalone_deriving" ):
                listener.enterStandalone_deriving(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStandalone_deriving" ):
                listener.exitStandalone_deriving(self)




    def standalone_deriving(self):

        localctx = HaskellParser.Standalone_derivingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_standalone_deriving)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1226
            self.match(HaskellParser.DERIVING)
            self.state = 1228
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.NEWTYPE) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0):
                self.state = 1227
                self.deriv_standalone_strategy()


            self.state = 1230
            self.match(HaskellParser.INSTANCE)
            self.state = 1232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,136,self._ctx)
            if la_ == 1:
                self.state = 1231
                self.overlap_pragma()


            self.state = 1234
            self.inst_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Role_annotContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(HaskellParser.TYPE, 0)

        def ROLE(self):
            return self.getToken(HaskellParser.ROLE, 0)

        def oqtycon(self):
            return self.getTypedRuleContext(HaskellParser.OqtyconContext,0)


        def roles(self):
            return self.getTypedRuleContext(HaskellParser.RolesContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_role_annot

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRole_annot" ):
                listener.enterRole_annot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRole_annot" ):
                listener.exitRole_annot(self)




    def role_annot(self):

        localctx = HaskellParser.Role_annotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_role_annot)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1236
            self.match(HaskellParser.TYPE)
            self.state = 1237
            self.match(HaskellParser.ROLE)
            self.state = 1238
            self.oqtycon()
            self.state = 1240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.WILDCARD) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or _la==HaskellParser.VARID:
                self.state = 1239
                self.roles()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RolesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def role(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.RoleContext)
            else:
                return self.getTypedRuleContext(HaskellParser.RoleContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_roles

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoles" ):
                listener.enterRoles(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoles" ):
                listener.exitRoles(self)




    def roles(self):

        localctx = HaskellParser.RolesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_roles)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1243 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1242
                self.role()
                self.state = 1245 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.WILDCARD) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or _la==HaskellParser.VARID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RoleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varid(self):
            return self.getTypedRuleContext(HaskellParser.VaridContext,0)


        def WILDCARD(self):
            return self.getToken(HaskellParser.WILDCARD, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_role

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRole" ):
                listener.enterRole(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRole" ):
                listener.exitRole(self)




    def role(self):

        localctx = HaskellParser.RoleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_role)
        try:
            self.state = 1249
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.AS, HaskellParser.HIDING, HaskellParser.QUALIFIED, HaskellParser.EXPORT, HaskellParser.STDCALL, HaskellParser.CCALL, HaskellParser.CAPI, HaskellParser.JSCALL, HaskellParser.STOCK, HaskellParser.ANYCLASS, HaskellParser.VIA, HaskellParser.VARID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1247
                self.varid()
                pass
            elif token in [HaskellParser.WILDCARD]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1248
                self.match(HaskellParser.WILDCARD)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pattern_synonym_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PATTERN(self):
            return self.getToken(HaskellParser.PATTERN, 0)

        def pattern_synonym_lhs(self):
            return self.getTypedRuleContext(HaskellParser.Pattern_synonym_lhsContext,0)


        def Eq(self):
            return self.getToken(HaskellParser.Eq, 0)

        def pat(self):
            return self.getTypedRuleContext(HaskellParser.PatContext,0)


        def Revarrow(self):
            return self.getToken(HaskellParser.Revarrow, 0)

        def where_decls(self):
            return self.getTypedRuleContext(HaskellParser.Where_declsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_pattern_synonym_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPattern_synonym_decl" ):
                listener.enterPattern_synonym_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPattern_synonym_decl" ):
                listener.exitPattern_synonym_decl(self)




    def pattern_synonym_decl(self):

        localctx = HaskellParser.Pattern_synonym_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_pattern_synonym_decl)
        self._la = 0 # Token type
        try:
            self.state = 1263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,141,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1251
                self.match(HaskellParser.PATTERN)
                self.state = 1252
                self.pattern_synonym_lhs()
                self.state = 1253
                self.match(HaskellParser.Eq)
                self.state = 1254
                self.pat()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1256
                self.match(HaskellParser.PATTERN)
                self.state = 1257
                self.pattern_synonym_lhs()
                self.state = 1258
                self.match(HaskellParser.Revarrow)
                self.state = 1259
                self.pat()
                self.state = 1261
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.WHERE:
                    self.state = 1260
                    self.where_decls()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pattern_synonym_lhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def con(self):
            return self.getTypedRuleContext(HaskellParser.ConContext,0)


        def hvars(self):
            return self.getTypedRuleContext(HaskellParser.HvarsContext,0)


        def varid(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.VaridContext)
            else:
                return self.getTypedRuleContext(HaskellParser.VaridContext,i)


        def conop(self):
            return self.getTypedRuleContext(HaskellParser.ConopContext,0)


        def OCURLY(self):
            return self.getToken(HaskellParser.OCURLY, 0)

        def cvars(self):
            return self.getTypedRuleContext(HaskellParser.CvarsContext,0)


        def CCURLY(self):
            return self.getToken(HaskellParser.CCURLY, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_pattern_synonym_lhs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPattern_synonym_lhs" ):
                listener.enterPattern_synonym_lhs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPattern_synonym_lhs" ):
                listener.exitPattern_synonym_lhs(self)




    def pattern_synonym_lhs(self):

        localctx = HaskellParser.Pattern_synonym_lhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_pattern_synonym_lhs)
        self._la = 0 # Token type
        try:
            self.state = 1278
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,143,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1265
                self.con()
                self.state = 1267
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or _la==HaskellParser.VARID:
                    self.state = 1266
                    self.hvars()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1269
                self.varid()
                self.state = 1270
                self.conop()
                self.state = 1271
                self.varid()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1273
                self.con()
                self.state = 1274
                self.match(HaskellParser.OCURLY)
                self.state = 1275
                self.cvars()
                self.state = 1276
                self.match(HaskellParser.CCURLY)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HvarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varid(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.VaridContext)
            else:
                return self.getTypedRuleContext(HaskellParser.VaridContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_hvars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHvars" ):
                listener.enterHvars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHvars" ):
                listener.exitHvars(self)




    def hvars(self):

        localctx = HaskellParser.HvarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_hvars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1281 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1280
                self.varid()
                self.state = 1283 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or _la==HaskellParser.VARID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CvarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.VarContext)
            else:
                return self.getTypedRuleContext(HaskellParser.VarContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Comma)
            else:
                return self.getToken(HaskellParser.Comma, i)

        def getRuleIndex(self):
            return HaskellParser.RULE_cvars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCvars" ):
                listener.enterCvars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCvars" ):
                listener.exitCvars(self)




    def cvars(self):

        localctx = HaskellParser.CvarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_cvars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1285
            self.var()
            self.state = 1290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Comma:
                self.state = 1286
                self.match(HaskellParser.Comma)
                self.state = 1287
                self.var()
                self.state = 1292
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Where_declsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(HaskellParser.WHERE, 0)

        def opn(self):
            return self.getTypedRuleContext(HaskellParser.OpnContext,0)


        def close(self):
            return self.getTypedRuleContext(HaskellParser.CloseContext,0)


        def decls(self):
            return self.getTypedRuleContext(HaskellParser.DeclsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_where_decls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_decls" ):
                listener.enterWhere_decls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_decls" ):
                listener.exitWhere_decls(self)




    def where_decls(self):

        localctx = HaskellParser.Where_declsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_where_decls)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1293
            self.match(HaskellParser.WHERE)
            self.state = 1294
            self.opn()
            self.state = 1296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.CASE) | (1 << HaskellParser.DO) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.IF) | (1 << HaskellParser.INFIX) | (1 << HaskellParser.INFIXL) | (1 << HaskellParser.INFIXR) | (1 << HaskellParser.LET) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.WILDCARD) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.MDO) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.PATTERN) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & ((1 << (HaskellParser.LCASE - 73)) | (1 << (HaskellParser.Bang - 73)) | (1 << (HaskellParser.Minus - 73)) | (1 << (HaskellParser.Tilde - 73)) | (1 << (HaskellParser.DDollar - 73)) | (1 << (HaskellParser.Dollar - 73)) | (1 << (HaskellParser.Semi - 73)) | (1 << (HaskellParser.Quote - 73)) | (1 << (HaskellParser.DoubleQuote - 73)) | (1 << (HaskellParser.ReverseSlash - 73)) | (1 << (HaskellParser.AopenParen - 73)) | (1 << (HaskellParser.TopenTexpQuote - 73)) | (1 << (HaskellParser.TopenExpQuote - 73)) | (1 << (HaskellParser.TopenPatQuote - 73)) | (1 << (HaskellParser.TopenTypQoute - 73)) | (1 << (HaskellParser.TopenDecQoute - 73)) | (1 << (HaskellParser.OpenBoxParen - 73)) | (1 << (HaskellParser.OpenRoundBracket - 73)) | (1 << (HaskellParser.OpenSquareBracket - 73)) | (1 << (HaskellParser.CHAR - 73)) | (1 << (HaskellParser.STRING - 73)) | (1 << (HaskellParser.VARID - 73)) | (1 << (HaskellParser.CONID - 73)) | (1 << (HaskellParser.OpenPragmaBracket - 73)) | (1 << (HaskellParser.SEMI - 73)))) != 0) or ((((_la - 137)) & ~0x3f) == 0 and ((1 << (_la - 137)) & ((1 << (HaskellParser.DECIMAL - 137)) | (1 << (HaskellParser.OCTAL - 137)) | (1 << (HaskellParser.HEXADECIMAL - 137)) | (1 << (HaskellParser.FLOAT - 137)))) != 0):
                self.state = 1295
                self.decls()


            self.state = 1298
            self.close()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pattern_synonym_sigContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PATTERN(self):
            return self.getToken(HaskellParser.PATTERN, 0)

        def con_list(self):
            return self.getTypedRuleContext(HaskellParser.Con_listContext,0)


        def DoubleColon(self):
            return self.getToken(HaskellParser.DoubleColon, 0)

        def sigtypedoc(self):
            return self.getTypedRuleContext(HaskellParser.SigtypedocContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_pattern_synonym_sig

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPattern_synonym_sig" ):
                listener.enterPattern_synonym_sig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPattern_synonym_sig" ):
                listener.exitPattern_synonym_sig(self)




    def pattern_synonym_sig(self):

        localctx = HaskellParser.Pattern_synonym_sigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_pattern_synonym_sig)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1300
            self.match(HaskellParser.PATTERN)
            self.state = 1301
            self.con_list()
            self.state = 1302
            self.match(HaskellParser.DoubleColon)
            self.state = 1303
            self.sigtypedoc()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_clsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def at_decl_cls(self):
            return self.getTypedRuleContext(HaskellParser.At_decl_clsContext,0)


        def decl(self):
            return self.getTypedRuleContext(HaskellParser.DeclContext,0)


        def DEFAULT(self):
            return self.getToken(HaskellParser.DEFAULT, 0)

        def infixexp(self):
            return self.getTypedRuleContext(HaskellParser.InfixexpContext,0)


        def DoubleColon(self):
            return self.getToken(HaskellParser.DoubleColon, 0)

        def sigtypedoc(self):
            return self.getTypedRuleContext(HaskellParser.SigtypedocContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_decl_cls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl_cls" ):
                listener.enterDecl_cls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl_cls" ):
                listener.exitDecl_cls(self)




    def decl_cls(self):

        localctx = HaskellParser.Decl_clsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_decl_cls)
        try:
            self.state = 1312
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.DATA, HaskellParser.TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1305
                self.at_decl_cls()
                pass
            elif token in [HaskellParser.AS, HaskellParser.CASE, HaskellParser.DO, HaskellParser.HIDING, HaskellParser.IF, HaskellParser.INFIX, HaskellParser.INFIXL, HaskellParser.INFIXR, HaskellParser.LET, HaskellParser.QUALIFIED, HaskellParser.WILDCARD, HaskellParser.EXPORT, HaskellParser.MDO, HaskellParser.STDCALL, HaskellParser.CCALL, HaskellParser.CAPI, HaskellParser.JSCALL, HaskellParser.PATTERN, HaskellParser.STOCK, HaskellParser.ANYCLASS, HaskellParser.VIA, HaskellParser.LCASE, HaskellParser.Bang, HaskellParser.Minus, HaskellParser.Tilde, HaskellParser.DDollar, HaskellParser.Dollar, HaskellParser.Semi, HaskellParser.Quote, HaskellParser.DoubleQuote, HaskellParser.ReverseSlash, HaskellParser.AopenParen, HaskellParser.TopenTexpQuote, HaskellParser.TopenExpQuote, HaskellParser.TopenPatQuote, HaskellParser.TopenTypQoute, HaskellParser.TopenDecQoute, HaskellParser.OpenBoxParen, HaskellParser.OpenRoundBracket, HaskellParser.OpenSquareBracket, HaskellParser.CHAR, HaskellParser.STRING, HaskellParser.VARID, HaskellParser.CONID, HaskellParser.OpenPragmaBracket, HaskellParser.SEMI, HaskellParser.DECIMAL, HaskellParser.OCTAL, HaskellParser.HEXADECIMAL, HaskellParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1306
                self.decl()
                pass
            elif token in [HaskellParser.DEFAULT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 1307
                self.match(HaskellParser.DEFAULT)
                self.state = 1308
                self.infixexp()
                self.state = 1309
                self.match(HaskellParser.DoubleColon)
                self.state = 1310
                self.sigtypedoc()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decls_clsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_cls(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.Decl_clsContext)
            else:
                return self.getTypedRuleContext(HaskellParser.Decl_clsContext,i)


        def semi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.SemiContext)
            else:
                return self.getTypedRuleContext(HaskellParser.SemiContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_decls_cls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecls_cls" ):
                listener.enterDecls_cls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecls_cls" ):
                listener.exitDecls_cls(self)




    def decls_cls(self):

        localctx = HaskellParser.Decls_clsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_decls_cls)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1314
            self.decl_cls()
            self.state = 1324
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,149,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1316 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 1315
                            self.semi()

                        else:
                            raise NoViableAltException(self)
                        self.state = 1318 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,148,self._ctx)

                    self.state = 1320
                    self.decl_cls() 
                self.state = 1326
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,149,self._ctx)

            self.state = 1330
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Semi or _la==HaskellParser.SEMI:
                self.state = 1327
                self.semi()
                self.state = 1332
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decllist_clsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opn(self):
            return self.getTypedRuleContext(HaskellParser.OpnContext,0)


        def close(self):
            return self.getTypedRuleContext(HaskellParser.CloseContext,0)


        def decls_cls(self):
            return self.getTypedRuleContext(HaskellParser.Decls_clsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_decllist_cls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecllist_cls" ):
                listener.enterDecllist_cls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecllist_cls" ):
                listener.exitDecllist_cls(self)




    def decllist_cls(self):

        localctx = HaskellParser.Decllist_clsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_decllist_cls)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1333
            self.opn()
            self.state = 1335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.CASE) | (1 << HaskellParser.DATA) | (1 << HaskellParser.DEFAULT) | (1 << HaskellParser.DO) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.IF) | (1 << HaskellParser.INFIX) | (1 << HaskellParser.INFIXL) | (1 << HaskellParser.INFIXR) | (1 << HaskellParser.LET) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.TYPE) | (1 << HaskellParser.WILDCARD) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.MDO) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.PATTERN) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & ((1 << (HaskellParser.LCASE - 73)) | (1 << (HaskellParser.Bang - 73)) | (1 << (HaskellParser.Minus - 73)) | (1 << (HaskellParser.Tilde - 73)) | (1 << (HaskellParser.DDollar - 73)) | (1 << (HaskellParser.Dollar - 73)) | (1 << (HaskellParser.Semi - 73)) | (1 << (HaskellParser.Quote - 73)) | (1 << (HaskellParser.DoubleQuote - 73)) | (1 << (HaskellParser.ReverseSlash - 73)) | (1 << (HaskellParser.AopenParen - 73)) | (1 << (HaskellParser.TopenTexpQuote - 73)) | (1 << (HaskellParser.TopenExpQuote - 73)) | (1 << (HaskellParser.TopenPatQuote - 73)) | (1 << (HaskellParser.TopenTypQoute - 73)) | (1 << (HaskellParser.TopenDecQoute - 73)) | (1 << (HaskellParser.OpenBoxParen - 73)) | (1 << (HaskellParser.OpenRoundBracket - 73)) | (1 << (HaskellParser.OpenSquareBracket - 73)) | (1 << (HaskellParser.CHAR - 73)) | (1 << (HaskellParser.STRING - 73)) | (1 << (HaskellParser.VARID - 73)) | (1 << (HaskellParser.CONID - 73)) | (1 << (HaskellParser.OpenPragmaBracket - 73)) | (1 << (HaskellParser.SEMI - 73)))) != 0) or ((((_la - 137)) & ~0x3f) == 0 and ((1 << (_la - 137)) & ((1 << (HaskellParser.DECIMAL - 137)) | (1 << (HaskellParser.OCTAL - 137)) | (1 << (HaskellParser.HEXADECIMAL - 137)) | (1 << (HaskellParser.FLOAT - 137)))) != 0):
                self.state = 1334
                self.decls_cls()


            self.state = 1337
            self.close()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Where_clsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(HaskellParser.WHERE, 0)

        def decllist_cls(self):
            return self.getTypedRuleContext(HaskellParser.Decllist_clsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_where_cls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_cls" ):
                listener.enterWhere_cls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_cls" ):
                listener.exitWhere_cls(self)




    def where_cls(self):

        localctx = HaskellParser.Where_clsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_where_cls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1339
            self.match(HaskellParser.WHERE)
            self.state = 1340
            self.decllist_cls()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_instContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def at_decl_inst(self):
            return self.getTypedRuleContext(HaskellParser.At_decl_instContext,0)


        def decl(self):
            return self.getTypedRuleContext(HaskellParser.DeclContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_decl_inst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl_inst" ):
                listener.enterDecl_inst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl_inst" ):
                listener.exitDecl_inst(self)




    def decl_inst(self):

        localctx = HaskellParser.Decl_instContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_decl_inst)
        try:
            self.state = 1344
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.DATA, HaskellParser.NEWTYPE, HaskellParser.TYPE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1342
                self.at_decl_inst()
                pass
            elif token in [HaskellParser.AS, HaskellParser.CASE, HaskellParser.DO, HaskellParser.HIDING, HaskellParser.IF, HaskellParser.INFIX, HaskellParser.INFIXL, HaskellParser.INFIXR, HaskellParser.LET, HaskellParser.QUALIFIED, HaskellParser.WILDCARD, HaskellParser.EXPORT, HaskellParser.MDO, HaskellParser.STDCALL, HaskellParser.CCALL, HaskellParser.CAPI, HaskellParser.JSCALL, HaskellParser.PATTERN, HaskellParser.STOCK, HaskellParser.ANYCLASS, HaskellParser.VIA, HaskellParser.LCASE, HaskellParser.Bang, HaskellParser.Minus, HaskellParser.Tilde, HaskellParser.DDollar, HaskellParser.Dollar, HaskellParser.Semi, HaskellParser.Quote, HaskellParser.DoubleQuote, HaskellParser.ReverseSlash, HaskellParser.AopenParen, HaskellParser.TopenTexpQuote, HaskellParser.TopenExpQuote, HaskellParser.TopenPatQuote, HaskellParser.TopenTypQoute, HaskellParser.TopenDecQoute, HaskellParser.OpenBoxParen, HaskellParser.OpenRoundBracket, HaskellParser.OpenSquareBracket, HaskellParser.CHAR, HaskellParser.STRING, HaskellParser.VARID, HaskellParser.CONID, HaskellParser.OpenPragmaBracket, HaskellParser.SEMI, HaskellParser.DECIMAL, HaskellParser.OCTAL, HaskellParser.HEXADECIMAL, HaskellParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1343
                self.decl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decls_instContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_inst(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.Decl_instContext)
            else:
                return self.getTypedRuleContext(HaskellParser.Decl_instContext,i)


        def semi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.SemiContext)
            else:
                return self.getTypedRuleContext(HaskellParser.SemiContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_decls_inst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecls_inst" ):
                listener.enterDecls_inst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecls_inst" ):
                listener.exitDecls_inst(self)




    def decls_inst(self):

        localctx = HaskellParser.Decls_instContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_decls_inst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1346
            self.decl_inst()
            self.state = 1356
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,154,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1348 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 1347
                            self.semi()

                        else:
                            raise NoViableAltException(self)
                        self.state = 1350 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,153,self._ctx)

                    self.state = 1352
                    self.decl_inst() 
                self.state = 1358
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,154,self._ctx)

            self.state = 1362
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Semi or _la==HaskellParser.SEMI:
                self.state = 1359
                self.semi()
                self.state = 1364
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decllist_instContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opn(self):
            return self.getTypedRuleContext(HaskellParser.OpnContext,0)


        def close(self):
            return self.getTypedRuleContext(HaskellParser.CloseContext,0)


        def decls_inst(self):
            return self.getTypedRuleContext(HaskellParser.Decls_instContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_decllist_inst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecllist_inst" ):
                listener.enterDecllist_inst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecllist_inst" ):
                listener.exitDecllist_inst(self)




    def decllist_inst(self):

        localctx = HaskellParser.Decllist_instContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_decllist_inst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1365
            self.opn()
            self.state = 1367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.CASE) | (1 << HaskellParser.DATA) | (1 << HaskellParser.DO) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.IF) | (1 << HaskellParser.INFIX) | (1 << HaskellParser.INFIXL) | (1 << HaskellParser.INFIXR) | (1 << HaskellParser.LET) | (1 << HaskellParser.NEWTYPE) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.TYPE) | (1 << HaskellParser.WILDCARD) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.MDO) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.PATTERN) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & ((1 << (HaskellParser.LCASE - 73)) | (1 << (HaskellParser.Bang - 73)) | (1 << (HaskellParser.Minus - 73)) | (1 << (HaskellParser.Tilde - 73)) | (1 << (HaskellParser.DDollar - 73)) | (1 << (HaskellParser.Dollar - 73)) | (1 << (HaskellParser.Semi - 73)) | (1 << (HaskellParser.Quote - 73)) | (1 << (HaskellParser.DoubleQuote - 73)) | (1 << (HaskellParser.ReverseSlash - 73)) | (1 << (HaskellParser.AopenParen - 73)) | (1 << (HaskellParser.TopenTexpQuote - 73)) | (1 << (HaskellParser.TopenExpQuote - 73)) | (1 << (HaskellParser.TopenPatQuote - 73)) | (1 << (HaskellParser.TopenTypQoute - 73)) | (1 << (HaskellParser.TopenDecQoute - 73)) | (1 << (HaskellParser.OpenBoxParen - 73)) | (1 << (HaskellParser.OpenRoundBracket - 73)) | (1 << (HaskellParser.OpenSquareBracket - 73)) | (1 << (HaskellParser.CHAR - 73)) | (1 << (HaskellParser.STRING - 73)) | (1 << (HaskellParser.VARID - 73)) | (1 << (HaskellParser.CONID - 73)) | (1 << (HaskellParser.OpenPragmaBracket - 73)) | (1 << (HaskellParser.SEMI - 73)))) != 0) or ((((_la - 137)) & ~0x3f) == 0 and ((1 << (_la - 137)) & ((1 << (HaskellParser.DECIMAL - 137)) | (1 << (HaskellParser.OCTAL - 137)) | (1 << (HaskellParser.HEXADECIMAL - 137)) | (1 << (HaskellParser.FLOAT - 137)))) != 0):
                self.state = 1366
                self.decls_inst()


            self.state = 1369
            self.close()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Where_instContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(HaskellParser.WHERE, 0)

        def decllist_inst(self):
            return self.getTypedRuleContext(HaskellParser.Decllist_instContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_where_inst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_inst" ):
                listener.enterWhere_inst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_inst" ):
                listener.exitWhere_inst(self)




    def where_inst(self):

        localctx = HaskellParser.Where_instContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_where_inst)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1371
            self.match(HaskellParser.WHERE)
            self.state = 1372
            self.decllist_inst()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.DeclContext)
            else:
                return self.getTypedRuleContext(HaskellParser.DeclContext,i)


        def semi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.SemiContext)
            else:
                return self.getTypedRuleContext(HaskellParser.SemiContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_decls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecls" ):
                listener.enterDecls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecls" ):
                listener.exitDecls(self)




    def decls(self):

        localctx = HaskellParser.DeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_decls)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1374
            self.decl()
            self.state = 1384
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,158,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1376 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 1375
                            self.semi()

                        else:
                            raise NoViableAltException(self)
                        self.state = 1378 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,157,self._ctx)

                    self.state = 1380
                    self.decl() 
                self.state = 1386
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,158,self._ctx)

            self.state = 1390
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Semi or _la==HaskellParser.SEMI:
                self.state = 1387
                self.semi()
                self.state = 1392
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DecllistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opn(self):
            return self.getTypedRuleContext(HaskellParser.OpnContext,0)


        def close(self):
            return self.getTypedRuleContext(HaskellParser.CloseContext,0)


        def decls(self):
            return self.getTypedRuleContext(HaskellParser.DeclsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_decllist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecllist" ):
                listener.enterDecllist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecllist" ):
                listener.exitDecllist(self)




    def decllist(self):

        localctx = HaskellParser.DecllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_decllist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1393
            self.opn()
            self.state = 1395
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.CASE) | (1 << HaskellParser.DO) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.IF) | (1 << HaskellParser.INFIX) | (1 << HaskellParser.INFIXL) | (1 << HaskellParser.INFIXR) | (1 << HaskellParser.LET) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.WILDCARD) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.MDO) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.PATTERN) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & ((1 << (HaskellParser.LCASE - 73)) | (1 << (HaskellParser.Bang - 73)) | (1 << (HaskellParser.Minus - 73)) | (1 << (HaskellParser.Tilde - 73)) | (1 << (HaskellParser.DDollar - 73)) | (1 << (HaskellParser.Dollar - 73)) | (1 << (HaskellParser.Semi - 73)) | (1 << (HaskellParser.Quote - 73)) | (1 << (HaskellParser.DoubleQuote - 73)) | (1 << (HaskellParser.ReverseSlash - 73)) | (1 << (HaskellParser.AopenParen - 73)) | (1 << (HaskellParser.TopenTexpQuote - 73)) | (1 << (HaskellParser.TopenExpQuote - 73)) | (1 << (HaskellParser.TopenPatQuote - 73)) | (1 << (HaskellParser.TopenTypQoute - 73)) | (1 << (HaskellParser.TopenDecQoute - 73)) | (1 << (HaskellParser.OpenBoxParen - 73)) | (1 << (HaskellParser.OpenRoundBracket - 73)) | (1 << (HaskellParser.OpenSquareBracket - 73)) | (1 << (HaskellParser.CHAR - 73)) | (1 << (HaskellParser.STRING - 73)) | (1 << (HaskellParser.VARID - 73)) | (1 << (HaskellParser.CONID - 73)) | (1 << (HaskellParser.OpenPragmaBracket - 73)) | (1 << (HaskellParser.SEMI - 73)))) != 0) or ((((_la - 137)) & ~0x3f) == 0 and ((1 << (_la - 137)) & ((1 << (HaskellParser.DECIMAL - 137)) | (1 << (HaskellParser.OCTAL - 137)) | (1 << (HaskellParser.HEXADECIMAL - 137)) | (1 << (HaskellParser.FLOAT - 137)))) != 0):
                self.state = 1394
                self.decls()


            self.state = 1397
            self.close()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BindsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decllist(self):
            return self.getTypedRuleContext(HaskellParser.DecllistContext,0)


        def opn(self):
            return self.getTypedRuleContext(HaskellParser.OpnContext,0)


        def close(self):
            return self.getTypedRuleContext(HaskellParser.CloseContext,0)


        def dbinds(self):
            return self.getTypedRuleContext(HaskellParser.DbindsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_binds

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinds" ):
                listener.enterBinds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinds" ):
                listener.exitBinds(self)




    def binds(self):

        localctx = HaskellParser.BindsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_binds)
        self._la = 0 # Token type
        try:
            self.state = 1406
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,162,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1399
                self.decllist()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1400
                self.opn()
                self.state = 1402
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or _la==HaskellParser.VARID:
                    self.state = 1401
                    self.dbinds()


                self.state = 1404
                self.close()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WherebindsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(HaskellParser.WHERE, 0)

        def binds(self):
            return self.getTypedRuleContext(HaskellParser.BindsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_wherebinds

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWherebinds" ):
                listener.enterWherebinds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWherebinds" ):
                listener.exitWherebinds(self)




    def wherebinds(self):

        localctx = HaskellParser.WherebindsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_wherebinds)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1408
            self.match(HaskellParser.WHERE)
            self.state = 1409
            self.binds()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RulesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pragma_rule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.Pragma_ruleContext)
            else:
                return self.getTypedRuleContext(HaskellParser.Pragma_ruleContext,i)


        def semi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.SemiContext)
            else:
                return self.getTypedRuleContext(HaskellParser.SemiContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_rules

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRules" ):
                listener.enterRules(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRules" ):
                listener.exitRules(self)




    def rules(self):

        localctx = HaskellParser.RulesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_rules)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1411
            self.pragma_rule()
            self.state = 1417
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,163,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1412
                    self.semi()
                    self.state = 1413
                    self.pragma_rule() 
                self.state = 1419
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,163,self._ctx)

            self.state = 1421
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HaskellParser.Semi or _la==HaskellParser.SEMI:
                self.state = 1420
                self.semi()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pragma_ruleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pstring(self):
            return self.getTypedRuleContext(HaskellParser.PstringContext,0)


        def infixexp(self):
            return self.getTypedRuleContext(HaskellParser.InfixexpContext,0)


        def Eq(self):
            return self.getToken(HaskellParser.Eq, 0)

        def exp(self):
            return self.getTypedRuleContext(HaskellParser.ExpContext,0)


        def rule_activation(self):
            return self.getTypedRuleContext(HaskellParser.Rule_activationContext,0)


        def rule_foralls(self):
            return self.getTypedRuleContext(HaskellParser.Rule_forallsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_pragma_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPragma_rule" ):
                listener.enterPragma_rule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPragma_rule" ):
                listener.exitPragma_rule(self)




    def pragma_rule(self):

        localctx = HaskellParser.Pragma_ruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_pragma_rule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1423
            self.pstring()
            self.state = 1425
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,165,self._ctx)
            if la_ == 1:
                self.state = 1424
                self.rule_activation()


            self.state = 1428
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HaskellParser.FORALL:
                self.state = 1427
                self.rule_foralls()


            self.state = 1430
            self.infixexp()
            self.state = 1431
            self.match(HaskellParser.Eq)
            self.state = 1432
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rule_activation_markerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Tilde(self):
            return self.getToken(HaskellParser.Tilde, 0)

        def varsym(self):
            return self.getTypedRuleContext(HaskellParser.VarsymContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_rule_activation_marker

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_activation_marker" ):
                listener.enterRule_activation_marker(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_activation_marker" ):
                listener.exitRule_activation_marker(self)




    def rule_activation_marker(self):

        localctx = HaskellParser.Rule_activation_markerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_rule_activation_marker)
        try:
            self.state = 1436
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,167,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1434
                self.match(HaskellParser.Tilde)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1435
                self.varsym()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rule_activationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenSquareBracket(self):
            return self.getToken(HaskellParser.OpenSquareBracket, 0)

        def integer(self):
            return self.getTypedRuleContext(HaskellParser.IntegerContext,0)


        def CloseSquareBracket(self):
            return self.getToken(HaskellParser.CloseSquareBracket, 0)

        def rule_activation_marker(self):
            return self.getTypedRuleContext(HaskellParser.Rule_activation_markerContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_rule_activation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_activation" ):
                listener.enterRule_activation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_activation" ):
                listener.exitRule_activation(self)




    def rule_activation(self):

        localctx = HaskellParser.Rule_activationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_rule_activation)
        try:
            self.state = 1451
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,168,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1438
                self.match(HaskellParser.OpenSquareBracket)
                self.state = 1439
                self.integer()
                self.state = 1440
                self.match(HaskellParser.CloseSquareBracket)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1442
                self.match(HaskellParser.OpenSquareBracket)
                self.state = 1443
                self.rule_activation_marker()
                self.state = 1444
                self.integer()
                self.state = 1445
                self.match(HaskellParser.CloseSquareBracket)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1447
                self.match(HaskellParser.OpenSquareBracket)
                self.state = 1448
                self.rule_activation_marker()
                self.state = 1449
                self.match(HaskellParser.CloseSquareBracket)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rule_forallsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FORALL(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.FORALL)
            else:
                return self.getToken(HaskellParser.FORALL, i)

        def Dot(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Dot)
            else:
                return self.getToken(HaskellParser.Dot, i)

        def rule_vars(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.Rule_varsContext)
            else:
                return self.getTypedRuleContext(HaskellParser.Rule_varsContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_rule_foralls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_foralls" ):
                listener.enterRule_foralls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_foralls" ):
                listener.exitRule_foralls(self)




    def rule_foralls(self):

        localctx = HaskellParser.Rule_forallsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_rule_foralls)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1453
            self.match(HaskellParser.FORALL)
            self.state = 1455
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or _la==HaskellParser.OpenRoundBracket or _la==HaskellParser.VARID:
                self.state = 1454
                self.rule_vars()


            self.state = 1457
            self.match(HaskellParser.Dot)
            self.state = 1463
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HaskellParser.FORALL:
                self.state = 1458
                self.match(HaskellParser.FORALL)
                self.state = 1460
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or _la==HaskellParser.OpenRoundBracket or _la==HaskellParser.VARID:
                    self.state = 1459
                    self.rule_vars()


                self.state = 1462
                self.match(HaskellParser.Dot)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rule_varsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rule_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.Rule_varContext)
            else:
                return self.getTypedRuleContext(HaskellParser.Rule_varContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_rule_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_vars" ):
                listener.enterRule_vars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_vars" ):
                listener.exitRule_vars(self)




    def rule_vars(self):

        localctx = HaskellParser.Rule_varsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_rule_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1466 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1465
                self.rule_var()
                self.state = 1468 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or _la==HaskellParser.OpenRoundBracket or _la==HaskellParser.VARID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rule_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varid(self):
            return self.getTypedRuleContext(HaskellParser.VaridContext,0)


        def OpenRoundBracket(self):
            return self.getToken(HaskellParser.OpenRoundBracket, 0)

        def DoubleColon(self):
            return self.getToken(HaskellParser.DoubleColon, 0)

        def ctype(self):
            return self.getTypedRuleContext(HaskellParser.CtypeContext,0)


        def CloseRoundBracket(self):
            return self.getToken(HaskellParser.CloseRoundBracket, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_rule_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_var" ):
                listener.enterRule_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_var" ):
                listener.exitRule_var(self)




    def rule_var(self):

        localctx = HaskellParser.Rule_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_rule_var)
        try:
            self.state = 1477
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.AS, HaskellParser.HIDING, HaskellParser.QUALIFIED, HaskellParser.EXPORT, HaskellParser.STDCALL, HaskellParser.CCALL, HaskellParser.CAPI, HaskellParser.JSCALL, HaskellParser.STOCK, HaskellParser.ANYCLASS, HaskellParser.VIA, HaskellParser.VARID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1470
                self.varid()
                pass
            elif token in [HaskellParser.OpenRoundBracket]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1471
                self.match(HaskellParser.OpenRoundBracket)
                self.state = 1472
                self.varid()
                self.state = 1473
                self.match(HaskellParser.DoubleColon)
                self.state = 1474
                self.ctype()
                self.state = 1475
                self.match(HaskellParser.CloseRoundBracket)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WarningsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pragma_warning(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.Pragma_warningContext)
            else:
                return self.getTypedRuleContext(HaskellParser.Pragma_warningContext,i)


        def semi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.SemiContext)
            else:
                return self.getTypedRuleContext(HaskellParser.SemiContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_warnings

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWarnings" ):
                listener.enterWarnings(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWarnings" ):
                listener.exitWarnings(self)




    def warnings(self):

        localctx = HaskellParser.WarningsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_warnings)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1479
            self.pragma_warning()
            self.state = 1485
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,174,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1480
                    self.semi()
                    self.state = 1481
                    self.pragma_warning() 
                self.state = 1487
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,174,self._ctx)

            self.state = 1489
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HaskellParser.Semi or _la==HaskellParser.SEMI:
                self.state = 1488
                self.semi()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pragma_warningContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namelist(self):
            return self.getTypedRuleContext(HaskellParser.NamelistContext,0)


        def strings(self):
            return self.getTypedRuleContext(HaskellParser.StringsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_pragma_warning

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPragma_warning" ):
                listener.enterPragma_warning(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPragma_warning" ):
                listener.exitPragma_warning(self)




    def pragma_warning(self):

        localctx = HaskellParser.Pragma_warningContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_pragma_warning)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1491
            self.namelist()
            self.state = 1492
            self.strings()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeprecationsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pragma_deprecation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.Pragma_deprecationContext)
            else:
                return self.getTypedRuleContext(HaskellParser.Pragma_deprecationContext,i)


        def semi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.SemiContext)
            else:
                return self.getTypedRuleContext(HaskellParser.SemiContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_deprecations

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeprecations" ):
                listener.enterDeprecations(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeprecations" ):
                listener.exitDeprecations(self)




    def deprecations(self):

        localctx = HaskellParser.DeprecationsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_deprecations)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1494
            self.pragma_deprecation()
            self.state = 1500
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,176,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1495
                    self.semi()
                    self.state = 1496
                    self.pragma_deprecation() 
                self.state = 1502
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,176,self._ctx)

            self.state = 1504
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HaskellParser.Semi or _la==HaskellParser.SEMI:
                self.state = 1503
                self.semi()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pragma_deprecationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def namelist(self):
            return self.getTypedRuleContext(HaskellParser.NamelistContext,0)


        def strings(self):
            return self.getTypedRuleContext(HaskellParser.StringsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_pragma_deprecation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPragma_deprecation" ):
                listener.enterPragma_deprecation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPragma_deprecation" ):
                listener.exitPragma_deprecation(self)




    def pragma_deprecation(self):

        localctx = HaskellParser.Pragma_deprecationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_pragma_deprecation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1506
            self.namelist()
            self.state = 1507
            self.strings()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pstring(self):
            return self.getTypedRuleContext(HaskellParser.PstringContext,0)


        def OpenSquareBracket(self):
            return self.getToken(HaskellParser.OpenSquareBracket, 0)

        def CloseSquareBracket(self):
            return self.getToken(HaskellParser.CloseSquareBracket, 0)

        def stringlist(self):
            return self.getTypedRuleContext(HaskellParser.StringlistContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_strings

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStrings" ):
                listener.enterStrings(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStrings" ):
                listener.exitStrings(self)




    def strings(self):

        localctx = HaskellParser.StringsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_strings)
        self._la = 0 # Token type
        try:
            self.state = 1515
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1509
                self.pstring()
                pass
            elif token in [HaskellParser.OpenSquareBracket]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1510
                self.match(HaskellParser.OpenSquareBracket)
                self.state = 1512
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.STRING:
                    self.state = 1511
                    self.stringlist()


                self.state = 1514
                self.match(HaskellParser.CloseSquareBracket)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StringlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pstring(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.PstringContext)
            else:
                return self.getTypedRuleContext(HaskellParser.PstringContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Comma)
            else:
                return self.getToken(HaskellParser.Comma, i)

        def getRuleIndex(self):
            return HaskellParser.RULE_stringlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringlist" ):
                listener.enterStringlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringlist" ):
                listener.exitStringlist(self)




    def stringlist(self):

        localctx = HaskellParser.StringlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 162, self.RULE_stringlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1517
            self.pstring()
            self.state = 1522
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Comma:
                self.state = 1518
                self.match(HaskellParser.Comma)
                self.state = 1519
                self.pstring()
                self.state = 1524
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AnnotationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenPragmaBracket(self):
            return self.getToken(HaskellParser.OpenPragmaBracket, 0)

        def ANN(self):
            return self.getToken(HaskellParser.ANN, 0)

        def name_var(self):
            return self.getTypedRuleContext(HaskellParser.Name_varContext,0)


        def aexp(self):
            return self.getTypedRuleContext(HaskellParser.AexpContext,0)


        def ClosePragmaBracket(self):
            return self.getToken(HaskellParser.ClosePragmaBracket, 0)

        def tycon(self):
            return self.getTypedRuleContext(HaskellParser.TyconContext,0)


        def MODULE(self):
            return self.getToken(HaskellParser.MODULE, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_annotation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAnnotation" ):
                listener.enterAnnotation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAnnotation" ):
                listener.exitAnnotation(self)




    def annotation(self):

        localctx = HaskellParser.AnnotationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 164, self.RULE_annotation)
        try:
            self.state = 1543
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,181,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1525
                self.match(HaskellParser.OpenPragmaBracket)
                self.state = 1526
                self.match(HaskellParser.ANN)
                self.state = 1527
                self.name_var()
                self.state = 1528
                self.aexp()
                self.state = 1529
                self.match(HaskellParser.ClosePragmaBracket)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1531
                self.match(HaskellParser.OpenPragmaBracket)
                self.state = 1532
                self.match(HaskellParser.ANN)
                self.state = 1533
                self.tycon()
                self.state = 1534
                self.aexp()
                self.state = 1535
                self.match(HaskellParser.ClosePragmaBracket)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1537
                self.match(HaskellParser.OpenPragmaBracket)
                self.state = 1538
                self.match(HaskellParser.ANN)
                self.state = 1539
                self.match(HaskellParser.MODULE)
                self.state = 1540
                self.aexp()
                self.state = 1541
                self.match(HaskellParser.ClosePragmaBracket)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(HaskellParser.IMPORT, 0)

        def callconv(self):
            return self.getTypedRuleContext(HaskellParser.CallconvContext,0)


        def fspec(self):
            return self.getTypedRuleContext(HaskellParser.FspecContext,0)


        def safety(self):
            return self.getTypedRuleContext(HaskellParser.SafetyContext,0)


        def EXPORT(self):
            return self.getToken(HaskellParser.EXPORT, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_fdecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFdecl" ):
                listener.enterFdecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFdecl" ):
                listener.exitFdecl(self)




    def fdecl(self):

        localctx = HaskellParser.FdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 166, self.RULE_fdecl)
        self._la = 0 # Token type
        try:
            self.state = 1556
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.IMPORT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1545
                self.match(HaskellParser.IMPORT)
                self.state = 1546
                self.callconv()
                self.state = 1548
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.SAFE) | (1 << HaskellParser.INTERRUPTIBLE) | (1 << HaskellParser.UNSAFE))) != 0):
                    self.state = 1547
                    self.safety()


                self.state = 1550
                self.fspec()
                pass
            elif token in [HaskellParser.EXPORT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1552
                self.match(HaskellParser.EXPORT)
                self.state = 1553
                self.callconv()
                self.state = 1554
                self.fspec()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallconvContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CCALL(self):
            return self.getToken(HaskellParser.CCALL, 0)

        def STDCALL(self):
            return self.getToken(HaskellParser.STDCALL, 0)

        def CPPCALL(self):
            return self.getToken(HaskellParser.CPPCALL, 0)

        def JSCALL(self):
            return self.getToken(HaskellParser.JSCALL, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_callconv

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCallconv" ):
                listener.enterCallconv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCallconv" ):
                listener.exitCallconv(self)




    def callconv(self):

        localctx = HaskellParser.CallconvContext(self, self._ctx, self.state)
        self.enterRule(localctx, 168, self.RULE_callconv)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1558
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CPPCALL) | (1 << HaskellParser.JSCALL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SafetyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNSAFE(self):
            return self.getToken(HaskellParser.UNSAFE, 0)

        def SAFE(self):
            return self.getToken(HaskellParser.SAFE, 0)

        def INTERRUPTIBLE(self):
            return self.getToken(HaskellParser.INTERRUPTIBLE, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_safety

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSafety" ):
                listener.enterSafety(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSafety" ):
                listener.exitSafety(self)




    def safety(self):

        localctx = HaskellParser.SafetyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 170, self.RULE_safety)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1560
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.SAFE) | (1 << HaskellParser.INTERRUPTIBLE) | (1 << HaskellParser.UNSAFE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FspecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(HaskellParser.VarContext,0)


        def DoubleColon(self):
            return self.getToken(HaskellParser.DoubleColon, 0)

        def sigtypedoc(self):
            return self.getTypedRuleContext(HaskellParser.SigtypedocContext,0)


        def pstring(self):
            return self.getTypedRuleContext(HaskellParser.PstringContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_fspec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFspec" ):
                listener.enterFspec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFspec" ):
                listener.exitFspec(self)




    def fspec(self):

        localctx = HaskellParser.FspecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 172, self.RULE_fspec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1563
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HaskellParser.STRING:
                self.state = 1562
                self.pstring()


            self.state = 1565
            self.var()
            self.state = 1566
            self.match(HaskellParser.DoubleColon)
            self.state = 1567
            self.sigtypedoc()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Opt_sigContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DoubleColon(self):
            return self.getToken(HaskellParser.DoubleColon, 0)

        def sigtype(self):
            return self.getTypedRuleContext(HaskellParser.SigtypeContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_opt_sig

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpt_sig" ):
                listener.enterOpt_sig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpt_sig" ):
                listener.exitOpt_sig(self)




    def opt_sig(self):

        localctx = HaskellParser.Opt_sigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 174, self.RULE_opt_sig)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1569
            self.match(HaskellParser.DoubleColon)
            self.state = 1570
            self.sigtype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Opt_tyconsigContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DoubleColon(self):
            return self.getToken(HaskellParser.DoubleColon, 0)

        def gtycon(self):
            return self.getTypedRuleContext(HaskellParser.GtyconContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_opt_tyconsig

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpt_tyconsig" ):
                listener.enterOpt_tyconsig(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpt_tyconsig" ):
                listener.exitOpt_tyconsig(self)




    def opt_tyconsig(self):

        localctx = HaskellParser.Opt_tyconsigContext(self, self._ctx, self.state)
        self.enterRule(localctx, 176, self.RULE_opt_tyconsig)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1572
            self.match(HaskellParser.DoubleColon)
            self.state = 1573
            self.gtycon()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SigtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ctype(self):
            return self.getTypedRuleContext(HaskellParser.CtypeContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_sigtype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSigtype" ):
                listener.enterSigtype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSigtype" ):
                listener.exitSigtype(self)




    def sigtype(self):

        localctx = HaskellParser.SigtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 178, self.RULE_sigtype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1575
            self.ctype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SigtypedocContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ctypedoc(self):
            return self.getTypedRuleContext(HaskellParser.CtypedocContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_sigtypedoc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSigtypedoc" ):
                listener.enterSigtypedoc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSigtypedoc" ):
                listener.exitSigtypedoc(self)




    def sigtypedoc(self):

        localctx = HaskellParser.SigtypedocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 180, self.RULE_sigtypedoc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1577
            self.ctypedoc()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sig_varsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.VarContext)
            else:
                return self.getTypedRuleContext(HaskellParser.VarContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Comma)
            else:
                return self.getToken(HaskellParser.Comma, i)

        def getRuleIndex(self):
            return HaskellParser.RULE_sig_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSig_vars" ):
                listener.enterSig_vars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSig_vars" ):
                listener.exitSig_vars(self)




    def sig_vars(self):

        localctx = HaskellParser.Sig_varsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 182, self.RULE_sig_vars)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1579
            self.var()
            self.state = 1584
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Comma:
                self.state = 1580
                self.match(HaskellParser.Comma)
                self.state = 1581
                self.var()
                self.state = 1586
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sigtypes1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sigtype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.SigtypeContext)
            else:
                return self.getTypedRuleContext(HaskellParser.SigtypeContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Comma)
            else:
                return self.getToken(HaskellParser.Comma, i)

        def getRuleIndex(self):
            return HaskellParser.RULE_sigtypes1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSigtypes1" ):
                listener.enterSigtypes1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSigtypes1" ):
                listener.exitSigtypes1(self)




    def sigtypes1(self):

        localctx = HaskellParser.Sigtypes1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_sigtypes1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1587
            self.sigtype()
            self.state = 1592
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Comma:
                self.state = 1588
                self.match(HaskellParser.Comma)
                self.state = 1589
                self.sigtype()
                self.state = 1594
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnpackednessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenPragmaBracket(self):
            return self.getToken(HaskellParser.OpenPragmaBracket, 0)

        def UNPACK(self):
            return self.getToken(HaskellParser.UNPACK, 0)

        def ClosePragmaBracket(self):
            return self.getToken(HaskellParser.ClosePragmaBracket, 0)

        def NOUNPACK(self):
            return self.getToken(HaskellParser.NOUNPACK, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_unpackedness

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnpackedness" ):
                listener.enterUnpackedness(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnpackedness" ):
                listener.exitUnpackedness(self)




    def unpackedness(self):

        localctx = HaskellParser.UnpackednessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 186, self.RULE_unpackedness)
        try:
            self.state = 1601
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,187,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1595
                self.match(HaskellParser.OpenPragmaBracket)
                self.state = 1596
                self.match(HaskellParser.UNPACK)
                self.state = 1597
                self.match(HaskellParser.ClosePragmaBracket)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1598
                self.match(HaskellParser.OpenPragmaBracket)
                self.state = 1599
                self.match(HaskellParser.NOUNPACK)
                self.state = 1600
                self.match(HaskellParser.ClosePragmaBracket)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Forall_vis_flagContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Dot(self):
            return self.getToken(HaskellParser.Dot, 0)

        def Arrow(self):
            return self.getToken(HaskellParser.Arrow, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_forall_vis_flag

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForall_vis_flag" ):
                listener.enterForall_vis_flag(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForall_vis_flag" ):
                listener.exitForall_vis_flag(self)




    def forall_vis_flag(self):

        localctx = HaskellParser.Forall_vis_flagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 188, self.RULE_forall_vis_flag)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1603
            _la = self._input.LA(1)
            if not(_la==HaskellParser.Arrow or _la==HaskellParser.Dot):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ctype(self):
            return self.getTypedRuleContext(HaskellParser.CtypeContext,0)


        def DoubleColon(self):
            return self.getToken(HaskellParser.DoubleColon, 0)

        def kind(self):
            return self.getTypedRuleContext(HaskellParser.KindContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_ktype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKtype" ):
                listener.enterKtype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKtype" ):
                listener.exitKtype(self)




    def ktype(self):

        localctx = HaskellParser.KtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_ktype)
        try:
            self.state = 1610
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,188,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1605
                self.ctype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1606
                self.ctype()
                self.state = 1607
                self.match(HaskellParser.DoubleColon)
                self.state = 1608
                self.kind()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KtypedocContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ctypedoc(self):
            return self.getTypedRuleContext(HaskellParser.CtypedocContext,0)


        def DoubleColon(self):
            return self.getToken(HaskellParser.DoubleColon, 0)

        def kind(self):
            return self.getTypedRuleContext(HaskellParser.KindContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_ktypedoc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKtypedoc" ):
                listener.enterKtypedoc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKtypedoc" ):
                listener.exitKtypedoc(self)




    def ktypedoc(self):

        localctx = HaskellParser.KtypedocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 192, self.RULE_ktypedoc)
        try:
            self.state = 1617
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,189,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1612
                self.ctypedoc()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1613
                self.ctypedoc()
                self.state = 1614
                self.match(HaskellParser.DoubleColon)
                self.state = 1615
                self.kind()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FORALL(self):
            return self.getToken(HaskellParser.FORALL, 0)

        def forall_vis_flag(self):
            return self.getTypedRuleContext(HaskellParser.Forall_vis_flagContext,0)


        def ctype(self):
            return self.getTypedRuleContext(HaskellParser.CtypeContext,0)


        def tv_bndrs(self):
            return self.getTypedRuleContext(HaskellParser.Tv_bndrsContext,0)


        def btype(self):
            return self.getTypedRuleContext(HaskellParser.BtypeContext,0)


        def DoubleArrow(self):
            return self.getToken(HaskellParser.DoubleArrow, 0)

        def var(self):
            return self.getTypedRuleContext(HaskellParser.VarContext,0)


        def DoubleColon(self):
            return self.getToken(HaskellParser.DoubleColon, 0)

        def htype(self):
            return self.getTypedRuleContext(HaskellParser.HtypeContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_ctype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCtype" ):
                listener.enterCtype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCtype" ):
                listener.exitCtype(self)




    def ctype(self):

        localctx = HaskellParser.CtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 194, self.RULE_ctype)
        self._la = 0 # Token type
        try:
            self.state = 1635
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,191,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1619
                self.match(HaskellParser.FORALL)
                self.state = 1621
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 120)) & ~0x3f) == 0 and ((1 << (_la - 120)) & ((1 << (HaskellParser.OpenRoundBracket - 120)) | (1 << (HaskellParser.VARID - 120)) | (1 << (HaskellParser.OCURLY - 120)))) != 0):
                    self.state = 1620
                    self.tv_bndrs()


                self.state = 1623
                self.forall_vis_flag()
                self.state = 1624
                self.ctype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1626
                self.btype()
                self.state = 1627
                self.match(HaskellParser.DoubleArrow)
                self.state = 1628
                self.ctype()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1630
                self.var()
                self.state = 1631
                self.match(HaskellParser.DoubleColon)
                self.state = 1632
                self.htype()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1634
                self.htype()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CtypedocContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FORALL(self):
            return self.getToken(HaskellParser.FORALL, 0)

        def forall_vis_flag(self):
            return self.getTypedRuleContext(HaskellParser.Forall_vis_flagContext,0)


        def ctypedoc(self):
            return self.getTypedRuleContext(HaskellParser.CtypedocContext,0)


        def tv_bndrs(self):
            return self.getTypedRuleContext(HaskellParser.Tv_bndrsContext,0)


        def tycl_context(self):
            return self.getTypedRuleContext(HaskellParser.Tycl_contextContext,0)


        def DoubleArrow(self):
            return self.getToken(HaskellParser.DoubleArrow, 0)

        def var(self):
            return self.getTypedRuleContext(HaskellParser.VarContext,0)


        def DoubleColon(self):
            return self.getToken(HaskellParser.DoubleColon, 0)

        def htype(self):
            return self.getTypedRuleContext(HaskellParser.HtypeContext,0)


        def typedoc(self):
            return self.getTypedRuleContext(HaskellParser.TypedocContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_ctypedoc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCtypedoc" ):
                listener.enterCtypedoc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCtypedoc" ):
                listener.exitCtypedoc(self)




    def ctypedoc(self):

        localctx = HaskellParser.CtypedocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 196, self.RULE_ctypedoc)
        self._la = 0 # Token type
        try:
            self.state = 1653
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,193,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1637
                self.match(HaskellParser.FORALL)
                self.state = 1639
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 120)) & ~0x3f) == 0 and ((1 << (_la - 120)) & ((1 << (HaskellParser.OpenRoundBracket - 120)) | (1 << (HaskellParser.VARID - 120)) | (1 << (HaskellParser.OCURLY - 120)))) != 0):
                    self.state = 1638
                    self.tv_bndrs()


                self.state = 1641
                self.forall_vis_flag()
                self.state = 1642
                self.ctypedoc()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1644
                self.tycl_context()
                self.state = 1645
                self.match(HaskellParser.DoubleArrow)
                self.state = 1646
                self.ctypedoc()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1648
                self.var()
                self.state = 1649
                self.match(HaskellParser.DoubleColon)
                self.state = 1650
                self.htype()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1652
                self.typedoc()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tycl_contextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def btype(self):
            return self.getTypedRuleContext(HaskellParser.BtypeContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_tycl_context

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTycl_context" ):
                listener.enterTycl_context(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTycl_context" ):
                listener.exitTycl_context(self)




    def tycl_context(self):

        localctx = HaskellParser.Tycl_contextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 198, self.RULE_tycl_context)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1655
            self.btype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constr_contextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constr_btype(self):
            return self.getTypedRuleContext(HaskellParser.Constr_btypeContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_constr_context

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstr_context" ):
                listener.enterConstr_context(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstr_context" ):
                listener.exitConstr_context(self)




    def constr_context(self):

        localctx = HaskellParser.Constr_contextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 200, self.RULE_constr_context)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1657
            self.constr_btype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def btype(self):
            return self.getTypedRuleContext(HaskellParser.BtypeContext,0)


        def Arrow(self):
            return self.getToken(HaskellParser.Arrow, 0)

        def ctype(self):
            return self.getTypedRuleContext(HaskellParser.CtypeContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_htype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHtype" ):
                listener.enterHtype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHtype" ):
                listener.exitHtype(self)




    def htype(self):

        localctx = HaskellParser.HtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 202, self.RULE_htype)
        try:
            self.state = 1664
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,194,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1659
                self.btype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1660
                self.btype()
                self.state = 1661
                self.match(HaskellParser.Arrow)
                self.state = 1662
                self.ctype()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypedocContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def btype(self):
            return self.getTypedRuleContext(HaskellParser.BtypeContext,0)


        def Arrow(self):
            return self.getToken(HaskellParser.Arrow, 0)

        def ctypedoc(self):
            return self.getTypedRuleContext(HaskellParser.CtypedocContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_typedoc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypedoc" ):
                listener.enterTypedoc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypedoc" ):
                listener.exitTypedoc(self)




    def typedoc(self):

        localctx = HaskellParser.TypedocContext(self, self._ctx, self.state)
        self.enterRule(localctx, 204, self.RULE_typedoc)
        try:
            self.state = 1671
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,195,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1666
                self.btype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1667
                self.btype()
                self.state = 1668
                self.match(HaskellParser.Arrow)
                self.state = 1669
                self.ctypedoc()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constr_btypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constr_tyapps(self):
            return self.getTypedRuleContext(HaskellParser.Constr_tyappsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_constr_btype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstr_btype" ):
                listener.enterConstr_btype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstr_btype" ):
                listener.exitConstr_btype(self)




    def constr_btype(self):

        localctx = HaskellParser.Constr_btypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 206, self.RULE_constr_btype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1673
            self.constr_tyapps()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constr_tyappsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constr_tyapp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.Constr_tyappContext)
            else:
                return self.getTypedRuleContext(HaskellParser.Constr_tyappContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_constr_tyapps

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstr_tyapps" ):
                listener.enterConstr_tyapps(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstr_tyapps" ):
                listener.exitConstr_tyapps(self)




    def constr_tyapps(self):

        localctx = HaskellParser.Constr_tyappsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 208, self.RULE_constr_tyapps)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1676 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 1675
                    self.constr_tyapp()

                else:
                    raise NoViableAltException(self)
                self.state = 1678 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,196,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constr_tyappContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tyapp(self):
            return self.getTypedRuleContext(HaskellParser.TyappContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_constr_tyapp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstr_tyapp" ):
                listener.enterConstr_tyapp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstr_tyapp" ):
                listener.exitConstr_tyapp(self)




    def constr_tyapp(self):

        localctx = HaskellParser.Constr_tyappContext(self, self._ctx, self.state)
        self.enterRule(localctx, 210, self.RULE_constr_tyapp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1680
            self.tyapp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tyapps(self):
            return self.getTypedRuleContext(HaskellParser.TyappsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_btype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBtype" ):
                listener.enterBtype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBtype" ):
                listener.exitBtype(self)




    def btype(self):

        localctx = HaskellParser.BtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 212, self.RULE_btype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1682
            self.tyapps()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TyappsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tyapp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.TyappContext)
            else:
                return self.getTypedRuleContext(HaskellParser.TyappContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_tyapps

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTyapps" ):
                listener.enterTyapps(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTyapps" ):
                listener.exitTyapps(self)




    def tyapps(self):

        localctx = HaskellParser.TyappsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 214, self.RULE_tyapps)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1685 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 1684
                    self.tyapp()

                else:
                    raise NoViableAltException(self)
                self.state = 1687 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,197,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TyappContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atype(self):
            return self.getTypedRuleContext(HaskellParser.AtypeContext,0)


        def Atsign(self):
            return self.getToken(HaskellParser.Atsign, 0)

        def qtyconop(self):
            return self.getTypedRuleContext(HaskellParser.QtyconopContext,0)


        def tyvarop(self):
            return self.getTypedRuleContext(HaskellParser.TyvaropContext,0)


        def Quote(self):
            return self.getToken(HaskellParser.Quote, 0)

        def qconop(self):
            return self.getTypedRuleContext(HaskellParser.QconopContext,0)


        def varop(self):
            return self.getTypedRuleContext(HaskellParser.VaropContext,0)


        def unpackedness(self):
            return self.getTypedRuleContext(HaskellParser.UnpackednessContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_tyapp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTyapp" ):
                listener.enterTyapp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTyapp" ):
                listener.exitTyapp(self)




    def tyapp(self):

        localctx = HaskellParser.TyappContext(self, self._ctx, self.state)
        self.enterRule(localctx, 216, self.RULE_tyapp)
        try:
            self.state = 1699
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,198,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1689
                self.atype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1690
                self.match(HaskellParser.Atsign)
                self.state = 1691
                self.atype()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1692
                self.qtyconop()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1693
                self.tyvarop()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1694
                self.match(HaskellParser.Quote)
                self.state = 1695
                self.qconop()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1696
                self.match(HaskellParser.Quote)
                self.state = 1697
                self.varop()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1698
                self.unpackedness()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ntgtycon(self):
            return self.getTypedRuleContext(HaskellParser.NtgtyconContext,0)


        def tyvar(self):
            return self.getTypedRuleContext(HaskellParser.TyvarContext,0)


        def Asterisk(self):
            return self.getToken(HaskellParser.Asterisk, 0)

        def Tilde(self):
            return self.getToken(HaskellParser.Tilde, 0)

        def atype(self):
            return self.getTypedRuleContext(HaskellParser.AtypeContext,0)


        def Bang(self):
            return self.getToken(HaskellParser.Bang, 0)

        def OCURLY(self):
            return self.getToken(HaskellParser.OCURLY, 0)

        def CCURLY(self):
            return self.getToken(HaskellParser.CCURLY, 0)

        def fielddecls(self):
            return self.getTypedRuleContext(HaskellParser.FielddeclsContext,0)


        def OpenRoundBracket(self):
            return self.getToken(HaskellParser.OpenRoundBracket, 0)

        def CloseRoundBracket(self):
            return self.getToken(HaskellParser.CloseRoundBracket, 0)

        def ktype(self):
            return self.getTypedRuleContext(HaskellParser.KtypeContext,0)


        def Comma(self):
            return self.getToken(HaskellParser.Comma, 0)

        def comma_types(self):
            return self.getTypedRuleContext(HaskellParser.Comma_typesContext,0)


        def OpenBoxParen(self):
            return self.getToken(HaskellParser.OpenBoxParen, 0)

        def CloseBoxParen(self):
            return self.getToken(HaskellParser.CloseBoxParen, 0)

        def bar_types2(self):
            return self.getTypedRuleContext(HaskellParser.Bar_types2Context,0)


        def OpenSquareBracket(self):
            return self.getToken(HaskellParser.OpenSquareBracket, 0)

        def CloseSquareBracket(self):
            return self.getToken(HaskellParser.CloseSquareBracket, 0)

        def quasiquote(self):
            return self.getTypedRuleContext(HaskellParser.QuasiquoteContext,0)


        def splice_untyped(self):
            return self.getTypedRuleContext(HaskellParser.Splice_untypedContext,0)


        def Quote(self):
            return self.getToken(HaskellParser.Quote, 0)

        def qcon_nowiredlist(self):
            return self.getTypedRuleContext(HaskellParser.Qcon_nowiredlistContext,0)


        def var(self):
            return self.getTypedRuleContext(HaskellParser.VarContext,0)


        def integer(self):
            return self.getTypedRuleContext(HaskellParser.IntegerContext,0)


        def pstring(self):
            return self.getTypedRuleContext(HaskellParser.PstringContext,0)


        def WILDCARD(self):
            return self.getToken(HaskellParser.WILDCARD, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_atype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtype" ):
                listener.enterAtype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtype" ):
                listener.exitAtype(self)




    def atype(self):

        localctx = HaskellParser.AtypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 218, self.RULE_atype)
        self._la = 0 # Token type
        try:
            self.state = 1767
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,201,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1701
                self.ntgtycon()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1702
                self.tyvar()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1703
                self.match(HaskellParser.Asterisk)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1704
                self.match(HaskellParser.Tilde)
                self.state = 1705
                self.atype()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 1706
                self.match(HaskellParser.Bang)
                self.state = 1707
                self.atype()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 1708
                self.match(HaskellParser.OCURLY)
                self.state = 1710
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or _la==HaskellParser.OpenRoundBracket or _la==HaskellParser.VARID:
                    self.state = 1709
                    self.fielddecls()


                self.state = 1712
                self.match(HaskellParser.CCURLY)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 1713
                self.match(HaskellParser.OpenRoundBracket)
                self.state = 1714
                self.match(HaskellParser.CloseRoundBracket)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 1715
                self.match(HaskellParser.OpenRoundBracket)
                self.state = 1716
                self.ktype()
                self.state = 1717
                self.match(HaskellParser.Comma)
                self.state = 1718
                self.comma_types()
                self.state = 1719
                self.match(HaskellParser.CloseRoundBracket)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 1721
                self.match(HaskellParser.OpenBoxParen)
                self.state = 1722
                self.match(HaskellParser.CloseBoxParen)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 1723
                self.match(HaskellParser.OpenBoxParen)
                self.state = 1724
                self.comma_types()
                self.state = 1725
                self.match(HaskellParser.CloseBoxParen)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 1727
                self.match(HaskellParser.OpenBoxParen)
                self.state = 1728
                self.bar_types2()
                self.state = 1729
                self.match(HaskellParser.CloseBoxParen)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 1731
                self.match(HaskellParser.OpenSquareBracket)
                self.state = 1732
                self.ktype()
                self.state = 1733
                self.match(HaskellParser.CloseSquareBracket)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 1735
                self.match(HaskellParser.OpenRoundBracket)
                self.state = 1736
                self.ktype()
                self.state = 1737
                self.match(HaskellParser.CloseRoundBracket)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 1739
                self.quasiquote()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 1740
                self.splice_untyped()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 1741
                self.match(HaskellParser.Quote)
                self.state = 1742
                self.qcon_nowiredlist()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 1743
                self.match(HaskellParser.Quote)
                self.state = 1744
                self.match(HaskellParser.OpenRoundBracket)
                self.state = 1745
                self.ktype()
                self.state = 1746
                self.match(HaskellParser.Comma)
                self.state = 1747
                self.comma_types()
                self.state = 1748
                self.match(HaskellParser.CloseRoundBracket)
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 1750
                self.match(HaskellParser.Quote)
                self.state = 1751
                self.match(HaskellParser.OpenSquareBracket)
                self.state = 1753
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.WILDCARD) | (1 << HaskellParser.FORALL) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 82)) & ~0x3f) == 0 and ((1 << (_la - 82)) & ((1 << (HaskellParser.Hash - 82)) | (1 << (HaskellParser.Less - 82)) | (1 << (HaskellParser.Greater - 82)) | (1 << (HaskellParser.Ampersand - 82)) | (1 << (HaskellParser.Pipe - 82)) | (1 << (HaskellParser.Bang - 82)) | (1 << (HaskellParser.Caret - 82)) | (1 << (HaskellParser.Plus - 82)) | (1 << (HaskellParser.Minus - 82)) | (1 << (HaskellParser.Asterisk - 82)) | (1 << (HaskellParser.Percent - 82)) | (1 << (HaskellParser.Divide - 82)) | (1 << (HaskellParser.Tilde - 82)) | (1 << (HaskellParser.Atsign - 82)) | (1 << (HaskellParser.Dollar - 82)) | (1 << (HaskellParser.Dot - 82)) | (1 << (HaskellParser.QuestionMark - 82)) | (1 << (HaskellParser.Colon - 82)) | (1 << (HaskellParser.Eq - 82)) | (1 << (HaskellParser.Quote - 82)) | (1 << (HaskellParser.ReverseSlash - 82)) | (1 << (HaskellParser.BackQuote - 82)) | (1 << (HaskellParser.OpenBoxParen - 82)) | (1 << (HaskellParser.OpenRoundBracket - 82)) | (1 << (HaskellParser.OpenSquareBracket - 82)) | (1 << (HaskellParser.STRING - 82)) | (1 << (HaskellParser.VARID - 82)) | (1 << (HaskellParser.CONID - 82)) | (1 << (HaskellParser.OpenPragmaBracket - 82)) | (1 << (HaskellParser.OCURLY - 82)) | (1 << (HaskellParser.DECIMAL - 82)) | (1 << (HaskellParser.OCTAL - 82)) | (1 << (HaskellParser.HEXADECIMAL - 82)))) != 0):
                    self.state = 1752
                    self.comma_types()


                self.state = 1755
                self.match(HaskellParser.CloseSquareBracket)
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 1756
                self.match(HaskellParser.Quote)
                self.state = 1757
                self.var()
                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 1758
                self.match(HaskellParser.OpenSquareBracket)
                self.state = 1759
                self.ktype()
                self.state = 1760
                self.match(HaskellParser.Comma)
                self.state = 1761
                self.comma_types()
                self.state = 1762
                self.match(HaskellParser.CloseSquareBracket)
                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
                self.state = 1764
                self.integer()
                pass

            elif la_ == 22:
                self.enterOuterAlt(localctx, 22)
                self.state = 1765
                self.pstring()
                pass

            elif la_ == 23:
                self.enterOuterAlt(localctx, 23)
                self.state = 1766
                self.match(HaskellParser.WILDCARD)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inst_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sigtype(self):
            return self.getTypedRuleContext(HaskellParser.SigtypeContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_inst_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInst_type" ):
                listener.enterInst_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInst_type" ):
                listener.exitInst_type(self)




    def inst_type(self):

        localctx = HaskellParser.Inst_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 220, self.RULE_inst_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1769
            self.sigtype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Deriv_typesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ktypedoc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.KtypedocContext)
            else:
                return self.getTypedRuleContext(HaskellParser.KtypedocContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Comma)
            else:
                return self.getToken(HaskellParser.Comma, i)

        def getRuleIndex(self):
            return HaskellParser.RULE_deriv_types

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeriv_types" ):
                listener.enterDeriv_types(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeriv_types" ):
                listener.exitDeriv_types(self)




    def deriv_types(self):

        localctx = HaskellParser.Deriv_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 222, self.RULE_deriv_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1771
            self.ktypedoc()
            self.state = 1776
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Comma:
                self.state = 1772
                self.match(HaskellParser.Comma)
                self.state = 1773
                self.ktypedoc()
                self.state = 1778
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comma_typesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ktype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.KtypeContext)
            else:
                return self.getTypedRuleContext(HaskellParser.KtypeContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Comma)
            else:
                return self.getToken(HaskellParser.Comma, i)

        def getRuleIndex(self):
            return HaskellParser.RULE_comma_types

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComma_types" ):
                listener.enterComma_types(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComma_types" ):
                listener.exitComma_types(self)




    def comma_types(self):

        localctx = HaskellParser.Comma_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 224, self.RULE_comma_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1779
            self.ktype()
            self.state = 1784
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Comma:
                self.state = 1780
                self.match(HaskellParser.Comma)
                self.state = 1781
                self.ktype()
                self.state = 1786
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Bar_types2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ktype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.KtypeContext)
            else:
                return self.getTypedRuleContext(HaskellParser.KtypeContext,i)


        def Pipe(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Pipe)
            else:
                return self.getToken(HaskellParser.Pipe, i)

        def getRuleIndex(self):
            return HaskellParser.RULE_bar_types2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBar_types2" ):
                listener.enterBar_types2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBar_types2" ):
                listener.exitBar_types2(self)




    def bar_types2(self):

        localctx = HaskellParser.Bar_types2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 226, self.RULE_bar_types2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1787
            self.ktype()
            self.state = 1788
            self.match(HaskellParser.Pipe)
            self.state = 1789
            self.ktype()
            self.state = 1794
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Pipe:
                self.state = 1790
                self.match(HaskellParser.Pipe)
                self.state = 1791
                self.ktype()
                self.state = 1796
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tv_bndrsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tv_bndr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.Tv_bndrContext)
            else:
                return self.getTypedRuleContext(HaskellParser.Tv_bndrContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_tv_bndrs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTv_bndrs" ):
                listener.enterTv_bndrs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTv_bndrs" ):
                listener.exitTv_bndrs(self)




    def tv_bndrs(self):

        localctx = HaskellParser.Tv_bndrsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 228, self.RULE_tv_bndrs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1798 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1797
                self.tv_bndr()
                self.state = 1800 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 120)) & ~0x3f) == 0 and ((1 << (_la - 120)) & ((1 << (HaskellParser.OpenRoundBracket - 120)) | (1 << (HaskellParser.VARID - 120)) | (1 << (HaskellParser.OCURLY - 120)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tv_bndrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tv_bndr_no_braces(self):
            return self.getTypedRuleContext(HaskellParser.Tv_bndr_no_bracesContext,0)


        def OCURLY(self):
            return self.getToken(HaskellParser.OCURLY, 0)

        def tyvar(self):
            return self.getTypedRuleContext(HaskellParser.TyvarContext,0)


        def CCURLY(self):
            return self.getToken(HaskellParser.CCURLY, 0)

        def DoubleColon(self):
            return self.getToken(HaskellParser.DoubleColon, 0)

        def kind(self):
            return self.getTypedRuleContext(HaskellParser.KindContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_tv_bndr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTv_bndr" ):
                listener.enterTv_bndr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTv_bndr" ):
                listener.exitTv_bndr(self)




    def tv_bndr(self):

        localctx = HaskellParser.Tv_bndrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 230, self.RULE_tv_bndr)
        try:
            self.state = 1813
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,206,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1802
                self.tv_bndr_no_braces()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1803
                self.match(HaskellParser.OCURLY)
                self.state = 1804
                self.tyvar()
                self.state = 1805
                self.match(HaskellParser.CCURLY)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1807
                self.match(HaskellParser.OCURLY)
                self.state = 1808
                self.tyvar()
                self.state = 1809
                self.match(HaskellParser.DoubleColon)
                self.state = 1810
                self.kind()
                self.state = 1811
                self.match(HaskellParser.CCURLY)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tv_bndr_no_bracesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tyvar(self):
            return self.getTypedRuleContext(HaskellParser.TyvarContext,0)


        def OpenRoundBracket(self):
            return self.getToken(HaskellParser.OpenRoundBracket, 0)

        def DoubleColon(self):
            return self.getToken(HaskellParser.DoubleColon, 0)

        def kind(self):
            return self.getTypedRuleContext(HaskellParser.KindContext,0)


        def CloseRoundBracket(self):
            return self.getToken(HaskellParser.CloseRoundBracket, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_tv_bndr_no_braces

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTv_bndr_no_braces" ):
                listener.enterTv_bndr_no_braces(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTv_bndr_no_braces" ):
                listener.exitTv_bndr_no_braces(self)




    def tv_bndr_no_braces(self):

        localctx = HaskellParser.Tv_bndr_no_bracesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 232, self.RULE_tv_bndr_no_braces)
        try:
            self.state = 1822
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.AS, HaskellParser.HIDING, HaskellParser.QUALIFIED, HaskellParser.EXPORT, HaskellParser.STDCALL, HaskellParser.CCALL, HaskellParser.CAPI, HaskellParser.JSCALL, HaskellParser.STOCK, HaskellParser.ANYCLASS, HaskellParser.VIA, HaskellParser.VARID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1815
                self.tyvar()
                pass
            elif token in [HaskellParser.OpenRoundBracket]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1816
                self.match(HaskellParser.OpenRoundBracket)
                self.state = 1817
                self.tyvar()
                self.state = 1818
                self.match(HaskellParser.DoubleColon)
                self.state = 1819
                self.kind()
                self.state = 1820
                self.match(HaskellParser.CloseRoundBracket)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FdsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Pipe(self):
            return self.getToken(HaskellParser.Pipe, 0)

        def fds1(self):
            return self.getTypedRuleContext(HaskellParser.Fds1Context,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_fds

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFds" ):
                listener.enterFds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFds" ):
                listener.exitFds(self)




    def fds(self):

        localctx = HaskellParser.FdsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 234, self.RULE_fds)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1824
            self.match(HaskellParser.Pipe)
            self.state = 1825
            self.fds1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fds1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.FdContext)
            else:
                return self.getTypedRuleContext(HaskellParser.FdContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Comma)
            else:
                return self.getToken(HaskellParser.Comma, i)

        def getRuleIndex(self):
            return HaskellParser.RULE_fds1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFds1" ):
                listener.enterFds1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFds1" ):
                listener.exitFds1(self)




    def fds1(self):

        localctx = HaskellParser.Fds1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 236, self.RULE_fds1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1827
            self.fd()
            self.state = 1832
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Comma:
                self.state = 1828
                self.match(HaskellParser.Comma)
                self.state = 1829
                self.fd()
                self.state = 1834
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Arrow(self):
            return self.getToken(HaskellParser.Arrow, 0)

        def varids0(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.Varids0Context)
            else:
                return self.getTypedRuleContext(HaskellParser.Varids0Context,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_fd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFd" ):
                listener.enterFd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFd" ):
                listener.exitFd(self)




    def fd(self):

        localctx = HaskellParser.FdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 238, self.RULE_fd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1836
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or _la==HaskellParser.VARID:
                self.state = 1835
                self.varids0()


            self.state = 1838
            self.match(HaskellParser.Arrow)
            self.state = 1840
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or _la==HaskellParser.VARID:
                self.state = 1839
                self.varids0()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Varids0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tyvar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.TyvarContext)
            else:
                return self.getTypedRuleContext(HaskellParser.TyvarContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_varids0

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarids0" ):
                listener.enterVarids0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarids0" ):
                listener.exitVarids0(self)




    def varids0(self):

        localctx = HaskellParser.Varids0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 240, self.RULE_varids0)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1843 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1842
                self.tyvar()
                self.state = 1845 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or _la==HaskellParser.VARID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class KindContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ctype(self):
            return self.getTypedRuleContext(HaskellParser.CtypeContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_kind

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKind" ):
                listener.enterKind(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKind" ):
                listener.exitKind(self)




    def kind(self):

        localctx = HaskellParser.KindContext(self, self._ctx, self.state)
        self.enterRule(localctx, 242, self.RULE_kind)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1847
            self.ctype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Gadt_constrlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(HaskellParser.WHERE, 0)

        def opn(self):
            return self.getTypedRuleContext(HaskellParser.OpnContext,0)


        def close(self):
            return self.getTypedRuleContext(HaskellParser.CloseContext,0)


        def gadt_constrs(self):
            return self.getTypedRuleContext(HaskellParser.Gadt_constrsContext,0)


        def semi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.SemiContext)
            else:
                return self.getTypedRuleContext(HaskellParser.SemiContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_gadt_constrlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGadt_constrlist" ):
                listener.enterGadt_constrlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGadt_constrlist" ):
                listener.exitGadt_constrlist(self)




    def gadt_constrlist(self):

        localctx = HaskellParser.Gadt_constrlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 244, self.RULE_gadt_constrlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1849
            self.match(HaskellParser.WHERE)
            self.state = 1850
            self.opn()
            self.state = 1852
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 118)) & ~0x3f) == 0 and ((1 << (_la - 118)) & ((1 << (HaskellParser.OpenBoxParen - 118)) | (1 << (HaskellParser.OpenRoundBracket - 118)) | (1 << (HaskellParser.OpenSquareBracket - 118)) | (1 << (HaskellParser.CONID - 118)))) != 0):
                self.state = 1851
                self.gadt_constrs()


            self.state = 1857
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Semi or _la==HaskellParser.SEMI:
                self.state = 1854
                self.semi()
                self.state = 1859
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 1860
            self.close()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Gadt_constrsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def gadt_constr_with_doc(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.Gadt_constr_with_docContext)
            else:
                return self.getTypedRuleContext(HaskellParser.Gadt_constr_with_docContext,i)


        def semi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.SemiContext)
            else:
                return self.getTypedRuleContext(HaskellParser.SemiContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_gadt_constrs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGadt_constrs" ):
                listener.enterGadt_constrs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGadt_constrs" ):
                listener.exitGadt_constrs(self)




    def gadt_constrs(self):

        localctx = HaskellParser.Gadt_constrsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 246, self.RULE_gadt_constrs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1862
            self.gadt_constr_with_doc()
            self.state = 1868
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,214,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 1863
                    self.semi()
                    self.state = 1864
                    self.gadt_constr_with_doc() 
                self.state = 1870
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,214,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Gadt_constr_with_docContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def gadt_constr(self):
            return self.getTypedRuleContext(HaskellParser.Gadt_constrContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_gadt_constr_with_doc

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGadt_constr_with_doc" ):
                listener.enterGadt_constr_with_doc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGadt_constr_with_doc" ):
                listener.exitGadt_constr_with_doc(self)




    def gadt_constr_with_doc(self):

        localctx = HaskellParser.Gadt_constr_with_docContext(self, self._ctx, self.state)
        self.enterRule(localctx, 248, self.RULE_gadt_constr_with_doc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1871
            self.gadt_constr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Gadt_constrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def con_list(self):
            return self.getTypedRuleContext(HaskellParser.Con_listContext,0)


        def DoubleColon(self):
            return self.getToken(HaskellParser.DoubleColon, 0)

        def sigtypedoc(self):
            return self.getTypedRuleContext(HaskellParser.SigtypedocContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_gadt_constr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGadt_constr" ):
                listener.enterGadt_constr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGadt_constr" ):
                listener.exitGadt_constr(self)




    def gadt_constr(self):

        localctx = HaskellParser.Gadt_constrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 250, self.RULE_gadt_constr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1873
            self.con_list()
            self.state = 1874
            self.match(HaskellParser.DoubleColon)
            self.state = 1875
            self.sigtypedoc()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstrsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Eq(self):
            return self.getToken(HaskellParser.Eq, 0)

        def constrs1(self):
            return self.getTypedRuleContext(HaskellParser.Constrs1Context,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_constrs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstrs" ):
                listener.enterConstrs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstrs" ):
                listener.exitConstrs(self)




    def constrs(self):

        localctx = HaskellParser.ConstrsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 252, self.RULE_constrs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1877
            self.match(HaskellParser.Eq)
            self.state = 1878
            self.constrs1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constrs1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.ConstrContext)
            else:
                return self.getTypedRuleContext(HaskellParser.ConstrContext,i)


        def Pipe(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Pipe)
            else:
                return self.getToken(HaskellParser.Pipe, i)

        def getRuleIndex(self):
            return HaskellParser.RULE_constrs1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstrs1" ):
                listener.enterConstrs1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstrs1" ):
                listener.exitConstrs1(self)




    def constrs1(self):

        localctx = HaskellParser.Constrs1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 254, self.RULE_constrs1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1880
            self.constr()
            self.state = 1885
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Pipe:
                self.state = 1881
                self.match(HaskellParser.Pipe)
                self.state = 1882
                self.constr()
                self.state = 1887
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constr_stuff(self):
            return self.getTypedRuleContext(HaskellParser.Constr_stuffContext,0)


        def forall(self):
            return self.getTypedRuleContext(HaskellParser.ForallContext,0)


        def constr_context(self):
            return self.getTypedRuleContext(HaskellParser.Constr_contextContext,0)


        def DoubleArrow(self):
            return self.getToken(HaskellParser.DoubleArrow, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_constr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstr" ):
                listener.enterConstr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstr" ):
                listener.exitConstr(self)




    def constr(self):

        localctx = HaskellParser.ConstrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 256, self.RULE_constr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1889
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HaskellParser.FORALL:
                self.state = 1888
                self.forall()


            self.state = 1894
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,217,self._ctx)
            if la_ == 1:
                self.state = 1891
                self.constr_context()
                self.state = 1892
                self.match(HaskellParser.DoubleArrow)


            self.state = 1896
            self.constr_stuff()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FORALL(self):
            return self.getToken(HaskellParser.FORALL, 0)

        def Dot(self):
            return self.getToken(HaskellParser.Dot, 0)

        def tv_bndrs(self):
            return self.getTypedRuleContext(HaskellParser.Tv_bndrsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_forall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForall" ):
                listener.enterForall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForall" ):
                listener.exitForall(self)




    def forall(self):

        localctx = HaskellParser.ForallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 258, self.RULE_forall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1898
            self.match(HaskellParser.FORALL)
            self.state = 1900
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 120)) & ~0x3f) == 0 and ((1 << (_la - 120)) & ((1 << (HaskellParser.OpenRoundBracket - 120)) | (1 << (HaskellParser.VARID - 120)) | (1 << (HaskellParser.OCURLY - 120)))) != 0):
                self.state = 1899
                self.tv_bndrs()


            self.state = 1902
            self.match(HaskellParser.Dot)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Constr_stuffContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constr_tyapps(self):
            return self.getTypedRuleContext(HaskellParser.Constr_tyappsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_constr_stuff

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstr_stuff" ):
                listener.enterConstr_stuff(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstr_stuff" ):
                listener.exitConstr_stuff(self)




    def constr_stuff(self):

        localctx = HaskellParser.Constr_stuffContext(self, self._ctx, self.state)
        self.enterRule(localctx, 260, self.RULE_constr_stuff)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1904
            self.constr_tyapps()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FielddeclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fielddecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.FielddeclContext)
            else:
                return self.getTypedRuleContext(HaskellParser.FielddeclContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Comma)
            else:
                return self.getToken(HaskellParser.Comma, i)

        def getRuleIndex(self):
            return HaskellParser.RULE_fielddecls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFielddecls" ):
                listener.enterFielddecls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFielddecls" ):
                listener.exitFielddecls(self)




    def fielddecls(self):

        localctx = HaskellParser.FielddeclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 262, self.RULE_fielddecls)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1906
            self.fielddecl()
            self.state = 1911
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Comma:
                self.state = 1907
                self.match(HaskellParser.Comma)
                self.state = 1908
                self.fielddecl()
                self.state = 1913
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FielddeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sig_vars(self):
            return self.getTypedRuleContext(HaskellParser.Sig_varsContext,0)


        def DoubleColon(self):
            return self.getToken(HaskellParser.DoubleColon, 0)

        def ctype(self):
            return self.getTypedRuleContext(HaskellParser.CtypeContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_fielddecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFielddecl" ):
                listener.enterFielddecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFielddecl" ):
                listener.exitFielddecl(self)




    def fielddecl(self):

        localctx = HaskellParser.FielddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 264, self.RULE_fielddecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1914
            self.sig_vars()
            self.state = 1915
            self.match(HaskellParser.DoubleColon)
            self.state = 1916
            self.ctype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DerivingsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def deriving(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.DerivingContext)
            else:
                return self.getTypedRuleContext(HaskellParser.DerivingContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_derivings

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDerivings" ):
                listener.enterDerivings(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDerivings" ):
                listener.exitDerivings(self)




    def derivings(self):

        localctx = HaskellParser.DerivingsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 266, self.RULE_derivings)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1919 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1918
                self.deriving()
                self.state = 1921 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==HaskellParser.DERIVING):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DerivingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DERIVING(self):
            return self.getToken(HaskellParser.DERIVING, 0)

        def deriv_clause_types(self):
            return self.getTypedRuleContext(HaskellParser.Deriv_clause_typesContext,0)


        def deriv_strategy_no_via(self):
            return self.getTypedRuleContext(HaskellParser.Deriv_strategy_no_viaContext,0)


        def deriv_strategy_via(self):
            return self.getTypedRuleContext(HaskellParser.Deriv_strategy_viaContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_deriving

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeriving" ):
                listener.enterDeriving(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeriving" ):
                listener.exitDeriving(self)




    def deriving(self):

        localctx = HaskellParser.DerivingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 268, self.RULE_deriving)
        try:
            self.state = 1933
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,221,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1923
                self.match(HaskellParser.DERIVING)
                self.state = 1924
                self.deriv_clause_types()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1925
                self.match(HaskellParser.DERIVING)
                self.state = 1926
                self.deriv_strategy_no_via()
                self.state = 1927
                self.deriv_clause_types()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1929
                self.match(HaskellParser.DERIVING)
                self.state = 1930
                self.deriv_clause_types()
                self.state = 1931
                self.deriv_strategy_via()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Deriv_clause_typesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qtycon(self):
            return self.getTypedRuleContext(HaskellParser.QtyconContext,0)


        def OpenRoundBracket(self):
            return self.getToken(HaskellParser.OpenRoundBracket, 0)

        def CloseRoundBracket(self):
            return self.getToken(HaskellParser.CloseRoundBracket, 0)

        def deriv_types(self):
            return self.getTypedRuleContext(HaskellParser.Deriv_typesContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_deriv_clause_types

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeriv_clause_types" ):
                listener.enterDeriv_clause_types(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeriv_clause_types" ):
                listener.exitDeriv_clause_types(self)




    def deriv_clause_types(self):

        localctx = HaskellParser.Deriv_clause_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 270, self.RULE_deriv_clause_types)
        try:
            self.state = 1942
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,222,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1935
                self.qtycon()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1936
                self.match(HaskellParser.OpenRoundBracket)
                self.state = 1937
                self.match(HaskellParser.CloseRoundBracket)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1938
                self.match(HaskellParser.OpenRoundBracket)
                self.state = 1939
                self.deriv_types()
                self.state = 1940
                self.match(HaskellParser.CloseRoundBracket)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Decl_no_thContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sigdecl(self):
            return self.getTypedRuleContext(HaskellParser.SigdeclContext,0)


        def infixexp(self):
            return self.getTypedRuleContext(HaskellParser.InfixexpContext,0)


        def rhs(self):
            return self.getTypedRuleContext(HaskellParser.RhsContext,0)


        def opt_sig(self):
            return self.getTypedRuleContext(HaskellParser.Opt_sigContext,0)


        def pattern_synonym_decl(self):
            return self.getTypedRuleContext(HaskellParser.Pattern_synonym_declContext,0)


        def semi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.SemiContext)
            else:
                return self.getTypedRuleContext(HaskellParser.SemiContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_decl_no_th

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl_no_th" ):
                listener.enterDecl_no_th(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl_no_th" ):
                listener.exitDecl_no_th(self)




    def decl_no_th(self):

        localctx = HaskellParser.Decl_no_thContext(self, self._ctx, self.state)
        self.enterRule(localctx, 272, self.RULE_decl_no_th)
        self._la = 0 # Token type
        try:
            self.state = 1957
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,225,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1944
                self.sigdecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1945
                self.infixexp()
                self.state = 1947
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.DoubleColon:
                    self.state = 1946
                    self.opt_sig()


                self.state = 1949
                self.rhs()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1951
                self.pattern_synonym_decl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 1953 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 1952
                        self.semi()

                    else:
                        raise NoViableAltException(self)
                    self.state = 1955 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,224,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def decl_no_th(self):
            return self.getTypedRuleContext(HaskellParser.Decl_no_thContext,0)


        def splice_exp(self):
            return self.getTypedRuleContext(HaskellParser.Splice_expContext,0)


        def semi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.SemiContext)
            else:
                return self.getTypedRuleContext(HaskellParser.SemiContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDecl" ):
                listener.enterDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDecl" ):
                listener.exitDecl(self)




    def decl(self):

        localctx = HaskellParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 274, self.RULE_decl)
        try:
            self.state = 1966
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,227,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1959
                self.decl_no_th()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1960
                self.splice_exp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1962 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 1961
                        self.semi()

                    else:
                        raise NoViableAltException(self)
                    self.state = 1964 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,226,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Eq(self):
            return self.getToken(HaskellParser.Eq, 0)

        def exp(self):
            return self.getTypedRuleContext(HaskellParser.ExpContext,0)


        def wherebinds(self):
            return self.getTypedRuleContext(HaskellParser.WherebindsContext,0)


        def gdrhs(self):
            return self.getTypedRuleContext(HaskellParser.GdrhsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_rhs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRhs" ):
                listener.enterRhs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRhs" ):
                listener.exitRhs(self)




    def rhs(self):

        localctx = HaskellParser.RhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 276, self.RULE_rhs)
        self._la = 0 # Token type
        try:
            self.state = 1977
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.Eq]:
                self.enterOuterAlt(localctx, 1)
                self.state = 1968
                self.match(HaskellParser.Eq)
                self.state = 1969
                self.exp()
                self.state = 1971
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.WHERE:
                    self.state = 1970
                    self.wherebinds()


                pass
            elif token in [HaskellParser.Pipe]:
                self.enterOuterAlt(localctx, 2)
                self.state = 1973
                self.gdrhs()
                self.state = 1975
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.WHERE:
                    self.state = 1974
                    self.wherebinds()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GdrhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def gdrh(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.GdrhContext)
            else:
                return self.getTypedRuleContext(HaskellParser.GdrhContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_gdrhs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGdrhs" ):
                listener.enterGdrhs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGdrhs" ):
                listener.exitGdrhs(self)




    def gdrhs(self):

        localctx = HaskellParser.GdrhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 278, self.RULE_gdrhs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1980 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 1979
                self.gdrh()
                self.state = 1982 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==HaskellParser.Pipe):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GdrhContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Pipe(self):
            return self.getToken(HaskellParser.Pipe, 0)

        def guards(self):
            return self.getTypedRuleContext(HaskellParser.GuardsContext,0)


        def Eq(self):
            return self.getToken(HaskellParser.Eq, 0)

        def exp(self):
            return self.getTypedRuleContext(HaskellParser.ExpContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_gdrh

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGdrh" ):
                listener.enterGdrh(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGdrh" ):
                listener.exitGdrh(self)




    def gdrh(self):

        localctx = HaskellParser.GdrhContext(self, self._ctx, self.state)
        self.enterRule(localctx, 280, self.RULE_gdrh)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 1984
            self.match(HaskellParser.Pipe)
            self.state = 1985
            self.guards()
            self.state = 1986
            self.match(HaskellParser.Eq)
            self.state = 1987
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SigdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def infixexp(self):
            return self.getTypedRuleContext(HaskellParser.InfixexpContext,0)


        def DoubleColon(self):
            return self.getToken(HaskellParser.DoubleColon, 0)

        def sigtypedoc(self):
            return self.getTypedRuleContext(HaskellParser.SigtypedocContext,0)


        def var(self):
            return self.getTypedRuleContext(HaskellParser.VarContext,0)


        def Comma(self):
            return self.getToken(HaskellParser.Comma, 0)

        def sig_vars(self):
            return self.getTypedRuleContext(HaskellParser.Sig_varsContext,0)


        def fixity(self):
            return self.getTypedRuleContext(HaskellParser.FixityContext,0)


        def ops(self):
            return self.getTypedRuleContext(HaskellParser.OpsContext,0)


        def integer(self):
            return self.getTypedRuleContext(HaskellParser.IntegerContext,0)


        def pattern_synonym_sig(self):
            return self.getTypedRuleContext(HaskellParser.Pattern_synonym_sigContext,0)


        def OpenPragmaBracket(self):
            return self.getToken(HaskellParser.OpenPragmaBracket, 0)

        def COMPLETE(self):
            return self.getToken(HaskellParser.COMPLETE, 0)

        def con_list(self):
            return self.getTypedRuleContext(HaskellParser.Con_listContext,0)


        def ClosePragmaBracket(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.ClosePragmaBracket)
            else:
                return self.getToken(HaskellParser.ClosePragmaBracket, i)

        def opt_tyconsig(self):
            return self.getTypedRuleContext(HaskellParser.Opt_tyconsigContext,0)


        def INLINE(self):
            return self.getToken(HaskellParser.INLINE, 0)

        def qvar(self):
            return self.getTypedRuleContext(HaskellParser.QvarContext,0)


        def activation(self):
            return self.getTypedRuleContext(HaskellParser.ActivationContext,0)


        def SCC(self):
            return self.getToken(HaskellParser.SCC, 0)

        def pstring(self):
            return self.getTypedRuleContext(HaskellParser.PstringContext,0)


        def SPECIALISE(self):
            return self.getToken(HaskellParser.SPECIALISE, 0)

        def sigtypes1(self):
            return self.getTypedRuleContext(HaskellParser.Sigtypes1Context,0)


        def SPECINLINE(self):
            return self.getToken(HaskellParser.SPECINLINE, 0)

        def INSTANCE(self):
            return self.getToken(HaskellParser.INSTANCE, 0)

        def inst_type(self):
            return self.getTypedRuleContext(HaskellParser.Inst_typeContext,0)


        def MINIMAL(self):
            return self.getToken(HaskellParser.MINIMAL, 0)

        def name_boolformula_opt(self):
            return self.getTypedRuleContext(HaskellParser.Name_boolformula_optContext,0)


        def semi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.SemiContext)
            else:
                return self.getTypedRuleContext(HaskellParser.SemiContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_sigdecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSigdecl" ):
                listener.enterSigdecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSigdecl" ):
                listener.exitSigdecl(self)




    def sigdecl(self):

        localctx = HaskellParser.SigdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 282, self.RULE_sigdecl)
        self._la = 0 # Token type
        try:
            self.state = 2068
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,240,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 1989
                self.infixexp()
                self.state = 1990
                self.match(HaskellParser.DoubleColon)
                self.state = 1991
                self.sigtypedoc()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 1993
                self.var()
                self.state = 1994
                self.match(HaskellParser.Comma)
                self.state = 1995
                self.sig_vars()
                self.state = 1996
                self.match(HaskellParser.DoubleColon)
                self.state = 1997
                self.sigtypedoc()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 1999
                self.fixity()
                self.state = 2001
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if ((((_la - 137)) & ~0x3f) == 0 and ((1 << (_la - 137)) & ((1 << (HaskellParser.DECIMAL - 137)) | (1 << (HaskellParser.OCTAL - 137)) | (1 << (HaskellParser.HEXADECIMAL - 137)))) != 0):
                    self.state = 2000
                    self.integer()


                self.state = 2003
                self.ops()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2005
                self.pattern_synonym_sig()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2006
                self.match(HaskellParser.OpenPragmaBracket)
                self.state = 2007
                self.match(HaskellParser.COMPLETE)
                self.state = 2008
                self.con_list()
                self.state = 2010
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.DoubleColon:
                    self.state = 2009
                    self.opt_tyconsig()


                self.state = 2012
                self.match(HaskellParser.ClosePragmaBracket)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 2014
                self.match(HaskellParser.OpenPragmaBracket)
                self.state = 2015
                self.match(HaskellParser.INLINE)
                self.state = 2017
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.OpenSquareBracket:
                    self.state = 2016
                    self.activation()


                self.state = 2019
                self.qvar()
                self.state = 2020
                self.match(HaskellParser.ClosePragmaBracket)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 2022
                self.match(HaskellParser.OpenPragmaBracket)
                self.state = 2023
                self.match(HaskellParser.SCC)
                self.state = 2024
                self.qvar()
                self.state = 2026
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.STRING:
                    self.state = 2025
                    self.pstring()


                self.state = 2028
                self.match(HaskellParser.ClosePragmaBracket)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 2030
                self.match(HaskellParser.OpenPragmaBracket)
                self.state = 2031
                self.match(HaskellParser.SPECIALISE)
                self.state = 2033
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.OpenSquareBracket:
                    self.state = 2032
                    self.activation()


                self.state = 2035
                self.qvar()
                self.state = 2036
                self.match(HaskellParser.DoubleColon)
                self.state = 2037
                self.sigtypes1()
                self.state = 2038
                self.match(HaskellParser.ClosePragmaBracket)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 2040
                self.match(HaskellParser.OpenPragmaBracket)
                self.state = 2041
                self.match(HaskellParser.SPECINLINE)
                self.state = 2043
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.OpenSquareBracket:
                    self.state = 2042
                    self.activation()


                self.state = 2045
                self.qvar()
                self.state = 2046
                self.match(HaskellParser.DoubleColon)
                self.state = 2047
                self.sigtypes1()
                self.state = 2048
                self.match(HaskellParser.ClosePragmaBracket)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 2050
                self.match(HaskellParser.OpenPragmaBracket)
                self.state = 2051
                self.match(HaskellParser.SPECIALISE)
                self.state = 2052
                self.match(HaskellParser.INSTANCE)
                self.state = 2053
                self.inst_type()
                self.state = 2054
                self.match(HaskellParser.ClosePragmaBracket)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 2056
                self.match(HaskellParser.OpenPragmaBracket)
                self.state = 2057
                self.match(HaskellParser.MINIMAL)
                self.state = 2058
                self.match(HaskellParser.ClosePragmaBracket)
                self.state = 2060
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 118)) & ~0x3f) == 0 and ((1 << (_la - 118)) & ((1 << (HaskellParser.OpenBoxParen - 118)) | (1 << (HaskellParser.OpenRoundBracket - 118)) | (1 << (HaskellParser.OpenSquareBracket - 118)) | (1 << (HaskellParser.VARID - 118)) | (1 << (HaskellParser.CONID - 118)))) != 0):
                    self.state = 2059
                    self.name_boolformula_opt()


                self.state = 2062
                self.match(HaskellParser.ClosePragmaBracket)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 2064 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 2063
                        self.semi()

                    else:
                        raise NoViableAltException(self)
                    self.state = 2066 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,239,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActivationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenSquareBracket(self):
            return self.getToken(HaskellParser.OpenSquareBracket, 0)

        def integer(self):
            return self.getTypedRuleContext(HaskellParser.IntegerContext,0)


        def CloseSquareBracket(self):
            return self.getToken(HaskellParser.CloseSquareBracket, 0)

        def rule_activation_marker(self):
            return self.getTypedRuleContext(HaskellParser.Rule_activation_markerContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_activation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActivation" ):
                listener.enterActivation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActivation" ):
                listener.exitActivation(self)




    def activation(self):

        localctx = HaskellParser.ActivationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 284, self.RULE_activation)
        try:
            self.state = 2079
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,241,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2070
                self.match(HaskellParser.OpenSquareBracket)
                self.state = 2071
                self.integer()
                self.state = 2072
                self.match(HaskellParser.CloseSquareBracket)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2074
                self.match(HaskellParser.OpenSquareBracket)
                self.state = 2075
                self.rule_activation_marker()
                self.state = 2076
                self.integer()
                self.state = 2077
                self.match(HaskellParser.CloseSquareBracket)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Th_quasiquoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenSquareBracket(self):
            return self.getToken(HaskellParser.OpenSquareBracket, 0)

        def varid(self):
            return self.getTypedRuleContext(HaskellParser.VaridContext,0)


        def Pipe(self):
            return self.getToken(HaskellParser.Pipe, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_th_quasiquote

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTh_quasiquote" ):
                listener.enterTh_quasiquote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTh_quasiquote" ):
                listener.exitTh_quasiquote(self)




    def th_quasiquote(self):

        localctx = HaskellParser.Th_quasiquoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 286, self.RULE_th_quasiquote)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2081
            self.match(HaskellParser.OpenSquareBracket)
            self.state = 2082
            self.varid()
            self.state = 2083
            self.match(HaskellParser.Pipe)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Th_qquasiquoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenSquareBracket(self):
            return self.getToken(HaskellParser.OpenSquareBracket, 0)

        def qvarid(self):
            return self.getTypedRuleContext(HaskellParser.QvaridContext,0)


        def Pipe(self):
            return self.getToken(HaskellParser.Pipe, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_th_qquasiquote

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTh_qquasiquote" ):
                listener.enterTh_qquasiquote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTh_qquasiquote" ):
                listener.exitTh_qquasiquote(self)




    def th_qquasiquote(self):

        localctx = HaskellParser.Th_qquasiquoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 288, self.RULE_th_qquasiquote)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2085
            self.match(HaskellParser.OpenSquareBracket)
            self.state = 2086
            self.qvarid()
            self.state = 2087
            self.match(HaskellParser.Pipe)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuasiquoteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def th_quasiquote(self):
            return self.getTypedRuleContext(HaskellParser.Th_quasiquoteContext,0)


        def th_qquasiquote(self):
            return self.getTypedRuleContext(HaskellParser.Th_qquasiquoteContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_quasiquote

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuasiquote" ):
                listener.enterQuasiquote(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuasiquote" ):
                listener.exitQuasiquote(self)




    def quasiquote(self):

        localctx = HaskellParser.QuasiquoteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 290, self.RULE_quasiquote)
        try:
            self.state = 2091
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,242,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2089
                self.th_quasiquote()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2090
                self.th_qquasiquote()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def infixexp(self):
            return self.getTypedRuleContext(HaskellParser.InfixexpContext,0)


        def DoubleColon(self):
            return self.getToken(HaskellParser.DoubleColon, 0)

        def sigtype(self):
            return self.getTypedRuleContext(HaskellParser.SigtypeContext,0)


        def LarrowTail(self):
            return self.getToken(HaskellParser.LarrowTail, 0)

        def exp(self):
            return self.getTypedRuleContext(HaskellParser.ExpContext,0)


        def RarrowTail(self):
            return self.getToken(HaskellParser.RarrowTail, 0)

        def LLarrowTail(self):
            return self.getToken(HaskellParser.LLarrowTail, 0)

        def RRarrowTail(self):
            return self.getToken(HaskellParser.RRarrowTail, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)




    def exp(self):

        localctx = HaskellParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 292, self.RULE_exp)
        try:
            self.state = 2114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,243,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2093
                self.infixexp()
                self.state = 2094
                self.match(HaskellParser.DoubleColon)
                self.state = 2095
                self.sigtype()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2097
                self.infixexp()
                self.state = 2098
                self.match(HaskellParser.LarrowTail)
                self.state = 2099
                self.exp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2101
                self.infixexp()
                self.state = 2102
                self.match(HaskellParser.RarrowTail)
                self.state = 2103
                self.exp()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2105
                self.infixexp()
                self.state = 2106
                self.match(HaskellParser.LLarrowTail)
                self.state = 2107
                self.exp()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2109
                self.infixexp()
                self.state = 2110
                self.match(HaskellParser.RRarrowTail)
                self.state = 2111
                self.exp()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 2113
                self.infixexp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InfixexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp10(self):
            return self.getTypedRuleContext(HaskellParser.Exp10Context,0)


        def qop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.QopContext)
            else:
                return self.getTypedRuleContext(HaskellParser.QopContext,i)


        def exp10p(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.Exp10pContext)
            else:
                return self.getTypedRuleContext(HaskellParser.Exp10pContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_infixexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInfixexp" ):
                listener.enterInfixexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInfixexp" ):
                listener.exitInfixexp(self)




    def infixexp(self):

        localctx = HaskellParser.InfixexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 294, self.RULE_infixexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2116
            self.exp10()
            self.state = 2122
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,244,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2117
                    self.qop()
                    self.state = 2118
                    self.exp10p() 
                self.state = 2124
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,244,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp10pContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp10(self):
            return self.getTypedRuleContext(HaskellParser.Exp10Context,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_exp10p

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp10p" ):
                listener.enterExp10p(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp10p" ):
                listener.exitExp10p(self)




    def exp10p(self):

        localctx = HaskellParser.Exp10pContext(self, self._ctx, self.state)
        self.enterRule(localctx, 296, self.RULE_exp10p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2125
            self.exp10()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fexp(self):
            return self.getTypedRuleContext(HaskellParser.FexpContext,0)


        def Minus(self):
            return self.getToken(HaskellParser.Minus, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_exp10

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp10" ):
                listener.enterExp10(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp10" ):
                listener.exitExp10(self)




    def exp10(self):

        localctx = HaskellParser.Exp10Context(self, self._ctx, self.state)
        self.enterRule(localctx, 298, self.RULE_exp10)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HaskellParser.Minus:
                self.state = 2127
                self.match(HaskellParser.Minus)


            self.state = 2130
            self.fexp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aexp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.AexpContext)
            else:
                return self.getTypedRuleContext(HaskellParser.AexpContext,i)


        def Atsign(self):
            return self.getToken(HaskellParser.Atsign, 0)

        def atype(self):
            return self.getTypedRuleContext(HaskellParser.AtypeContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_fexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFexp" ):
                listener.enterFexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFexp" ):
                listener.exitFexp(self)




    def fexp(self):

        localctx = HaskellParser.FexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 300, self.RULE_fexp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2133 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 2132
                    self.aexp()

                else:
                    raise NoViableAltException(self)
                self.state = 2135 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,246,self._ctx)

            self.state = 2139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,247,self._ctx)
            if la_ == 1:
                self.state = 2137
                self.match(HaskellParser.Atsign)
                self.state = 2138
                self.atype()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qvar(self):
            return self.getTypedRuleContext(HaskellParser.QvarContext,0)


        def Atsign(self):
            return self.getToken(HaskellParser.Atsign, 0)

        def aexp(self):
            return self.getTypedRuleContext(HaskellParser.AexpContext,0)


        def Tilde(self):
            return self.getToken(HaskellParser.Tilde, 0)

        def Bang(self):
            return self.getToken(HaskellParser.Bang, 0)

        def ReverseSlash(self):
            return self.getToken(HaskellParser.ReverseSlash, 0)

        def apats(self):
            return self.getTypedRuleContext(HaskellParser.ApatsContext,0)


        def Arrow(self):
            return self.getToken(HaskellParser.Arrow, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.ExpContext)
            else:
                return self.getTypedRuleContext(HaskellParser.ExpContext,i)


        def LET(self):
            return self.getToken(HaskellParser.LET, 0)

        def decllist(self):
            return self.getTypedRuleContext(HaskellParser.DecllistContext,0)


        def IN(self):
            return self.getToken(HaskellParser.IN, 0)

        def LCASE(self):
            return self.getToken(HaskellParser.LCASE, 0)

        def alts(self):
            return self.getTypedRuleContext(HaskellParser.AltsContext,0)


        def IF(self):
            return self.getToken(HaskellParser.IF, 0)

        def THEN(self):
            return self.getToken(HaskellParser.THEN, 0)

        def ELSE(self):
            return self.getToken(HaskellParser.ELSE, 0)

        def semi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.SemiContext)
            else:
                return self.getTypedRuleContext(HaskellParser.SemiContext,i)


        def ifgdpats(self):
            return self.getTypedRuleContext(HaskellParser.IfgdpatsContext,0)


        def CASE(self):
            return self.getToken(HaskellParser.CASE, 0)

        def OF(self):
            return self.getToken(HaskellParser.OF, 0)

        def DO(self):
            return self.getToken(HaskellParser.DO, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(HaskellParser.StmtlistContext,0)


        def MDO(self):
            return self.getToken(HaskellParser.MDO, 0)

        def aexp1(self):
            return self.getTypedRuleContext(HaskellParser.Aexp1Context,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_aexp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAexp" ):
                listener.enterAexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAexp" ):
                listener.exitAexp(self)




    def aexp(self):

        localctx = HaskellParser.AexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 302, self.RULE_aexp)
        self._la = 0 # Token type
        try:
            self.state = 2186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,250,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2141
                self.qvar()
                self.state = 2142
                self.match(HaskellParser.Atsign)
                self.state = 2143
                self.aexp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2145
                self.match(HaskellParser.Tilde)
                self.state = 2146
                self.aexp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2147
                self.match(HaskellParser.Bang)
                self.state = 2148
                self.aexp()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2149
                self.match(HaskellParser.ReverseSlash)
                self.state = 2150
                self.apats()
                self.state = 2151
                self.match(HaskellParser.Arrow)
                self.state = 2152
                self.exp()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2154
                self.match(HaskellParser.LET)
                self.state = 2155
                self.decllist()
                self.state = 2156
                self.match(HaskellParser.IN)
                self.state = 2157
                self.exp()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 2159
                self.match(HaskellParser.LCASE)
                self.state = 2160
                self.alts()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 2161
                self.match(HaskellParser.IF)
                self.state = 2162
                self.exp()
                self.state = 2164
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.Semi or _la==HaskellParser.SEMI:
                    self.state = 2163
                    self.semi()


                self.state = 2166
                self.match(HaskellParser.THEN)
                self.state = 2167
                self.exp()
                self.state = 2169
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.Semi or _la==HaskellParser.SEMI:
                    self.state = 2168
                    self.semi()


                self.state = 2171
                self.match(HaskellParser.ELSE)
                self.state = 2172
                self.exp()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 2174
                self.match(HaskellParser.IF)
                self.state = 2175
                self.ifgdpats()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 2176
                self.match(HaskellParser.CASE)
                self.state = 2177
                self.exp()
                self.state = 2178
                self.match(HaskellParser.OF)
                self.state = 2179
                self.alts()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 2181
                self.match(HaskellParser.DO)
                self.state = 2182
                self.stmtlist()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 2183
                self.match(HaskellParser.MDO)
                self.state = 2184
                self.stmtlist()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 2185
                self.aexp1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Aexp1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aexp2(self):
            return self.getTypedRuleContext(HaskellParser.Aexp2Context,0)


        def OCURLY(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.OCURLY)
            else:
                return self.getToken(HaskellParser.OCURLY, i)

        def CCURLY(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.CCURLY)
            else:
                return self.getToken(HaskellParser.CCURLY, i)

        def fbinds(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.FbindsContext)
            else:
                return self.getTypedRuleContext(HaskellParser.FbindsContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_aexp1

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAexp1" ):
                listener.enterAexp1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAexp1" ):
                listener.exitAexp1(self)




    def aexp1(self):

        localctx = HaskellParser.Aexp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 304, self.RULE_aexp1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2188
            self.aexp2()
            self.state = 2196
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,252,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2189
                    self.match(HaskellParser.OCURLY)
                    self.state = 2191
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 98)) & ~0x3f) == 0 and ((1 << (_la - 98)) & ((1 << (HaskellParser.DoubleDot - 98)) | (1 << (HaskellParser.OpenRoundBracket - 98)) | (1 << (HaskellParser.VARID - 98)) | (1 << (HaskellParser.CONID - 98)))) != 0):
                        self.state = 2190
                        self.fbinds()


                    self.state = 2193
                    self.match(HaskellParser.CCURLY) 
                self.state = 2198
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,252,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Aexp2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qvar(self):
            return self.getTypedRuleContext(HaskellParser.QvarContext,0)


        def qcon(self):
            return self.getTypedRuleContext(HaskellParser.QconContext,0)


        def varid(self):
            return self.getTypedRuleContext(HaskellParser.VaridContext,0)


        def literal(self):
            return self.getTypedRuleContext(HaskellParser.LiteralContext,0)


        def pstring(self):
            return self.getTypedRuleContext(HaskellParser.PstringContext,0)


        def integer(self):
            return self.getTypedRuleContext(HaskellParser.IntegerContext,0)


        def pfloat(self):
            return self.getTypedRuleContext(HaskellParser.PfloatContext,0)


        def OpenRoundBracket(self):
            return self.getToken(HaskellParser.OpenRoundBracket, 0)

        def texp(self):
            return self.getTypedRuleContext(HaskellParser.TexpContext,0)


        def CloseRoundBracket(self):
            return self.getToken(HaskellParser.CloseRoundBracket, 0)

        def tup_exprs(self):
            return self.getTypedRuleContext(HaskellParser.Tup_exprsContext,0)


        def OpenBoxParen(self):
            return self.getToken(HaskellParser.OpenBoxParen, 0)

        def CloseBoxParen(self):
            return self.getToken(HaskellParser.CloseBoxParen, 0)

        def OpenSquareBracket(self):
            return self.getToken(HaskellParser.OpenSquareBracket, 0)

        def lst(self):
            return self.getTypedRuleContext(HaskellParser.LstContext,0)


        def CloseSquareBracket(self):
            return self.getToken(HaskellParser.CloseSquareBracket, 0)

        def WILDCARD(self):
            return self.getToken(HaskellParser.WILDCARD, 0)

        def splice_untyped(self):
            return self.getTypedRuleContext(HaskellParser.Splice_untypedContext,0)


        def splice_typed(self):
            return self.getTypedRuleContext(HaskellParser.Splice_typedContext,0)


        def Quote(self):
            return self.getToken(HaskellParser.Quote, 0)

        def DoubleQuote(self):
            return self.getToken(HaskellParser.DoubleQuote, 0)

        def tyvar(self):
            return self.getTypedRuleContext(HaskellParser.TyvarContext,0)


        def gtycon(self):
            return self.getTypedRuleContext(HaskellParser.GtyconContext,0)


        def TopenExpQuote(self):
            return self.getToken(HaskellParser.TopenExpQuote, 0)

        def exp(self):
            return self.getTypedRuleContext(HaskellParser.ExpContext,0)


        def TcloseQoute(self):
            return self.getToken(HaskellParser.TcloseQoute, 0)

        def TopenTexpQuote(self):
            return self.getToken(HaskellParser.TopenTexpQuote, 0)

        def TcloseTExpQoute(self):
            return self.getToken(HaskellParser.TcloseTExpQoute, 0)

        def TopenTypQoute(self):
            return self.getToken(HaskellParser.TopenTypQoute, 0)

        def ktype(self):
            return self.getTypedRuleContext(HaskellParser.KtypeContext,0)


        def TopenPatQuote(self):
            return self.getToken(HaskellParser.TopenPatQuote, 0)

        def infixexp(self):
            return self.getTypedRuleContext(HaskellParser.InfixexpContext,0)


        def TopenDecQoute(self):
            return self.getToken(HaskellParser.TopenDecQoute, 0)

        def cvtopbody(self):
            return self.getTypedRuleContext(HaskellParser.CvtopbodyContext,0)


        def quasiquote(self):
            return self.getTypedRuleContext(HaskellParser.QuasiquoteContext,0)


        def AopenParen(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.AopenParen)
            else:
                return self.getToken(HaskellParser.AopenParen, i)

        def aexp(self):
            return self.getTypedRuleContext(HaskellParser.AexpContext,0)


        def cmdargs(self):
            return self.getTypedRuleContext(HaskellParser.CmdargsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_aexp2

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAexp2" ):
                listener.enterAexp2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAexp2" ):
                listener.exitAexp2(self)




    def aexp2(self):

        localctx = HaskellParser.Aexp2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 306, self.RULE_aexp2)
        try:
            self.state = 2266
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,254,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2199
                self.qvar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2200
                self.qcon()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2201
                self.varid()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2202
                self.literal()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2203
                self.pstring()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 2204
                self.integer()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 2205
                self.pfloat()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 2206
                self.match(HaskellParser.OpenRoundBracket)
                self.state = 2207
                self.texp()
                self.state = 2208
                self.match(HaskellParser.CloseRoundBracket)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 2210
                self.match(HaskellParser.OpenRoundBracket)
                self.state = 2211
                self.tup_exprs()
                self.state = 2212
                self.match(HaskellParser.CloseRoundBracket)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 2214
                self.match(HaskellParser.OpenBoxParen)
                self.state = 2215
                self.texp()
                self.state = 2216
                self.match(HaskellParser.CloseBoxParen)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 2218
                self.match(HaskellParser.OpenBoxParen)
                self.state = 2219
                self.tup_exprs()
                self.state = 2220
                self.match(HaskellParser.CloseBoxParen)
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 2222
                self.match(HaskellParser.OpenSquareBracket)
                self.state = 2223
                self.lst()
                self.state = 2224
                self.match(HaskellParser.CloseSquareBracket)
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 2226
                self.match(HaskellParser.WILDCARD)
                pass

            elif la_ == 14:
                self.enterOuterAlt(localctx, 14)
                self.state = 2227
                self.splice_untyped()
                pass

            elif la_ == 15:
                self.enterOuterAlt(localctx, 15)
                self.state = 2228
                self.splice_typed()
                pass

            elif la_ == 16:
                self.enterOuterAlt(localctx, 16)
                self.state = 2229
                self.match(HaskellParser.Quote)
                self.state = 2230
                self.qvar()
                pass

            elif la_ == 17:
                self.enterOuterAlt(localctx, 17)
                self.state = 2231
                self.match(HaskellParser.Quote)
                self.state = 2232
                self.qcon()
                pass

            elif la_ == 18:
                self.enterOuterAlt(localctx, 18)
                self.state = 2233
                self.match(HaskellParser.DoubleQuote)
                self.state = 2234
                self.tyvar()
                pass

            elif la_ == 19:
                self.enterOuterAlt(localctx, 19)
                self.state = 2235
                self.match(HaskellParser.DoubleQuote)
                self.state = 2236
                self.gtycon()
                pass

            elif la_ == 20:
                self.enterOuterAlt(localctx, 20)
                self.state = 2237
                self.match(HaskellParser.DoubleQuote)
                pass

            elif la_ == 21:
                self.enterOuterAlt(localctx, 21)
                self.state = 2238
                self.match(HaskellParser.TopenExpQuote)
                self.state = 2239
                self.exp()
                self.state = 2240
                self.match(HaskellParser.TcloseQoute)
                pass

            elif la_ == 22:
                self.enterOuterAlt(localctx, 22)
                self.state = 2242
                self.match(HaskellParser.TopenTexpQuote)
                self.state = 2243
                self.exp()
                self.state = 2244
                self.match(HaskellParser.TcloseTExpQoute)
                pass

            elif la_ == 23:
                self.enterOuterAlt(localctx, 23)
                self.state = 2246
                self.match(HaskellParser.TopenTypQoute)
                self.state = 2247
                self.ktype()
                self.state = 2248
                self.match(HaskellParser.TcloseQoute)
                pass

            elif la_ == 24:
                self.enterOuterAlt(localctx, 24)
                self.state = 2250
                self.match(HaskellParser.TopenPatQuote)
                self.state = 2251
                self.infixexp()
                self.state = 2252
                self.match(HaskellParser.TcloseQoute)
                pass

            elif la_ == 25:
                self.enterOuterAlt(localctx, 25)
                self.state = 2254
                self.match(HaskellParser.TopenDecQoute)
                self.state = 2255
                self.cvtopbody()
                self.state = 2256
                self.match(HaskellParser.TcloseQoute)
                pass

            elif la_ == 26:
                self.enterOuterAlt(localctx, 26)
                self.state = 2258
                self.quasiquote()
                pass

            elif la_ == 27:
                self.enterOuterAlt(localctx, 27)
                self.state = 2259
                self.match(HaskellParser.AopenParen)
                self.state = 2260
                self.aexp()
                self.state = 2262
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,253,self._ctx)
                if la_ == 1:
                    self.state = 2261
                    self.cmdargs()


                self.state = 2264
                self.match(HaskellParser.AopenParen)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Splice_expContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def splice_typed(self):
            return self.getTypedRuleContext(HaskellParser.Splice_typedContext,0)


        def splice_untyped(self):
            return self.getTypedRuleContext(HaskellParser.Splice_untypedContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_splice_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSplice_exp" ):
                listener.enterSplice_exp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSplice_exp" ):
                listener.exitSplice_exp(self)




    def splice_exp(self):

        localctx = HaskellParser.Splice_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 308, self.RULE_splice_exp)
        try:
            self.state = 2270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.DDollar]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2268
                self.splice_typed()
                pass
            elif token in [HaskellParser.Dollar]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2269
                self.splice_untyped()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Splice_untypedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Dollar(self):
            return self.getToken(HaskellParser.Dollar, 0)

        def aexp(self):
            return self.getTypedRuleContext(HaskellParser.AexpContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_splice_untyped

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSplice_untyped" ):
                listener.enterSplice_untyped(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSplice_untyped" ):
                listener.exitSplice_untyped(self)




    def splice_untyped(self):

        localctx = HaskellParser.Splice_untypedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 310, self.RULE_splice_untyped)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2272
            self.match(HaskellParser.Dollar)
            self.state = 2273
            self.aexp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Splice_typedContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DDollar(self):
            return self.getToken(HaskellParser.DDollar, 0)

        def aexp(self):
            return self.getTypedRuleContext(HaskellParser.AexpContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_splice_typed

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSplice_typed" ):
                listener.enterSplice_typed(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSplice_typed" ):
                listener.exitSplice_typed(self)




    def splice_typed(self):

        localctx = HaskellParser.Splice_typedContext(self, self._ctx, self.state)
        self.enterRule(localctx, 312, self.RULE_splice_typed)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2275
            self.match(HaskellParser.DDollar)
            self.state = 2276
            self.aexp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdargsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def acmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.AcmdContext)
            else:
                return self.getTypedRuleContext(HaskellParser.AcmdContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_cmdargs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdargs" ):
                listener.enterCmdargs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdargs" ):
                listener.exitCmdargs(self)




    def cmdargs(self):

        localctx = HaskellParser.CmdargsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 314, self.RULE_cmdargs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2279 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 2278
                    self.acmd()

                else:
                    raise NoViableAltException(self)
                self.state = 2281 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,256,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AcmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aexp(self):
            return self.getTypedRuleContext(HaskellParser.AexpContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_acmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcmd" ):
                listener.enterAcmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcmd" ):
                listener.exitAcmd(self)




    def acmd(self):

        localctx = HaskellParser.AcmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 316, self.RULE_acmd)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2283
            self.aexp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CvtopbodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opn(self):
            return self.getTypedRuleContext(HaskellParser.OpnContext,0)


        def close(self):
            return self.getTypedRuleContext(HaskellParser.CloseContext,0)


        def cvtopdecls0(self):
            return self.getTypedRuleContext(HaskellParser.Cvtopdecls0Context,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_cvtopbody

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCvtopbody" ):
                listener.enterCvtopbody(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCvtopbody" ):
                listener.exitCvtopbody(self)




    def cvtopbody(self):

        localctx = HaskellParser.CvtopbodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 318, self.RULE_cvtopbody)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2285
            self.opn()
            self.state = 2287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.NEWLINE) | (1 << HaskellParser.AS) | (1 << HaskellParser.CASE) | (1 << HaskellParser.CLASS) | (1 << HaskellParser.DATA) | (1 << HaskellParser.DEFAULT) | (1 << HaskellParser.DERIVING) | (1 << HaskellParser.DO) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.IF) | (1 << HaskellParser.INFIX) | (1 << HaskellParser.INFIXL) | (1 << HaskellParser.INFIXR) | (1 << HaskellParser.INSTANCE) | (1 << HaskellParser.LET) | (1 << HaskellParser.NEWTYPE) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.TYPE) | (1 << HaskellParser.WILDCARD) | (1 << HaskellParser.FOREIGN) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.MDO) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.PATTERN) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & ((1 << (HaskellParser.LCASE - 73)) | (1 << (HaskellParser.Bang - 73)) | (1 << (HaskellParser.Minus - 73)) | (1 << (HaskellParser.Tilde - 73)) | (1 << (HaskellParser.DDollar - 73)) | (1 << (HaskellParser.Dollar - 73)) | (1 << (HaskellParser.Semi - 73)) | (1 << (HaskellParser.Quote - 73)) | (1 << (HaskellParser.DoubleQuote - 73)) | (1 << (HaskellParser.ReverseSlash - 73)) | (1 << (HaskellParser.AopenParen - 73)) | (1 << (HaskellParser.TopenTexpQuote - 73)) | (1 << (HaskellParser.TopenExpQuote - 73)) | (1 << (HaskellParser.TopenPatQuote - 73)) | (1 << (HaskellParser.TopenTypQoute - 73)) | (1 << (HaskellParser.TopenDecQoute - 73)) | (1 << (HaskellParser.OpenBoxParen - 73)) | (1 << (HaskellParser.OpenRoundBracket - 73)) | (1 << (HaskellParser.OpenSquareBracket - 73)) | (1 << (HaskellParser.CHAR - 73)) | (1 << (HaskellParser.STRING - 73)) | (1 << (HaskellParser.VARID - 73)) | (1 << (HaskellParser.CONID - 73)) | (1 << (HaskellParser.OpenPragmaBracket - 73)) | (1 << (HaskellParser.SEMI - 73)))) != 0) or ((((_la - 137)) & ~0x3f) == 0 and ((1 << (_la - 137)) & ((1 << (HaskellParser.DECIMAL - 137)) | (1 << (HaskellParser.OCTAL - 137)) | (1 << (HaskellParser.HEXADECIMAL - 137)) | (1 << (HaskellParser.FLOAT - 137)))) != 0):
                self.state = 2286
                self.cvtopdecls0()


            self.state = 2289
            self.close()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Cvtopdecls0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def topdecls(self):
            return self.getTypedRuleContext(HaskellParser.TopdeclsContext,0)


        def semi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.SemiContext)
            else:
                return self.getTypedRuleContext(HaskellParser.SemiContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_cvtopdecls0

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCvtopdecls0" ):
                listener.enterCvtopdecls0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCvtopdecls0" ):
                listener.exitCvtopdecls0(self)




    def cvtopdecls0(self):

        localctx = HaskellParser.Cvtopdecls0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 320, self.RULE_cvtopdecls0)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2291
            self.topdecls()
            self.state = 2295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Semi or _la==HaskellParser.SEMI:
                self.state = 2292
                self.semi()
                self.state = 2297
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TexpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(HaskellParser.ExpContext,0)


        def infixexp(self):
            return self.getTypedRuleContext(HaskellParser.InfixexpContext,0)


        def qop(self):
            return self.getTypedRuleContext(HaskellParser.QopContext,0)


        def qopm(self):
            return self.getTypedRuleContext(HaskellParser.QopmContext,0)


        def Arrow(self):
            return self.getToken(HaskellParser.Arrow, 0)

        def texp(self):
            return self.getTypedRuleContext(HaskellParser.TexpContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_texp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTexp" ):
                listener.enterTexp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTexp" ):
                listener.exitTexp(self)




    def texp(self):

        localctx = HaskellParser.TexpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 322, self.RULE_texp)
        try:
            self.state = 2309
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,259,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2298
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2299
                self.infixexp()
                self.state = 2300
                self.qop()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2302
                self.qopm()
                self.state = 2303
                self.infixexp()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2305
                self.exp()
                self.state = 2306
                self.match(HaskellParser.Arrow)
                self.state = 2307
                self.texp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tup_exprsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def texp(self):
            return self.getTypedRuleContext(HaskellParser.TexpContext,0)


        def commas_tup_tail(self):
            return self.getTypedRuleContext(HaskellParser.Commas_tup_tailContext,0)


        def bars(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.BarsContext)
            else:
                return self.getTypedRuleContext(HaskellParser.BarsContext,i)


        def commas(self):
            return self.getTypedRuleContext(HaskellParser.CommasContext,0)


        def tup_tail(self):
            return self.getTypedRuleContext(HaskellParser.Tup_tailContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_tup_exprs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTup_exprs" ):
                listener.enterTup_exprs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTup_exprs" ):
                listener.exitTup_exprs(self)




    def tup_exprs(self):

        localctx = HaskellParser.Tup_exprsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 324, self.RULE_tup_exprs)
        self._la = 0 # Token type
        try:
            self.state = 2326
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,262,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2311
                self.texp()
                self.state = 2312
                self.commas_tup_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2314
                self.texp()
                self.state = 2315
                self.bars()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2317
                self.commas()
                self.state = 2319
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.CASE) | (1 << HaskellParser.DO) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.IF) | (1 << HaskellParser.LET) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.WILDCARD) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.MDO) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & ((1 << (HaskellParser.LCASE - 73)) | (1 << (HaskellParser.Hash - 73)) | (1 << (HaskellParser.Less - 73)) | (1 << (HaskellParser.Greater - 73)) | (1 << (HaskellParser.Ampersand - 73)) | (1 << (HaskellParser.Pipe - 73)) | (1 << (HaskellParser.Bang - 73)) | (1 << (HaskellParser.Caret - 73)) | (1 << (HaskellParser.Plus - 73)) | (1 << (HaskellParser.Minus - 73)) | (1 << (HaskellParser.Asterisk - 73)) | (1 << (HaskellParser.Percent - 73)) | (1 << (HaskellParser.Divide - 73)) | (1 << (HaskellParser.Tilde - 73)) | (1 << (HaskellParser.Atsign - 73)) | (1 << (HaskellParser.DDollar - 73)) | (1 << (HaskellParser.Dollar - 73)) | (1 << (HaskellParser.Dot - 73)) | (1 << (HaskellParser.QuestionMark - 73)) | (1 << (HaskellParser.Colon - 73)) | (1 << (HaskellParser.Eq - 73)) | (1 << (HaskellParser.Quote - 73)) | (1 << (HaskellParser.DoubleQuote - 73)) | (1 << (HaskellParser.ReverseSlash - 73)) | (1 << (HaskellParser.BackQuote - 73)) | (1 << (HaskellParser.AopenParen - 73)) | (1 << (HaskellParser.TopenTexpQuote - 73)) | (1 << (HaskellParser.TopenExpQuote - 73)) | (1 << (HaskellParser.TopenPatQuote - 73)) | (1 << (HaskellParser.TopenTypQoute - 73)) | (1 << (HaskellParser.TopenDecQoute - 73)) | (1 << (HaskellParser.OpenBoxParen - 73)) | (1 << (HaskellParser.OpenRoundBracket - 73)) | (1 << (HaskellParser.OpenSquareBracket - 73)) | (1 << (HaskellParser.CHAR - 73)) | (1 << (HaskellParser.STRING - 73)) | (1 << (HaskellParser.VARID - 73)) | (1 << (HaskellParser.CONID - 73)))) != 0) or ((((_la - 137)) & ~0x3f) == 0 and ((1 << (_la - 137)) & ((1 << (HaskellParser.DECIMAL - 137)) | (1 << (HaskellParser.OCTAL - 137)) | (1 << (HaskellParser.HEXADECIMAL - 137)) | (1 << (HaskellParser.FLOAT - 137)))) != 0):
                    self.state = 2318
                    self.tup_tail()


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2321
                self.bars()
                self.state = 2322
                self.texp()
                self.state = 2324
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HaskellParser.Pipe:
                    self.state = 2323
                    self.bars()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Commas_tup_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def commas(self):
            return self.getTypedRuleContext(HaskellParser.CommasContext,0)


        def tup_tail(self):
            return self.getTypedRuleContext(HaskellParser.Tup_tailContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_commas_tup_tail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommas_tup_tail" ):
                listener.enterCommas_tup_tail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommas_tup_tail" ):
                listener.exitCommas_tup_tail(self)




    def commas_tup_tail(self):

        localctx = HaskellParser.Commas_tup_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 326, self.RULE_commas_tup_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2328
            self.commas()
            self.state = 2330
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.CASE) | (1 << HaskellParser.DO) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.IF) | (1 << HaskellParser.LET) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.WILDCARD) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.MDO) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & ((1 << (HaskellParser.LCASE - 73)) | (1 << (HaskellParser.Hash - 73)) | (1 << (HaskellParser.Less - 73)) | (1 << (HaskellParser.Greater - 73)) | (1 << (HaskellParser.Ampersand - 73)) | (1 << (HaskellParser.Pipe - 73)) | (1 << (HaskellParser.Bang - 73)) | (1 << (HaskellParser.Caret - 73)) | (1 << (HaskellParser.Plus - 73)) | (1 << (HaskellParser.Minus - 73)) | (1 << (HaskellParser.Asterisk - 73)) | (1 << (HaskellParser.Percent - 73)) | (1 << (HaskellParser.Divide - 73)) | (1 << (HaskellParser.Tilde - 73)) | (1 << (HaskellParser.Atsign - 73)) | (1 << (HaskellParser.DDollar - 73)) | (1 << (HaskellParser.Dollar - 73)) | (1 << (HaskellParser.Dot - 73)) | (1 << (HaskellParser.QuestionMark - 73)) | (1 << (HaskellParser.Colon - 73)) | (1 << (HaskellParser.Eq - 73)) | (1 << (HaskellParser.Quote - 73)) | (1 << (HaskellParser.DoubleQuote - 73)) | (1 << (HaskellParser.ReverseSlash - 73)) | (1 << (HaskellParser.BackQuote - 73)) | (1 << (HaskellParser.AopenParen - 73)) | (1 << (HaskellParser.TopenTexpQuote - 73)) | (1 << (HaskellParser.TopenExpQuote - 73)) | (1 << (HaskellParser.TopenPatQuote - 73)) | (1 << (HaskellParser.TopenTypQoute - 73)) | (1 << (HaskellParser.TopenDecQoute - 73)) | (1 << (HaskellParser.OpenBoxParen - 73)) | (1 << (HaskellParser.OpenRoundBracket - 73)) | (1 << (HaskellParser.OpenSquareBracket - 73)) | (1 << (HaskellParser.CHAR - 73)) | (1 << (HaskellParser.STRING - 73)) | (1 << (HaskellParser.VARID - 73)) | (1 << (HaskellParser.CONID - 73)))) != 0) or ((((_la - 137)) & ~0x3f) == 0 and ((1 << (_la - 137)) & ((1 << (HaskellParser.DECIMAL - 137)) | (1 << (HaskellParser.OCTAL - 137)) | (1 << (HaskellParser.HEXADECIMAL - 137)) | (1 << (HaskellParser.FLOAT - 137)))) != 0):
                self.state = 2329
                self.tup_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Tup_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def texp(self):
            return self.getTypedRuleContext(HaskellParser.TexpContext,0)


        def commas_tup_tail(self):
            return self.getTypedRuleContext(HaskellParser.Commas_tup_tailContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_tup_tail

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTup_tail" ):
                listener.enterTup_tail(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTup_tail" ):
                listener.exitTup_tail(self)




    def tup_tail(self):

        localctx = HaskellParser.Tup_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 328, self.RULE_tup_tail)
        try:
            self.state = 2336
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,264,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2332
                self.texp()
                self.state = 2333
                self.commas_tup_tail()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2335
                self.texp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def texp(self):
            return self.getTypedRuleContext(HaskellParser.TexpContext,0)


        def lexps(self):
            return self.getTypedRuleContext(HaskellParser.LexpsContext,0)


        def DoubleDot(self):
            return self.getToken(HaskellParser.DoubleDot, 0)

        def Comma(self):
            return self.getToken(HaskellParser.Comma, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.ExpContext)
            else:
                return self.getTypedRuleContext(HaskellParser.ExpContext,i)


        def Pipe(self):
            return self.getToken(HaskellParser.Pipe, 0)

        def flattenedpquals(self):
            return self.getTypedRuleContext(HaskellParser.FlattenedpqualsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_lst

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLst" ):
                listener.enterLst(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLst" ):
                listener.exitLst(self)




    def lst(self):

        localctx = HaskellParser.LstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 330, self.RULE_lst)
        try:
            self.state = 2362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,265,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2338
                self.texp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2339
                self.lexps()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2340
                self.texp()
                self.state = 2341
                self.match(HaskellParser.DoubleDot)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2343
                self.texp()
                self.state = 2344
                self.match(HaskellParser.Comma)
                self.state = 2345
                self.exp()
                self.state = 2346
                self.match(HaskellParser.DoubleDot)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2348
                self.texp()
                self.state = 2349
                self.match(HaskellParser.DoubleDot)
                self.state = 2350
                self.exp()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 2352
                self.texp()
                self.state = 2353
                self.match(HaskellParser.Comma)
                self.state = 2354
                self.exp()
                self.state = 2355
                self.match(HaskellParser.DoubleDot)
                self.state = 2356
                self.exp()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 2358
                self.texp()
                self.state = 2359
                self.match(HaskellParser.Pipe)
                self.state = 2360
                self.flattenedpquals()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LexpsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def texp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.TexpContext)
            else:
                return self.getTypedRuleContext(HaskellParser.TexpContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Comma)
            else:
                return self.getToken(HaskellParser.Comma, i)

        def getRuleIndex(self):
            return HaskellParser.RULE_lexps

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLexps" ):
                listener.enterLexps(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLexps" ):
                listener.exitLexps(self)




    def lexps(self):

        localctx = HaskellParser.LexpsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 332, self.RULE_lexps)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2364
            self.texp()
            self.state = 2365
            self.match(HaskellParser.Comma)
            self.state = 2366
            self.texp()
            self.state = 2371
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Comma:
                self.state = 2367
                self.match(HaskellParser.Comma)
                self.state = 2368
                self.texp()
                self.state = 2373
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FlattenedpqualsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pquals(self):
            return self.getTypedRuleContext(HaskellParser.PqualsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_flattenedpquals

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFlattenedpquals" ):
                listener.enterFlattenedpquals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFlattenedpquals" ):
                listener.exitFlattenedpquals(self)




    def flattenedpquals(self):

        localctx = HaskellParser.FlattenedpqualsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 334, self.RULE_flattenedpquals)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2374
            self.pquals()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PqualsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def squals(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.SqualsContext)
            else:
                return self.getTypedRuleContext(HaskellParser.SqualsContext,i)


        def Pipe(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Pipe)
            else:
                return self.getToken(HaskellParser.Pipe, i)

        def getRuleIndex(self):
            return HaskellParser.RULE_pquals

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPquals" ):
                listener.enterPquals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPquals" ):
                listener.exitPquals(self)




    def pquals(self):

        localctx = HaskellParser.PqualsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 336, self.RULE_pquals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2376
            self.squals()
            self.state = 2381
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Pipe:
                self.state = 2377
                self.match(HaskellParser.Pipe)
                self.state = 2378
                self.squals()
                self.state = 2383
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SqualsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def transformqual(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.TransformqualContext)
            else:
                return self.getTypedRuleContext(HaskellParser.TransformqualContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Comma)
            else:
                return self.getToken(HaskellParser.Comma, i)

        def qual(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.QualContext)
            else:
                return self.getTypedRuleContext(HaskellParser.QualContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_squals

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSquals" ):
                listener.enterSquals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSquals" ):
                listener.exitSquals(self)




    def squals(self):

        localctx = HaskellParser.SqualsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 338, self.RULE_squals)
        self._la = 0 # Token type
        try:
            self.state = 2416
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,272,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2384
                self.transformqual()
                self.state = 2389
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==HaskellParser.Comma:
                    self.state = 2385
                    self.match(HaskellParser.Comma)
                    self.state = 2386
                    self.transformqual()
                    self.state = 2391
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2392
                self.transformqual()
                self.state = 2397
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==HaskellParser.Comma:
                    self.state = 2393
                    self.match(HaskellParser.Comma)
                    self.state = 2394
                    self.qual()
                    self.state = 2399
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2400
                self.qual()
                self.state = 2405
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==HaskellParser.Comma:
                    self.state = 2401
                    self.match(HaskellParser.Comma)
                    self.state = 2402
                    self.transformqual()
                    self.state = 2407
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2408
                self.qual()
                self.state = 2413
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==HaskellParser.Comma:
                    self.state = 2409
                    self.match(HaskellParser.Comma)
                    self.state = 2410
                    self.qual()
                    self.state = 2415
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TransformqualContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THEN(self):
            return self.getToken(HaskellParser.THEN, 0)

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.ExpContext)
            else:
                return self.getTypedRuleContext(HaskellParser.ExpContext,i)


        def BY(self):
            return self.getToken(HaskellParser.BY, 0)

        def GROUP(self):
            return self.getToken(HaskellParser.GROUP, 0)

        def USING(self):
            return self.getToken(HaskellParser.USING, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_transformqual

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTransformqual" ):
                listener.enterTransformqual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTransformqual" ):
                listener.exitTransformqual(self)




    def transformqual(self):

        localctx = HaskellParser.TransformqualContext(self, self._ctx, self.state)
        self.enterRule(localctx, 340, self.RULE_transformqual)
        try:
            self.state = 2436
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,273,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2418
                self.match(HaskellParser.THEN)
                self.state = 2419
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2420
                self.match(HaskellParser.THEN)
                self.state = 2421
                self.exp()
                self.state = 2422
                self.match(HaskellParser.BY)
                self.state = 2423
                self.exp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2425
                self.match(HaskellParser.THEN)
                self.state = 2426
                self.match(HaskellParser.GROUP)
                self.state = 2427
                self.match(HaskellParser.USING)
                self.state = 2428
                self.exp()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2429
                self.match(HaskellParser.THEN)
                self.state = 2430
                self.match(HaskellParser.GROUP)
                self.state = 2431
                self.match(HaskellParser.BY)
                self.state = 2432
                self.exp()
                self.state = 2433
                self.match(HaskellParser.USING)
                self.state = 2434
                self.exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GuardsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def guard(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.GuardContext)
            else:
                return self.getTypedRuleContext(HaskellParser.GuardContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Comma)
            else:
                return self.getToken(HaskellParser.Comma, i)

        def getRuleIndex(self):
            return HaskellParser.RULE_guards

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGuards" ):
                listener.enterGuards(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGuards" ):
                listener.exitGuards(self)




    def guards(self):

        localctx = HaskellParser.GuardsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 342, self.RULE_guards)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2438
            self.guard()
            self.state = 2443
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Comma:
                self.state = 2439
                self.match(HaskellParser.Comma)
                self.state = 2440
                self.guard()
                self.state = 2445
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GuardContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pat(self):
            return self.getTypedRuleContext(HaskellParser.PatContext,0)


        def Revarrow(self):
            return self.getToken(HaskellParser.Revarrow, 0)

        def infixexp(self):
            return self.getTypedRuleContext(HaskellParser.InfixexpContext,0)


        def LET(self):
            return self.getToken(HaskellParser.LET, 0)

        def decllist(self):
            return self.getTypedRuleContext(HaskellParser.DecllistContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_guard

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGuard" ):
                listener.enterGuard(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGuard" ):
                listener.exitGuard(self)




    def guard(self):

        localctx = HaskellParser.GuardContext(self, self._ctx, self.state)
        self.enterRule(localctx, 344, self.RULE_guard)
        try:
            self.state = 2453
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,275,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2446
                self.pat()
                self.state = 2447
                self.match(HaskellParser.Revarrow)
                self.state = 2448
                self.infixexp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2450
                self.match(HaskellParser.LET)
                self.state = 2451
                self.decllist()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2452
                self.infixexp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AltsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opn(self):
            return self.getTypedRuleContext(HaskellParser.OpnContext,0)


        def close(self):
            return self.getTypedRuleContext(HaskellParser.CloseContext,0)


        def alt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.AltContext)
            else:
                return self.getTypedRuleContext(HaskellParser.AltContext,i)


        def semi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.SemiContext)
            else:
                return self.getTypedRuleContext(HaskellParser.SemiContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_alts

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlts" ):
                listener.enterAlts(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlts" ):
                listener.exitAlts(self)




    def alts(self):

        localctx = HaskellParser.AltsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 346, self.RULE_alts)
        self._la = 0 # Token type
        try:
            self.state = 2472
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,278,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2455
                self.opn()
                self.state = 2463 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 2456
                    self.alt()
                    self.state = 2460
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==HaskellParser.Semi or _la==HaskellParser.SEMI:
                        self.state = 2457
                        self.semi()
                        self.state = 2462
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 2465 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.CASE) | (1 << HaskellParser.DO) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.IF) | (1 << HaskellParser.LET) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.WILDCARD) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.MDO) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & ((1 << (HaskellParser.LCASE - 73)) | (1 << (HaskellParser.Bang - 73)) | (1 << (HaskellParser.Minus - 73)) | (1 << (HaskellParser.Tilde - 73)) | (1 << (HaskellParser.DDollar - 73)) | (1 << (HaskellParser.Dollar - 73)) | (1 << (HaskellParser.Quote - 73)) | (1 << (HaskellParser.DoubleQuote - 73)) | (1 << (HaskellParser.ReverseSlash - 73)) | (1 << (HaskellParser.AopenParen - 73)) | (1 << (HaskellParser.TopenTexpQuote - 73)) | (1 << (HaskellParser.TopenExpQuote - 73)) | (1 << (HaskellParser.TopenPatQuote - 73)) | (1 << (HaskellParser.TopenTypQoute - 73)) | (1 << (HaskellParser.TopenDecQoute - 73)) | (1 << (HaskellParser.OpenBoxParen - 73)) | (1 << (HaskellParser.OpenRoundBracket - 73)) | (1 << (HaskellParser.OpenSquareBracket - 73)) | (1 << (HaskellParser.CHAR - 73)) | (1 << (HaskellParser.STRING - 73)) | (1 << (HaskellParser.VARID - 73)) | (1 << (HaskellParser.CONID - 73)))) != 0) or ((((_la - 137)) & ~0x3f) == 0 and ((1 << (_la - 137)) & ((1 << (HaskellParser.DECIMAL - 137)) | (1 << (HaskellParser.OCTAL - 137)) | (1 << (HaskellParser.HEXADECIMAL - 137)) | (1 << (HaskellParser.FLOAT - 137)))) != 0)):
                        break

                self.state = 2467
                self.close()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2469
                self.opn()
                self.state = 2470
                self.close()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AltContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def pat(self):
            return self.getTypedRuleContext(HaskellParser.PatContext,0)


        def alt_rhs(self):
            return self.getTypedRuleContext(HaskellParser.Alt_rhsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_alt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlt" ):
                listener.enterAlt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlt" ):
                listener.exitAlt(self)




    def alt(self):

        localctx = HaskellParser.AltContext(self, self._ctx, self.state)
        self.enterRule(localctx, 348, self.RULE_alt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2474
            self.pat()
            self.state = 2475
            self.alt_rhs()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Alt_rhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ralt(self):
            return self.getTypedRuleContext(HaskellParser.RaltContext,0)


        def wherebinds(self):
            return self.getTypedRuleContext(HaskellParser.WherebindsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_alt_rhs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlt_rhs" ):
                listener.enterAlt_rhs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlt_rhs" ):
                listener.exitAlt_rhs(self)




    def alt_rhs(self):

        localctx = HaskellParser.Alt_rhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 350, self.RULE_alt_rhs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2477
            self.ralt()
            self.state = 2479
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HaskellParser.WHERE:
                self.state = 2478
                self.wherebinds()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RaltContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Arrow(self):
            return self.getToken(HaskellParser.Arrow, 0)

        def exp(self):
            return self.getTypedRuleContext(HaskellParser.ExpContext,0)


        def gdpats(self):
            return self.getTypedRuleContext(HaskellParser.GdpatsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_ralt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRalt" ):
                listener.enterRalt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRalt" ):
                listener.exitRalt(self)




    def ralt(self):

        localctx = HaskellParser.RaltContext(self, self._ctx, self.state)
        self.enterRule(localctx, 352, self.RULE_ralt)
        try:
            self.state = 2484
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.Arrow]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2481
                self.match(HaskellParser.Arrow)
                self.state = 2482
                self.exp()
                pass
            elif token in [HaskellParser.Pipe]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2483
                self.gdpats()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GdpatsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def gdpat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.GdpatContext)
            else:
                return self.getTypedRuleContext(HaskellParser.GdpatContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_gdpats

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGdpats" ):
                listener.enterGdpats(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGdpats" ):
                listener.exitGdpats(self)




    def gdpats(self):

        localctx = HaskellParser.GdpatsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 354, self.RULE_gdpats)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2487 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 2486
                    self.gdpat()

                else:
                    raise NoViableAltException(self)
                self.state = 2489 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,281,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfgdpatsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OCURLY(self):
            return self.getToken(HaskellParser.OCURLY, 0)

        def gdpats(self):
            return self.getTypedRuleContext(HaskellParser.GdpatsContext,0)


        def CCURLY(self):
            return self.getToken(HaskellParser.CCURLY, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_ifgdpats

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfgdpats" ):
                listener.enterIfgdpats(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfgdpats" ):
                listener.exitIfgdpats(self)




    def ifgdpats(self):

        localctx = HaskellParser.IfgdpatsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 356, self.RULE_ifgdpats)
        try:
            self.state = 2496
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.OCURLY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2491
                self.match(HaskellParser.OCURLY)
                self.state = 2492
                self.gdpats()
                self.state = 2493
                self.match(HaskellParser.CCURLY)
                pass
            elif token in [HaskellParser.Pipe]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2495
                self.gdpats()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GdpatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Pipe(self):
            return self.getToken(HaskellParser.Pipe, 0)

        def guards(self):
            return self.getTypedRuleContext(HaskellParser.GuardsContext,0)


        def Arrow(self):
            return self.getToken(HaskellParser.Arrow, 0)

        def exp(self):
            return self.getTypedRuleContext(HaskellParser.ExpContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_gdpat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGdpat" ):
                listener.enterGdpat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGdpat" ):
                listener.exitGdpat(self)




    def gdpat(self):

        localctx = HaskellParser.GdpatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 358, self.RULE_gdpat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2498
            self.match(HaskellParser.Pipe)
            self.state = 2499
            self.guards()
            self.state = 2500
            self.match(HaskellParser.Arrow)
            self.state = 2501
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(HaskellParser.ExpContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_pat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPat" ):
                listener.enterPat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPat" ):
                listener.exitPat(self)




    def pat(self):

        localctx = HaskellParser.PatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 360, self.RULE_pat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2503
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BindpatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(HaskellParser.ExpContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_bindpat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBindpat" ):
                listener.enterBindpat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBindpat" ):
                listener.exitBindpat(self)




    def bindpat(self):

        localctx = HaskellParser.BindpatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 362, self.RULE_bindpat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2505
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ApatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aexp(self):
            return self.getTypedRuleContext(HaskellParser.AexpContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_apat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterApat" ):
                listener.enterApat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitApat" ):
                listener.exitApat(self)




    def apat(self):

        localctx = HaskellParser.ApatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 364, self.RULE_apat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2507
            self.aexp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ApatsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def apat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.ApatContext)
            else:
                return self.getTypedRuleContext(HaskellParser.ApatContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_apats

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterApats" ):
                listener.enterApats(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitApats" ):
                listener.exitApats(self)




    def apats(self):

        localctx = HaskellParser.ApatsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 366, self.RULE_apats)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2510 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 2509
                self.apat()
                self.state = 2512 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.CASE) | (1 << HaskellParser.DO) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.IF) | (1 << HaskellParser.LET) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.WILDCARD) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.MDO) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & ((1 << (HaskellParser.LCASE - 73)) | (1 << (HaskellParser.Bang - 73)) | (1 << (HaskellParser.Tilde - 73)) | (1 << (HaskellParser.DDollar - 73)) | (1 << (HaskellParser.Dollar - 73)) | (1 << (HaskellParser.Quote - 73)) | (1 << (HaskellParser.DoubleQuote - 73)) | (1 << (HaskellParser.ReverseSlash - 73)) | (1 << (HaskellParser.AopenParen - 73)) | (1 << (HaskellParser.TopenTexpQuote - 73)) | (1 << (HaskellParser.TopenExpQuote - 73)) | (1 << (HaskellParser.TopenPatQuote - 73)) | (1 << (HaskellParser.TopenTypQoute - 73)) | (1 << (HaskellParser.TopenDecQoute - 73)) | (1 << (HaskellParser.OpenBoxParen - 73)) | (1 << (HaskellParser.OpenRoundBracket - 73)) | (1 << (HaskellParser.OpenSquareBracket - 73)) | (1 << (HaskellParser.CHAR - 73)) | (1 << (HaskellParser.STRING - 73)) | (1 << (HaskellParser.VARID - 73)) | (1 << (HaskellParser.CONID - 73)))) != 0) or ((((_la - 137)) & ~0x3f) == 0 and ((1 << (_la - 137)) & ((1 << (HaskellParser.DECIMAL - 137)) | (1 << (HaskellParser.OCTAL - 137)) | (1 << (HaskellParser.HEXADECIMAL - 137)) | (1 << (HaskellParser.FLOAT - 137)))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FpatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qvar(self):
            return self.getTypedRuleContext(HaskellParser.QvarContext,0)


        def Eq(self):
            return self.getToken(HaskellParser.Eq, 0)

        def pat(self):
            return self.getTypedRuleContext(HaskellParser.PatContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_fpat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFpat" ):
                listener.enterFpat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFpat" ):
                listener.exitFpat(self)




    def fpat(self):

        localctx = HaskellParser.FpatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 368, self.RULE_fpat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2514
            self.qvar()
            self.state = 2515
            self.match(HaskellParser.Eq)
            self.state = 2516
            self.pat()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opn(self):
            return self.getTypedRuleContext(HaskellParser.OpnContext,0)


        def close(self):
            return self.getTypedRuleContext(HaskellParser.CloseContext,0)


        def stmts(self):
            return self.getTypedRuleContext(HaskellParser.StmtsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_stmtlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmtlist" ):
                listener.enterStmtlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmtlist" ):
                listener.exitStmtlist(self)




    def stmtlist(self):

        localctx = HaskellParser.StmtlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 370, self.RULE_stmtlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2518
            self.opn()
            self.state = 2520
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.CASE) | (1 << HaskellParser.DO) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.IF) | (1 << HaskellParser.LET) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.WILDCARD) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.MDO) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.REC) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0) or ((((_la - 73)) & ~0x3f) == 0 and ((1 << (_la - 73)) & ((1 << (HaskellParser.LCASE - 73)) | (1 << (HaskellParser.Bang - 73)) | (1 << (HaskellParser.Minus - 73)) | (1 << (HaskellParser.Tilde - 73)) | (1 << (HaskellParser.DDollar - 73)) | (1 << (HaskellParser.Dollar - 73)) | (1 << (HaskellParser.Semi - 73)) | (1 << (HaskellParser.Quote - 73)) | (1 << (HaskellParser.DoubleQuote - 73)) | (1 << (HaskellParser.ReverseSlash - 73)) | (1 << (HaskellParser.AopenParen - 73)) | (1 << (HaskellParser.TopenTexpQuote - 73)) | (1 << (HaskellParser.TopenExpQuote - 73)) | (1 << (HaskellParser.TopenPatQuote - 73)) | (1 << (HaskellParser.TopenTypQoute - 73)) | (1 << (HaskellParser.TopenDecQoute - 73)) | (1 << (HaskellParser.OpenBoxParen - 73)) | (1 << (HaskellParser.OpenRoundBracket - 73)) | (1 << (HaskellParser.OpenSquareBracket - 73)) | (1 << (HaskellParser.CHAR - 73)) | (1 << (HaskellParser.STRING - 73)) | (1 << (HaskellParser.VARID - 73)) | (1 << (HaskellParser.CONID - 73)) | (1 << (HaskellParser.SEMI - 73)))) != 0) or ((((_la - 137)) & ~0x3f) == 0 and ((1 << (_la - 137)) & ((1 << (HaskellParser.DECIMAL - 137)) | (1 << (HaskellParser.OCTAL - 137)) | (1 << (HaskellParser.HEXADECIMAL - 137)) | (1 << (HaskellParser.FLOAT - 137)))) != 0):
                self.state = 2519
                self.stmts()


            self.state = 2522
            self.close()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.StmtContext)
            else:
                return self.getTypedRuleContext(HaskellParser.StmtContext,i)


        def semi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.SemiContext)
            else:
                return self.getTypedRuleContext(HaskellParser.SemiContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_stmts

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmts" ):
                listener.enterStmts(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmts" ):
                listener.exitStmts(self)




    def stmts(self):

        localctx = HaskellParser.StmtsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 372, self.RULE_stmts)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2524
            self.stmt()
            self.state = 2534
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,286,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2526 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 2525
                            self.semi()

                        else:
                            raise NoViableAltException(self)
                        self.state = 2528 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,285,self._ctx)

                    self.state = 2530
                    self.stmt() 
                self.state = 2536
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,286,self._ctx)

            self.state = 2540
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Semi or _la==HaskellParser.SEMI:
                self.state = 2537
                self.semi()
                self.state = 2542
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qual(self):
            return self.getTypedRuleContext(HaskellParser.QualContext,0)


        def REC(self):
            return self.getToken(HaskellParser.REC, 0)

        def stmtlist(self):
            return self.getTypedRuleContext(HaskellParser.StmtlistContext,0)


        def semi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.SemiContext)
            else:
                return self.getTypedRuleContext(HaskellParser.SemiContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_stmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStmt" ):
                listener.enterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStmt" ):
                listener.exitStmt(self)




    def stmt(self):

        localctx = HaskellParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 374, self.RULE_stmt)
        try:
            self.state = 2551
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.AS, HaskellParser.CASE, HaskellParser.DO, HaskellParser.HIDING, HaskellParser.IF, HaskellParser.LET, HaskellParser.QUALIFIED, HaskellParser.WILDCARD, HaskellParser.EXPORT, HaskellParser.MDO, HaskellParser.STDCALL, HaskellParser.CCALL, HaskellParser.CAPI, HaskellParser.JSCALL, HaskellParser.STOCK, HaskellParser.ANYCLASS, HaskellParser.VIA, HaskellParser.LCASE, HaskellParser.Bang, HaskellParser.Minus, HaskellParser.Tilde, HaskellParser.DDollar, HaskellParser.Dollar, HaskellParser.Quote, HaskellParser.DoubleQuote, HaskellParser.ReverseSlash, HaskellParser.AopenParen, HaskellParser.TopenTexpQuote, HaskellParser.TopenExpQuote, HaskellParser.TopenPatQuote, HaskellParser.TopenTypQoute, HaskellParser.TopenDecQoute, HaskellParser.OpenBoxParen, HaskellParser.OpenRoundBracket, HaskellParser.OpenSquareBracket, HaskellParser.CHAR, HaskellParser.STRING, HaskellParser.VARID, HaskellParser.CONID, HaskellParser.DECIMAL, HaskellParser.OCTAL, HaskellParser.HEXADECIMAL, HaskellParser.FLOAT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2543
                self.qual()
                pass
            elif token in [HaskellParser.REC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2544
                self.match(HaskellParser.REC)
                self.state = 2545
                self.stmtlist()
                pass
            elif token in [HaskellParser.Semi, HaskellParser.SEMI]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2547 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 2546
                        self.semi()

                    else:
                        raise NoViableAltException(self)
                    self.state = 2549 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,288,self._ctx)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QualContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def bindpat(self):
            return self.getTypedRuleContext(HaskellParser.BindpatContext,0)


        def Revarrow(self):
            return self.getToken(HaskellParser.Revarrow, 0)

        def exp(self):
            return self.getTypedRuleContext(HaskellParser.ExpContext,0)


        def LET(self):
            return self.getToken(HaskellParser.LET, 0)

        def binds(self):
            return self.getTypedRuleContext(HaskellParser.BindsContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_qual

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQual" ):
                listener.enterQual(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQual" ):
                listener.exitQual(self)




    def qual(self):

        localctx = HaskellParser.QualContext(self, self._ctx, self.state)
        self.enterRule(localctx, 376, self.RULE_qual)
        try:
            self.state = 2560
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,290,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2553
                self.bindpat()
                self.state = 2554
                self.match(HaskellParser.Revarrow)
                self.state = 2555
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2557
                self.exp()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2558
                self.match(HaskellParser.LET)
                self.state = 2559
                self.binds()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FbindsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fbind(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.FbindContext)
            else:
                return self.getTypedRuleContext(HaskellParser.FbindContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Comma)
            else:
                return self.getToken(HaskellParser.Comma, i)

        def DoubleDot(self):
            return self.getToken(HaskellParser.DoubleDot, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_fbinds

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFbinds" ):
                listener.enterFbinds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFbinds" ):
                listener.exitFbinds(self)




    def fbinds(self):

        localctx = HaskellParser.FbindsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 378, self.RULE_fbinds)
        self._la = 0 # Token type
        try:
            self.state = 2571
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.AS, HaskellParser.HIDING, HaskellParser.QUALIFIED, HaskellParser.EXPORT, HaskellParser.STDCALL, HaskellParser.CCALL, HaskellParser.CAPI, HaskellParser.JSCALL, HaskellParser.STOCK, HaskellParser.ANYCLASS, HaskellParser.VIA, HaskellParser.OpenRoundBracket, HaskellParser.VARID, HaskellParser.CONID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2562
                self.fbind()
                self.state = 2567
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==HaskellParser.Comma:
                    self.state = 2563
                    self.match(HaskellParser.Comma)
                    self.state = 2564
                    self.fbind()
                    self.state = 2569
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [HaskellParser.DoubleDot]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2570
                self.match(HaskellParser.DoubleDot)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FbindContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qvar(self):
            return self.getTypedRuleContext(HaskellParser.QvarContext,0)


        def Eq(self):
            return self.getToken(HaskellParser.Eq, 0)

        def exp(self):
            return self.getTypedRuleContext(HaskellParser.ExpContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_fbind

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFbind" ):
                listener.enterFbind(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFbind" ):
                listener.exitFbind(self)




    def fbind(self):

        localctx = HaskellParser.FbindContext(self, self._ctx, self.state)
        self.enterRule(localctx, 380, self.RULE_fbind)
        try:
            self.state = 2578
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,293,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2573
                self.qvar()
                self.state = 2574
                self.match(HaskellParser.Eq)
                self.state = 2575
                self.exp()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2577
                self.qvar()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DbindsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dbind(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.DbindContext)
            else:
                return self.getTypedRuleContext(HaskellParser.DbindContext,i)


        def semi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.SemiContext)
            else:
                return self.getTypedRuleContext(HaskellParser.SemiContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_dbinds

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDbinds" ):
                listener.enterDbinds(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDbinds" ):
                listener.exitDbinds(self)




    def dbinds(self):

        localctx = HaskellParser.DbindsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 382, self.RULE_dbinds)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2580
            self.dbind()

            self.state = 2582 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 2581
                self.semi()
                self.state = 2584 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==HaskellParser.Semi or _la==HaskellParser.SEMI):
                    break

            self.state = 2586
            self.dbind()
            self.state = 2591
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Semi or _la==HaskellParser.SEMI:
                self.state = 2588
                self.semi()
                self.state = 2593
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DbindContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varid(self):
            return self.getTypedRuleContext(HaskellParser.VaridContext,0)


        def Eq(self):
            return self.getToken(HaskellParser.Eq, 0)

        def exp(self):
            return self.getTypedRuleContext(HaskellParser.ExpContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_dbind

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDbind" ):
                listener.enterDbind(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDbind" ):
                listener.exitDbind(self)




    def dbind(self):

        localctx = HaskellParser.DbindContext(self, self._ctx, self.state)
        self.enterRule(localctx, 384, self.RULE_dbind)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2594
            self.varid()
            self.state = 2595
            self.match(HaskellParser.Eq)
            self.state = 2596
            self.exp()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_boolformula_optContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_boolformula_and(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.Name_boolformula_andContext)
            else:
                return self.getTypedRuleContext(HaskellParser.Name_boolformula_andContext,i)


        def Pipe(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Pipe)
            else:
                return self.getToken(HaskellParser.Pipe, i)

        def getRuleIndex(self):
            return HaskellParser.RULE_name_boolformula_opt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName_boolformula_opt" ):
                listener.enterName_boolformula_opt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName_boolformula_opt" ):
                listener.exitName_boolformula_opt(self)




    def name_boolformula_opt(self):

        localctx = HaskellParser.Name_boolformula_optContext(self, self._ctx, self.state)
        self.enterRule(localctx, 386, self.RULE_name_boolformula_opt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2598
            self.name_boolformula_and()
            self.state = 2603
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Pipe:
                self.state = 2599
                self.match(HaskellParser.Pipe)
                self.state = 2600
                self.name_boolformula_and()
                self.state = 2605
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_boolformula_andContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_boolformula_and_list(self):
            return self.getTypedRuleContext(HaskellParser.Name_boolformula_and_listContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_name_boolformula_and

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName_boolformula_and" ):
                listener.enterName_boolformula_and(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName_boolformula_and" ):
                listener.exitName_boolformula_and(self)




    def name_boolformula_and(self):

        localctx = HaskellParser.Name_boolformula_andContext(self, self._ctx, self.state)
        self.enterRule(localctx, 388, self.RULE_name_boolformula_and)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2606
            self.name_boolformula_and_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_boolformula_and_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_boolformula_atom(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.Name_boolformula_atomContext)
            else:
                return self.getTypedRuleContext(HaskellParser.Name_boolformula_atomContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Comma)
            else:
                return self.getToken(HaskellParser.Comma, i)

        def getRuleIndex(self):
            return HaskellParser.RULE_name_boolformula_and_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName_boolformula_and_list" ):
                listener.enterName_boolformula_and_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName_boolformula_and_list" ):
                listener.exitName_boolformula_and_list(self)




    def name_boolformula_and_list(self):

        localctx = HaskellParser.Name_boolformula_and_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 390, self.RULE_name_boolformula_and_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2608
            self.name_boolformula_atom()
            self.state = 2613
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Comma:
                self.state = 2609
                self.match(HaskellParser.Comma)
                self.state = 2610
                self.name_boolformula_atom()
                self.state = 2615
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_boolformula_atomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenRoundBracket(self):
            return self.getToken(HaskellParser.OpenRoundBracket, 0)

        def name_boolformula_opt(self):
            return self.getTypedRuleContext(HaskellParser.Name_boolformula_optContext,0)


        def CloseRoundBracket(self):
            return self.getToken(HaskellParser.CloseRoundBracket, 0)

        def name_var(self):
            return self.getTypedRuleContext(HaskellParser.Name_varContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_name_boolformula_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName_boolformula_atom" ):
                listener.enterName_boolformula_atom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName_boolformula_atom" ):
                listener.exitName_boolformula_atom(self)




    def name_boolformula_atom(self):

        localctx = HaskellParser.Name_boolformula_atomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 392, self.RULE_name_boolformula_atom)
        try:
            self.state = 2621
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,298,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2616
                self.match(HaskellParser.OpenRoundBracket)
                self.state = 2617
                self.name_boolformula_opt()
                self.state = 2618
                self.match(HaskellParser.CloseRoundBracket)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2620
                self.name_var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NamelistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.Name_varContext)
            else:
                return self.getTypedRuleContext(HaskellParser.Name_varContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Comma)
            else:
                return self.getToken(HaskellParser.Comma, i)

        def getRuleIndex(self):
            return HaskellParser.RULE_namelist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNamelist" ):
                listener.enterNamelist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNamelist" ):
                listener.exitNamelist(self)




    def namelist(self):

        localctx = HaskellParser.NamelistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 394, self.RULE_namelist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2623
            self.name_var()
            self.state = 2628
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Comma:
                self.state = 2624
                self.match(HaskellParser.Comma)
                self.state = 2625
                self.name_var()
                self.state = 2630
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_varContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(HaskellParser.VarContext,0)


        def con(self):
            return self.getTypedRuleContext(HaskellParser.ConContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_name_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName_var" ):
                listener.enterName_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName_var" ):
                listener.exitName_var(self)




    def name_var(self):

        localctx = HaskellParser.Name_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 396, self.RULE_name_var)
        try:
            self.state = 2633
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,300,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2631
                self.var()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2632
                self.con()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Qcon_nowiredlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def gen_qcon(self):
            return self.getTypedRuleContext(HaskellParser.Gen_qconContext,0)


        def sysdcon_nolist(self):
            return self.getTypedRuleContext(HaskellParser.Sysdcon_nolistContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_qcon_nowiredlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQcon_nowiredlist" ):
                listener.enterQcon_nowiredlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQcon_nowiredlist" ):
                listener.exitQcon_nowiredlist(self)




    def qcon_nowiredlist(self):

        localctx = HaskellParser.Qcon_nowiredlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 398, self.RULE_qcon_nowiredlist)
        try:
            self.state = 2637
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,301,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2635
                self.gen_qcon()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2636
                self.sysdcon_nolist()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QconContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def gen_qcon(self):
            return self.getTypedRuleContext(HaskellParser.Gen_qconContext,0)


        def sysdcon(self):
            return self.getTypedRuleContext(HaskellParser.SysdconContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_qcon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQcon" ):
                listener.enterQcon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQcon" ):
                listener.exitQcon(self)




    def qcon(self):

        localctx = HaskellParser.QconContext(self, self._ctx, self.state)
        self.enterRule(localctx, 400, self.RULE_qcon)
        try:
            self.state = 2641
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,302,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2639
                self.gen_qcon()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2640
                self.sysdcon()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Gen_qconContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qconid(self):
            return self.getTypedRuleContext(HaskellParser.QconidContext,0)


        def OpenRoundBracket(self):
            return self.getToken(HaskellParser.OpenRoundBracket, 0)

        def qconsym(self):
            return self.getTypedRuleContext(HaskellParser.QconsymContext,0)


        def CloseRoundBracket(self):
            return self.getToken(HaskellParser.CloseRoundBracket, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_gen_qcon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGen_qcon" ):
                listener.enterGen_qcon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGen_qcon" ):
                listener.exitGen_qcon(self)




    def gen_qcon(self):

        localctx = HaskellParser.Gen_qconContext(self, self._ctx, self.state)
        self.enterRule(localctx, 402, self.RULE_gen_qcon)
        try:
            self.state = 2648
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.CONID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2643
                self.qconid()
                pass
            elif token in [HaskellParser.OpenRoundBracket]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2644
                self.match(HaskellParser.OpenRoundBracket)
                self.state = 2645
                self.qconsym()
                self.state = 2646
                self.match(HaskellParser.CloseRoundBracket)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conid(self):
            return self.getTypedRuleContext(HaskellParser.ConidContext,0)


        def OpenRoundBracket(self):
            return self.getToken(HaskellParser.OpenRoundBracket, 0)

        def consym(self):
            return self.getTypedRuleContext(HaskellParser.ConsymContext,0)


        def CloseRoundBracket(self):
            return self.getToken(HaskellParser.CloseRoundBracket, 0)

        def sysdcon(self):
            return self.getTypedRuleContext(HaskellParser.SysdconContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_con

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCon" ):
                listener.enterCon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCon" ):
                listener.exitCon(self)




    def con(self):

        localctx = HaskellParser.ConContext(self, self._ctx, self.state)
        self.enterRule(localctx, 404, self.RULE_con)
        try:
            self.state = 2656
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,304,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2650
                self.conid()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2651
                self.match(HaskellParser.OpenRoundBracket)
                self.state = 2652
                self.consym()
                self.state = 2653
                self.match(HaskellParser.CloseRoundBracket)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2655
                self.sysdcon()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Con_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def con(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.ConContext)
            else:
                return self.getTypedRuleContext(HaskellParser.ConContext,i)


        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Comma)
            else:
                return self.getToken(HaskellParser.Comma, i)

        def getRuleIndex(self):
            return HaskellParser.RULE_con_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCon_list" ):
                listener.enterCon_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCon_list" ):
                listener.exitCon_list(self)




    def con_list(self):

        localctx = HaskellParser.Con_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 406, self.RULE_con_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2658
            self.con()
            self.state = 2663
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HaskellParser.Comma:
                self.state = 2659
                self.match(HaskellParser.Comma)
                self.state = 2660
                self.con()
                self.state = 2665
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sysdcon_nolistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenRoundBracket(self):
            return self.getToken(HaskellParser.OpenRoundBracket, 0)

        def CloseRoundBracket(self):
            return self.getToken(HaskellParser.CloseRoundBracket, 0)

        def commas(self):
            return self.getTypedRuleContext(HaskellParser.CommasContext,0)


        def OpenBoxParen(self):
            return self.getToken(HaskellParser.OpenBoxParen, 0)

        def CloseBoxParen(self):
            return self.getToken(HaskellParser.CloseBoxParen, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_sysdcon_nolist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSysdcon_nolist" ):
                listener.enterSysdcon_nolist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSysdcon_nolist" ):
                listener.exitSysdcon_nolist(self)




    def sysdcon_nolist(self):

        localctx = HaskellParser.Sysdcon_nolistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 408, self.RULE_sysdcon_nolist)
        try:
            self.state = 2678
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,306,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2666
                self.match(HaskellParser.OpenRoundBracket)
                self.state = 2667
                self.match(HaskellParser.CloseRoundBracket)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2668
                self.match(HaskellParser.OpenRoundBracket)
                self.state = 2669
                self.commas()
                self.state = 2670
                self.match(HaskellParser.CloseRoundBracket)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2672
                self.match(HaskellParser.OpenBoxParen)
                self.state = 2673
                self.match(HaskellParser.CloseBoxParen)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2674
                self.match(HaskellParser.OpenBoxParen)
                self.state = 2675
                self.commas()
                self.state = 2676
                self.match(HaskellParser.CloseBoxParen)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SysdconContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sysdcon_nolist(self):
            return self.getTypedRuleContext(HaskellParser.Sysdcon_nolistContext,0)


        def OpenSquareBracket(self):
            return self.getToken(HaskellParser.OpenSquareBracket, 0)

        def CloseSquareBracket(self):
            return self.getToken(HaskellParser.CloseSquareBracket, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_sysdcon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSysdcon" ):
                listener.enterSysdcon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSysdcon" ):
                listener.exitSysdcon(self)




    def sysdcon(self):

        localctx = HaskellParser.SysdconContext(self, self._ctx, self.state)
        self.enterRule(localctx, 410, self.RULE_sysdcon)
        try:
            self.state = 2683
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.OpenBoxParen, HaskellParser.OpenRoundBracket]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2680
                self.sysdcon_nolist()
                pass
            elif token in [HaskellParser.OpenSquareBracket]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2681
                self.match(HaskellParser.OpenSquareBracket)
                self.state = 2682
                self.match(HaskellParser.CloseSquareBracket)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def consym(self):
            return self.getTypedRuleContext(HaskellParser.ConsymContext,0)


        def BackQuote(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.BackQuote)
            else:
                return self.getToken(HaskellParser.BackQuote, i)

        def conid(self):
            return self.getTypedRuleContext(HaskellParser.ConidContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_conop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConop" ):
                listener.enterConop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConop" ):
                listener.exitConop(self)




    def conop(self):

        localctx = HaskellParser.ConopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 412, self.RULE_conop)
        try:
            self.state = 2690
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.Colon]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2685
                self.consym()
                pass
            elif token in [HaskellParser.BackQuote]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2686
                self.match(HaskellParser.BackQuote)
                self.state = 2687
                self.conid()
                self.state = 2688
                self.match(HaskellParser.BackQuote)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QconopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def gconsym(self):
            return self.getTypedRuleContext(HaskellParser.GconsymContext,0)


        def BackQuote(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.BackQuote)
            else:
                return self.getToken(HaskellParser.BackQuote, i)

        def qconid(self):
            return self.getTypedRuleContext(HaskellParser.QconidContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_qconop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQconop" ):
                listener.enterQconop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQconop" ):
                listener.exitQconop(self)




    def qconop(self):

        localctx = HaskellParser.QconopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 414, self.RULE_qconop)
        try:
            self.state = 2697
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.Colon, HaskellParser.CONID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2692
                self.gconsym()
                pass
            elif token in [HaskellParser.BackQuote]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2693
                self.match(HaskellParser.BackQuote)
                self.state = 2694
                self.qconid()
                self.state = 2695
                self.match(HaskellParser.BackQuote)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GconsymContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Colon(self):
            return self.getToken(HaskellParser.Colon, 0)

        def qconsym(self):
            return self.getTypedRuleContext(HaskellParser.QconsymContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_gconsym

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGconsym" ):
                listener.enterGconsym(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGconsym" ):
                listener.exitGconsym(self)




    def gconsym(self):

        localctx = HaskellParser.GconsymContext(self, self._ctx, self.state)
        self.enterRule(localctx, 416, self.RULE_gconsym)
        try:
            self.state = 2701
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,310,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2699
                self.match(HaskellParser.Colon)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2700
                self.qconsym()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GtyconContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ntgtycon(self):
            return self.getTypedRuleContext(HaskellParser.NtgtyconContext,0)


        def OpenRoundBracket(self):
            return self.getToken(HaskellParser.OpenRoundBracket, 0)

        def CloseRoundBracket(self):
            return self.getToken(HaskellParser.CloseRoundBracket, 0)

        def OpenBoxParen(self):
            return self.getToken(HaskellParser.OpenBoxParen, 0)

        def CloseBoxParen(self):
            return self.getToken(HaskellParser.CloseBoxParen, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_gtycon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGtycon" ):
                listener.enterGtycon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGtycon" ):
                listener.exitGtycon(self)




    def gtycon(self):

        localctx = HaskellParser.GtyconContext(self, self._ctx, self.state)
        self.enterRule(localctx, 418, self.RULE_gtycon)
        try:
            self.state = 2708
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,311,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2703
                self.ntgtycon()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2704
                self.match(HaskellParser.OpenRoundBracket)
                self.state = 2705
                self.match(HaskellParser.CloseRoundBracket)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2706
                self.match(HaskellParser.OpenBoxParen)
                self.state = 2707
                self.match(HaskellParser.CloseBoxParen)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NtgtyconContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def oqtycon(self):
            return self.getTypedRuleContext(HaskellParser.OqtyconContext,0)


        def OpenRoundBracket(self):
            return self.getToken(HaskellParser.OpenRoundBracket, 0)

        def commas(self):
            return self.getTypedRuleContext(HaskellParser.CommasContext,0)


        def CloseRoundBracket(self):
            return self.getToken(HaskellParser.CloseRoundBracket, 0)

        def OpenBoxParen(self):
            return self.getToken(HaskellParser.OpenBoxParen, 0)

        def CloseBoxParen(self):
            return self.getToken(HaskellParser.CloseBoxParen, 0)

        def Arrow(self):
            return self.getToken(HaskellParser.Arrow, 0)

        def OpenSquareBracket(self):
            return self.getToken(HaskellParser.OpenSquareBracket, 0)

        def CloseSquareBracket(self):
            return self.getToken(HaskellParser.CloseSquareBracket, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_ntgtycon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNtgtycon" ):
                listener.enterNtgtycon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNtgtycon" ):
                listener.exitNtgtycon(self)




    def ntgtycon(self):

        localctx = HaskellParser.NtgtyconContext(self, self._ctx, self.state)
        self.enterRule(localctx, 420, self.RULE_ntgtycon)
        try:
            self.state = 2724
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,312,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2710
                self.oqtycon()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2711
                self.match(HaskellParser.OpenRoundBracket)
                self.state = 2712
                self.commas()
                self.state = 2713
                self.match(HaskellParser.CloseRoundBracket)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2715
                self.match(HaskellParser.OpenBoxParen)
                self.state = 2716
                self.commas()
                self.state = 2717
                self.match(HaskellParser.CloseBoxParen)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2719
                self.match(HaskellParser.OpenRoundBracket)
                self.state = 2720
                self.match(HaskellParser.Arrow)
                self.state = 2721
                self.match(HaskellParser.CloseRoundBracket)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2722
                self.match(HaskellParser.OpenSquareBracket)
                self.state = 2723
                self.match(HaskellParser.CloseSquareBracket)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OqtyconContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qtycon(self):
            return self.getTypedRuleContext(HaskellParser.QtyconContext,0)


        def OpenRoundBracket(self):
            return self.getToken(HaskellParser.OpenRoundBracket, 0)

        def qtyconsym(self):
            return self.getTypedRuleContext(HaskellParser.QtyconsymContext,0)


        def CloseRoundBracket(self):
            return self.getToken(HaskellParser.CloseRoundBracket, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_oqtycon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOqtycon" ):
                listener.enterOqtycon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOqtycon" ):
                listener.exitOqtycon(self)




    def oqtycon(self):

        localctx = HaskellParser.OqtyconContext(self, self._ctx, self.state)
        self.enterRule(localctx, 422, self.RULE_oqtycon)
        try:
            self.state = 2731
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.CONID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2726
                self.qtycon()
                pass
            elif token in [HaskellParser.OpenRoundBracket]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2727
                self.match(HaskellParser.OpenRoundBracket)
                self.state = 2728
                self.qtyconsym()
                self.state = 2729
                self.match(HaskellParser.CloseRoundBracket)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QtyconopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qtyconsym(self):
            return self.getTypedRuleContext(HaskellParser.QtyconsymContext,0)


        def BackQuote(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.BackQuote)
            else:
                return self.getToken(HaskellParser.BackQuote, i)

        def qtycon(self):
            return self.getTypedRuleContext(HaskellParser.QtyconContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_qtyconop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQtyconop" ):
                listener.enterQtyconop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQtyconop" ):
                listener.exitQtyconop(self)




    def qtyconop(self):

        localctx = HaskellParser.QtyconopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 424, self.RULE_qtyconop)
        try:
            self.state = 2738
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.Hash, HaskellParser.Less, HaskellParser.Greater, HaskellParser.Ampersand, HaskellParser.Pipe, HaskellParser.Bang, HaskellParser.Caret, HaskellParser.Plus, HaskellParser.Minus, HaskellParser.Asterisk, HaskellParser.Percent, HaskellParser.Divide, HaskellParser.Tilde, HaskellParser.Atsign, HaskellParser.Dollar, HaskellParser.Dot, HaskellParser.QuestionMark, HaskellParser.Colon, HaskellParser.Eq, HaskellParser.ReverseSlash, HaskellParser.CONID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2733
                self.qtyconsym()
                pass
            elif token in [HaskellParser.BackQuote]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2734
                self.match(HaskellParser.BackQuote)
                self.state = 2735
                self.qtycon()
                self.state = 2736
                self.match(HaskellParser.BackQuote)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QtyconContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tycon(self):
            return self.getTypedRuleContext(HaskellParser.TyconContext,0)


        def modid(self):
            return self.getTypedRuleContext(HaskellParser.ModidContext,0)


        def Dot(self):
            return self.getToken(HaskellParser.Dot, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_qtycon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQtycon" ):
                listener.enterQtycon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQtycon" ):
                listener.exitQtycon(self)




    def qtycon(self):

        localctx = HaskellParser.QtyconContext(self, self._ctx, self.state)
        self.enterRule(localctx, 426, self.RULE_qtycon)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2743
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,315,self._ctx)
            if la_ == 1:
                self.state = 2740
                self.modid()
                self.state = 2741
                self.match(HaskellParser.Dot)


            self.state = 2745
            self.tycon()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TyconContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conid(self):
            return self.getTypedRuleContext(HaskellParser.ConidContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_tycon

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTycon" ):
                listener.enterTycon(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTycon" ):
                listener.exitTycon(self)




    def tycon(self):

        localctx = HaskellParser.TyconContext(self, self._ctx, self.state)
        self.enterRule(localctx, 428, self.RULE_tycon)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2747
            self.conid()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QtyconsymContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qconsym(self):
            return self.getTypedRuleContext(HaskellParser.QconsymContext,0)


        def qvarsym(self):
            return self.getTypedRuleContext(HaskellParser.QvarsymContext,0)


        def tyconsym(self):
            return self.getTypedRuleContext(HaskellParser.TyconsymContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_qtyconsym

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQtyconsym" ):
                listener.enterQtyconsym(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQtyconsym" ):
                listener.exitQtyconsym(self)




    def qtyconsym(self):

        localctx = HaskellParser.QtyconsymContext(self, self._ctx, self.state)
        self.enterRule(localctx, 430, self.RULE_qtyconsym)
        try:
            self.state = 2752
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,316,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2749
                self.qconsym()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2750
                self.qvarsym()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2751
                self.tyconsym()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TyconsymContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def consym(self):
            return self.getTypedRuleContext(HaskellParser.ConsymContext,0)


        def varsym(self):
            return self.getTypedRuleContext(HaskellParser.VarsymContext,0)


        def Colon(self):
            return self.getToken(HaskellParser.Colon, 0)

        def Minus(self):
            return self.getToken(HaskellParser.Minus, 0)

        def Dot(self):
            return self.getToken(HaskellParser.Dot, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_tyconsym

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTyconsym" ):
                listener.enterTyconsym(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTyconsym" ):
                listener.exitTyconsym(self)




    def tyconsym(self):

        localctx = HaskellParser.TyconsymContext(self, self._ctx, self.state)
        self.enterRule(localctx, 432, self.RULE_tyconsym)
        try:
            self.state = 2759
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,317,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2754
                self.consym()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2755
                self.varsym()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2756
                self.match(HaskellParser.Colon)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2757
                self.match(HaskellParser.Minus)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2758
                self.match(HaskellParser.Dot)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varop(self):
            return self.getTypedRuleContext(HaskellParser.VaropContext,0)


        def conop(self):
            return self.getTypedRuleContext(HaskellParser.ConopContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp" ):
                listener.enterOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp" ):
                listener.exitOp(self)




    def op(self):

        localctx = HaskellParser.OpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 434, self.RULE_op)
        try:
            self.state = 2763
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,318,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2761
                self.varop()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2762
                self.conop()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VaropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varsym(self):
            return self.getTypedRuleContext(HaskellParser.VarsymContext,0)


        def BackQuote(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.BackQuote)
            else:
                return self.getToken(HaskellParser.BackQuote, i)

        def varid(self):
            return self.getTypedRuleContext(HaskellParser.VaridContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_varop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarop" ):
                listener.enterVarop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarop" ):
                listener.exitVarop(self)




    def varop(self):

        localctx = HaskellParser.VaropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 436, self.RULE_varop)
        try:
            self.state = 2770
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.Hash, HaskellParser.Less, HaskellParser.Greater, HaskellParser.Ampersand, HaskellParser.Pipe, HaskellParser.Bang, HaskellParser.Caret, HaskellParser.Plus, HaskellParser.Minus, HaskellParser.Asterisk, HaskellParser.Percent, HaskellParser.Divide, HaskellParser.Tilde, HaskellParser.Atsign, HaskellParser.Dollar, HaskellParser.Dot, HaskellParser.QuestionMark, HaskellParser.Colon, HaskellParser.Eq, HaskellParser.ReverseSlash]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2765
                self.varsym()
                pass
            elif token in [HaskellParser.BackQuote]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2766
                self.match(HaskellParser.BackQuote)
                self.state = 2767
                self.varid()
                self.state = 2768
                self.match(HaskellParser.BackQuote)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qvarop(self):
            return self.getTypedRuleContext(HaskellParser.QvaropContext,0)


        def qconop(self):
            return self.getTypedRuleContext(HaskellParser.QconopContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_qop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQop" ):
                listener.enterQop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQop" ):
                listener.exitQop(self)




    def qop(self):

        localctx = HaskellParser.QopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 438, self.RULE_qop)
        try:
            self.state = 2774
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,320,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2772
                self.qvarop()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2773
                self.qconop()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QopmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qvaropm(self):
            return self.getTypedRuleContext(HaskellParser.QvaropmContext,0)


        def qconop(self):
            return self.getTypedRuleContext(HaskellParser.QconopContext,0)


        def hole_op(self):
            return self.getTypedRuleContext(HaskellParser.Hole_opContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_qopm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQopm" ):
                listener.enterQopm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQopm" ):
                listener.exitQopm(self)




    def qopm(self):

        localctx = HaskellParser.QopmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 440, self.RULE_qopm)
        try:
            self.state = 2779
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,321,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2776
                self.qvaropm()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2777
                self.qconop()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2778
                self.hole_op()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Hole_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BackQuote(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.BackQuote)
            else:
                return self.getToken(HaskellParser.BackQuote, i)

        def WILDCARD(self):
            return self.getToken(HaskellParser.WILDCARD, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_hole_op

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHole_op" ):
                listener.enterHole_op(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHole_op" ):
                listener.exitHole_op(self)




    def hole_op(self):

        localctx = HaskellParser.Hole_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 442, self.RULE_hole_op)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2781
            self.match(HaskellParser.BackQuote)
            self.state = 2782
            self.match(HaskellParser.WILDCARD)
            self.state = 2783
            self.match(HaskellParser.BackQuote)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QvaropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qvarsym(self):
            return self.getTypedRuleContext(HaskellParser.QvarsymContext,0)


        def BackQuote(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.BackQuote)
            else:
                return self.getToken(HaskellParser.BackQuote, i)

        def qvarid(self):
            return self.getTypedRuleContext(HaskellParser.QvaridContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_qvarop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQvarop" ):
                listener.enterQvarop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQvarop" ):
                listener.exitQvarop(self)




    def qvarop(self):

        localctx = HaskellParser.QvaropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 444, self.RULE_qvarop)
        try:
            self.state = 2790
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.Hash, HaskellParser.Less, HaskellParser.Greater, HaskellParser.Ampersand, HaskellParser.Pipe, HaskellParser.Bang, HaskellParser.Caret, HaskellParser.Plus, HaskellParser.Minus, HaskellParser.Asterisk, HaskellParser.Percent, HaskellParser.Divide, HaskellParser.Tilde, HaskellParser.Atsign, HaskellParser.Dollar, HaskellParser.Dot, HaskellParser.QuestionMark, HaskellParser.Colon, HaskellParser.Eq, HaskellParser.ReverseSlash, HaskellParser.CONID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2785
                self.qvarsym()
                pass
            elif token in [HaskellParser.BackQuote]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2786
                self.match(HaskellParser.BackQuote)
                self.state = 2787
                self.qvarid()
                self.state = 2788
                self.match(HaskellParser.BackQuote)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QvaropmContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qvarsym_no_minus(self):
            return self.getTypedRuleContext(HaskellParser.Qvarsym_no_minusContext,0)


        def BackQuote(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.BackQuote)
            else:
                return self.getToken(HaskellParser.BackQuote, i)

        def qvarid(self):
            return self.getTypedRuleContext(HaskellParser.QvaridContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_qvaropm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQvaropm" ):
                listener.enterQvaropm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQvaropm" ):
                listener.exitQvaropm(self)




    def qvaropm(self):

        localctx = HaskellParser.QvaropmContext(self, self._ctx, self.state)
        self.enterRule(localctx, 446, self.RULE_qvaropm)
        try:
            self.state = 2797
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.Hash, HaskellParser.Less, HaskellParser.Greater, HaskellParser.Ampersand, HaskellParser.Pipe, HaskellParser.Bang, HaskellParser.Caret, HaskellParser.Plus, HaskellParser.Minus, HaskellParser.Asterisk, HaskellParser.Percent, HaskellParser.Divide, HaskellParser.Tilde, HaskellParser.Atsign, HaskellParser.Dollar, HaskellParser.Dot, HaskellParser.QuestionMark, HaskellParser.Colon, HaskellParser.Eq, HaskellParser.ReverseSlash, HaskellParser.CONID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2792
                self.qvarsym_no_minus()
                pass
            elif token in [HaskellParser.BackQuote]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2793
                self.match(HaskellParser.BackQuote)
                self.state = 2794
                self.qvarid()
                self.state = 2795
                self.match(HaskellParser.BackQuote)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TyvarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varid(self):
            return self.getTypedRuleContext(HaskellParser.VaridContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_tyvar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTyvar" ):
                listener.enterTyvar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTyvar" ):
                listener.exitTyvar(self)




    def tyvar(self):

        localctx = HaskellParser.TyvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 448, self.RULE_tyvar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2799
            self.varid()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TyvaropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BackQuote(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.BackQuote)
            else:
                return self.getToken(HaskellParser.BackQuote, i)

        def tyvarid(self):
            return self.getTypedRuleContext(HaskellParser.TyvaridContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_tyvarop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTyvarop" ):
                listener.enterTyvarop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTyvarop" ):
                listener.exitTyvarop(self)




    def tyvarop(self):

        localctx = HaskellParser.TyvaropContext(self, self._ctx, self.state)
        self.enterRule(localctx, 450, self.RULE_tyvarop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2801
            self.match(HaskellParser.BackQuote)
            self.state = 2802
            self.tyvarid()
            self.state = 2803
            self.match(HaskellParser.BackQuote)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TyvaridContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varid(self):
            return self.getTypedRuleContext(HaskellParser.VaridContext,0)


        def special_id(self):
            return self.getTypedRuleContext(HaskellParser.Special_idContext,0)


        def UNSAFE(self):
            return self.getToken(HaskellParser.UNSAFE, 0)

        def SAFE(self):
            return self.getToken(HaskellParser.SAFE, 0)

        def INTERRUPTIBLE(self):
            return self.getToken(HaskellParser.INTERRUPTIBLE, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_tyvarid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTyvarid" ):
                listener.enterTyvarid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTyvarid" ):
                listener.exitTyvarid(self)




    def tyvarid(self):

        localctx = HaskellParser.TyvaridContext(self, self._ctx, self.state)
        self.enterRule(localctx, 452, self.RULE_tyvarid)
        try:
            self.state = 2810
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,324,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2805
                self.varid()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2806
                self.special_id()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 2807
                self.match(HaskellParser.UNSAFE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 2808
                self.match(HaskellParser.SAFE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 2809
                self.match(HaskellParser.INTERRUPTIBLE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TyclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conid(self):
            return self.getTypedRuleContext(HaskellParser.ConidContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_tycls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTycls" ):
                listener.enterTycls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTycls" ):
                listener.exitTycls(self)




    def tycls(self):

        localctx = HaskellParser.TyclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 454, self.RULE_tycls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2812
            self.conid()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QtyclsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tycls(self):
            return self.getTypedRuleContext(HaskellParser.TyclsContext,0)


        def modid(self):
            return self.getTypedRuleContext(HaskellParser.ModidContext,0)


        def Dot(self):
            return self.getToken(HaskellParser.Dot, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_qtycls

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQtycls" ):
                listener.enterQtycls(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQtycls" ):
                listener.exitQtycls(self)




    def qtycls(self):

        localctx = HaskellParser.QtyclsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 456, self.RULE_qtycls)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2817
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,325,self._ctx)
            if la_ == 1:
                self.state = 2814
                self.modid()
                self.state = 2815
                self.match(HaskellParser.Dot)


            self.state = 2819
            self.tycls()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varid(self):
            return self.getTypedRuleContext(HaskellParser.VaridContext,0)


        def OpenRoundBracket(self):
            return self.getToken(HaskellParser.OpenRoundBracket, 0)

        def varsym(self):
            return self.getTypedRuleContext(HaskellParser.VarsymContext,0)


        def CloseRoundBracket(self):
            return self.getToken(HaskellParser.CloseRoundBracket, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)




    def var(self):

        localctx = HaskellParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 458, self.RULE_var)
        try:
            self.state = 2826
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.AS, HaskellParser.HIDING, HaskellParser.QUALIFIED, HaskellParser.EXPORT, HaskellParser.STDCALL, HaskellParser.CCALL, HaskellParser.CAPI, HaskellParser.JSCALL, HaskellParser.STOCK, HaskellParser.ANYCLASS, HaskellParser.VIA, HaskellParser.VARID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2821
                self.varid()
                pass
            elif token in [HaskellParser.OpenRoundBracket]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2822
                self.match(HaskellParser.OpenRoundBracket)
                self.state = 2823
                self.varsym()
                self.state = 2824
                self.match(HaskellParser.CloseRoundBracket)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QvarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qvarid(self):
            return self.getTypedRuleContext(HaskellParser.QvaridContext,0)


        def OpenRoundBracket(self):
            return self.getToken(HaskellParser.OpenRoundBracket, 0)

        def qvarsym(self):
            return self.getTypedRuleContext(HaskellParser.QvarsymContext,0)


        def CloseRoundBracket(self):
            return self.getToken(HaskellParser.CloseRoundBracket, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_qvar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQvar" ):
                listener.enterQvar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQvar" ):
                listener.exitQvar(self)




    def qvar(self):

        localctx = HaskellParser.QvarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 460, self.RULE_qvar)
        try:
            self.state = 2833
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.AS, HaskellParser.HIDING, HaskellParser.QUALIFIED, HaskellParser.EXPORT, HaskellParser.STDCALL, HaskellParser.CCALL, HaskellParser.CAPI, HaskellParser.JSCALL, HaskellParser.STOCK, HaskellParser.ANYCLASS, HaskellParser.VIA, HaskellParser.VARID, HaskellParser.CONID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2828
                self.qvarid()
                pass
            elif token in [HaskellParser.OpenRoundBracket]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2829
                self.match(HaskellParser.OpenRoundBracket)
                self.state = 2830
                self.qvarsym()
                self.state = 2831
                self.match(HaskellParser.CloseRoundBracket)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QvaridContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varid(self):
            return self.getTypedRuleContext(HaskellParser.VaridContext,0)


        def modid(self):
            return self.getTypedRuleContext(HaskellParser.ModidContext,0)


        def Dot(self):
            return self.getToken(HaskellParser.Dot, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_qvarid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQvarid" ):
                listener.enterQvarid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQvarid" ):
                listener.exitQvarid(self)




    def qvarid(self):

        localctx = HaskellParser.QvaridContext(self, self._ctx, self.state)
        self.enterRule(localctx, 462, self.RULE_qvarid)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2838
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HaskellParser.CONID:
                self.state = 2835
                self.modid()
                self.state = 2836
                self.match(HaskellParser.Dot)


            self.state = 2840
            self.varid()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VaridContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARID(self):
            return self.getToken(HaskellParser.VARID, 0)

        def special_id(self):
            return self.getTypedRuleContext(HaskellParser.Special_idContext,0)


        def Hash(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Hash)
            else:
                return self.getToken(HaskellParser.Hash, i)

        def getRuleIndex(self):
            return HaskellParser.RULE_varid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarid" ):
                listener.enterVarid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarid" ):
                listener.exitVarid(self)




    def varid(self):

        localctx = HaskellParser.VaridContext(self, self._ctx, self.state)
        self.enterRule(localctx, 464, self.RULE_varid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2844
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.VARID]:
                self.state = 2842
                self.match(HaskellParser.VARID)
                pass
            elif token in [HaskellParser.AS, HaskellParser.HIDING, HaskellParser.QUALIFIED, HaskellParser.EXPORT, HaskellParser.STDCALL, HaskellParser.CCALL, HaskellParser.CAPI, HaskellParser.JSCALL, HaskellParser.STOCK, HaskellParser.ANYCLASS, HaskellParser.VIA]:
                self.state = 2843
                self.special_id()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 2849
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,330,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2846
                    self.match(HaskellParser.Hash) 
                self.state = 2851
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,330,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QvarsymContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varsym(self):
            return self.getTypedRuleContext(HaskellParser.VarsymContext,0)


        def modid(self):
            return self.getTypedRuleContext(HaskellParser.ModidContext,0)


        def Dot(self):
            return self.getToken(HaskellParser.Dot, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_qvarsym

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQvarsym" ):
                listener.enterQvarsym(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQvarsym" ):
                listener.exitQvarsym(self)




    def qvarsym(self):

        localctx = HaskellParser.QvarsymContext(self, self._ctx, self.state)
        self.enterRule(localctx, 466, self.RULE_qvarsym)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2855
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HaskellParser.CONID:
                self.state = 2852
                self.modid()
                self.state = 2853
                self.match(HaskellParser.Dot)


            self.state = 2857
            self.varsym()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Qvarsym_no_minusContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varsym_no_minus(self):
            return self.getTypedRuleContext(HaskellParser.Varsym_no_minusContext,0)


        def qvarsym(self):
            return self.getTypedRuleContext(HaskellParser.QvarsymContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_qvarsym_no_minus

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQvarsym_no_minus" ):
                listener.enterQvarsym_no_minus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQvarsym_no_minus" ):
                listener.exitQvarsym_no_minus(self)




    def qvarsym_no_minus(self):

        localctx = HaskellParser.Qvarsym_no_minusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 468, self.RULE_qvarsym_no_minus)
        try:
            self.state = 2861
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,332,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 2859
                self.varsym_no_minus()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 2860
                self.qvarsym()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsymContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def varsym_no_minus(self):
            return self.getTypedRuleContext(HaskellParser.Varsym_no_minusContext,0)


        def Minus(self):
            return self.getToken(HaskellParser.Minus, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_varsym

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarsym" ):
                listener.enterVarsym(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarsym" ):
                listener.exitVarsym(self)




    def varsym(self):

        localctx = HaskellParser.VarsymContext(self, self._ctx, self.state)
        self.enterRule(localctx, 470, self.RULE_varsym)
        try:
            self.state = 2865
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.Hash, HaskellParser.Less, HaskellParser.Greater, HaskellParser.Ampersand, HaskellParser.Pipe, HaskellParser.Bang, HaskellParser.Caret, HaskellParser.Plus, HaskellParser.Asterisk, HaskellParser.Percent, HaskellParser.Divide, HaskellParser.Tilde, HaskellParser.Atsign, HaskellParser.Dollar, HaskellParser.Dot, HaskellParser.QuestionMark, HaskellParser.Colon, HaskellParser.Eq, HaskellParser.ReverseSlash]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2863
                self.varsym_no_minus()
                pass
            elif token in [HaskellParser.Minus]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2864
                self.match(HaskellParser.Minus)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Varsym_no_minusContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ascSymbol(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.AscSymbolContext)
            else:
                return self.getTypedRuleContext(HaskellParser.AscSymbolContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_varsym_no_minus

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarsym_no_minus" ):
                listener.enterVarsym_no_minus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarsym_no_minus" ):
                listener.exitVarsym_no_minus(self)




    def varsym_no_minus(self):

        localctx = HaskellParser.Varsym_no_minusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 472, self.RULE_varsym_no_minus)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2868 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 2867
                    self.ascSymbol()

                else:
                    raise NoViableAltException(self)
                self.state = 2870 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,334,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Special_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AS(self):
            return self.getToken(HaskellParser.AS, 0)

        def QUALIFIED(self):
            return self.getToken(HaskellParser.QUALIFIED, 0)

        def HIDING(self):
            return self.getToken(HaskellParser.HIDING, 0)

        def EXPORT(self):
            return self.getToken(HaskellParser.EXPORT, 0)

        def STDCALL(self):
            return self.getToken(HaskellParser.STDCALL, 0)

        def CCALL(self):
            return self.getToken(HaskellParser.CCALL, 0)

        def CAPI(self):
            return self.getToken(HaskellParser.CAPI, 0)

        def JSCALL(self):
            return self.getToken(HaskellParser.JSCALL, 0)

        def STOCK(self):
            return self.getToken(HaskellParser.STOCK, 0)

        def ANYCLASS(self):
            return self.getToken(HaskellParser.ANYCLASS, 0)

        def VIA(self):
            return self.getToken(HaskellParser.VIA, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_special_id

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecial_id" ):
                listener.enterSpecial_id(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecial_id" ):
                listener.exitSpecial_id(self)




    def special_id(self):

        localctx = HaskellParser.Special_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 474, self.RULE_special_id)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2872
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HaskellParser.AS) | (1 << HaskellParser.HIDING) | (1 << HaskellParser.QUALIFIED) | (1 << HaskellParser.EXPORT) | (1 << HaskellParser.STDCALL) | (1 << HaskellParser.CCALL) | (1 << HaskellParser.CAPI) | (1 << HaskellParser.JSCALL) | (1 << HaskellParser.STOCK) | (1 << HaskellParser.ANYCLASS) | (1 << HaskellParser.VIA))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QconidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conid(self):
            return self.getTypedRuleContext(HaskellParser.ConidContext,0)


        def modid(self):
            return self.getTypedRuleContext(HaskellParser.ModidContext,0)


        def Dot(self):
            return self.getToken(HaskellParser.Dot, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_qconid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQconid" ):
                listener.enterQconid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQconid" ):
                listener.exitQconid(self)




    def qconid(self):

        localctx = HaskellParser.QconidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 476, self.RULE_qconid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2877
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,335,self._ctx)
            if la_ == 1:
                self.state = 2874
                self.modid()
                self.state = 2875
                self.match(HaskellParser.Dot)


            self.state = 2879
            self.conid()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONID(self):
            return self.getToken(HaskellParser.CONID, 0)

        def Hash(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Hash)
            else:
                return self.getToken(HaskellParser.Hash, i)

        def getRuleIndex(self):
            return HaskellParser.RULE_conid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConid" ):
                listener.enterConid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConid" ):
                listener.exitConid(self)




    def conid(self):

        localctx = HaskellParser.ConidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 478, self.RULE_conid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2881
            self.match(HaskellParser.CONID)
            self.state = 2885
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,336,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2882
                    self.match(HaskellParser.Hash) 
                self.state = 2887
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,336,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QconsymContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def consym(self):
            return self.getTypedRuleContext(HaskellParser.ConsymContext,0)


        def modid(self):
            return self.getTypedRuleContext(HaskellParser.ModidContext,0)


        def Dot(self):
            return self.getToken(HaskellParser.Dot, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_qconsym

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQconsym" ):
                listener.enterQconsym(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQconsym" ):
                listener.exitQconsym(self)




    def qconsym(self):

        localctx = HaskellParser.QconsymContext(self, self._ctx, self.state)
        self.enterRule(localctx, 480, self.RULE_qconsym)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2891
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HaskellParser.CONID:
                self.state = 2888
                self.modid()
                self.state = 2889
                self.match(HaskellParser.Dot)


            self.state = 2893
            self.consym()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConsymContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Colon(self):
            return self.getToken(HaskellParser.Colon, 0)

        def ascSymbol(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.AscSymbolContext)
            else:
                return self.getTypedRuleContext(HaskellParser.AscSymbolContext,i)


        def getRuleIndex(self):
            return HaskellParser.RULE_consym

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConsym" ):
                listener.enterConsym(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConsym" ):
                listener.exitConsym(self)




    def consym(self):

        localctx = HaskellParser.ConsymContext(self, self._ctx, self.state)
        self.enterRule(localctx, 482, self.RULE_consym)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2895
            self.match(HaskellParser.Colon)
            self.state = 2899
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,338,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2896
                    self.ascSymbol() 
                self.state = 2901
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,338,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integer(self):
            return self.getTypedRuleContext(HaskellParser.IntegerContext,0)


        def pfloat(self):
            return self.getTypedRuleContext(HaskellParser.PfloatContext,0)


        def pchar(self):
            return self.getTypedRuleContext(HaskellParser.PcharContext,0)


        def pstring(self):
            return self.getTypedRuleContext(HaskellParser.PstringContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = HaskellParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 484, self.RULE_literal)
        try:
            self.state = 2906
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HaskellParser.DECIMAL, HaskellParser.OCTAL, HaskellParser.HEXADECIMAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 2902
                self.integer()
                pass
            elif token in [HaskellParser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 2903
                self.pfloat()
                pass
            elif token in [HaskellParser.CHAR]:
                self.enterOuterAlt(localctx, 3)
                self.state = 2904
                self.pchar()
                pass
            elif token in [HaskellParser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 2905
                self.pstring()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VOCURLY(self):
            return self.getToken(HaskellParser.VOCURLY, 0)

        def OCURLY(self):
            return self.getToken(HaskellParser.OCURLY, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_opn

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpn" ):
                listener.enterOpn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpn" ):
                listener.exitOpn(self)




    def opn(self):

        localctx = HaskellParser.OpnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 486, self.RULE_opn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2908
            _la = self._input.LA(1)
            if not(_la==HaskellParser.OCURLY or _la==HaskellParser.VOCURLY):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CloseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VCCURLY(self):
            return self.getToken(HaskellParser.VCCURLY, 0)

        def CCURLY(self):
            return self.getToken(HaskellParser.CCURLY, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_close

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClose" ):
                listener.enterClose(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClose" ):
                listener.exitClose(self)




    def close(self):

        localctx = HaskellParser.CloseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 488, self.RULE_close)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2910
            _la = self._input.LA(1)
            if not(_la==HaskellParser.CCURLY or _la==HaskellParser.VCCURLY):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SemiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Semi(self):
            return self.getToken(HaskellParser.Semi, 0)

        def SEMI(self):
            return self.getToken(HaskellParser.SEMI, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_semi

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSemi" ):
                listener.enterSemi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSemi" ):
                listener.exitSemi(self)




    def semi(self):

        localctx = HaskellParser.SemiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 490, self.RULE_semi)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2912
            _la = self._input.LA(1)
            if not(_la==HaskellParser.Semi or _la==HaskellParser.SEMI):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModidContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conid(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HaskellParser.ConidContext)
            else:
                return self.getTypedRuleContext(HaskellParser.ConidContext,i)


        def Dot(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Dot)
            else:
                return self.getToken(HaskellParser.Dot, i)

        def getRuleIndex(self):
            return HaskellParser.RULE_modid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModid" ):
                listener.enterModid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModid" ):
                listener.exitModid(self)




    def modid(self):

        localctx = HaskellParser.ModidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 492, self.RULE_modid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2919
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,340,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 2914
                    self.conid()
                    self.state = 2915
                    self.match(HaskellParser.Dot) 
                self.state = 2921
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,340,self._ctx)

            self.state = 2922
            self.conid()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Comma(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Comma)
            else:
                return self.getToken(HaskellParser.Comma, i)

        def getRuleIndex(self):
            return HaskellParser.RULE_commas

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommas" ):
                listener.enterCommas(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommas" ):
                listener.exitCommas(self)




    def commas(self):

        localctx = HaskellParser.CommasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 494, self.RULE_commas)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2925 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 2924
                self.match(HaskellParser.Comma)
                self.state = 2927 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==HaskellParser.Comma):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Pipe(self, i:int=None):
            if i is None:
                return self.getTokens(HaskellParser.Pipe)
            else:
                return self.getToken(HaskellParser.Pipe, i)

        def getRuleIndex(self):
            return HaskellParser.RULE_bars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBars" ):
                listener.enterBars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBars" ):
                listener.exitBars(self)




    def bars(self):

        localctx = HaskellParser.BarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 496, self.RULE_bars)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2930 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 2929
                    self.match(HaskellParser.Pipe)

                else:
                    raise NoViableAltException(self)
                self.state = 2932 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,342,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OpenRoundBracket(self):
            return self.getToken(HaskellParser.OpenRoundBracket, 0)

        def CloseRoundBracket(self):
            return self.getToken(HaskellParser.CloseRoundBracket, 0)

        def Comma(self):
            return self.getToken(HaskellParser.Comma, 0)

        def Semi(self):
            return self.getToken(HaskellParser.Semi, 0)

        def OpenSquareBracket(self):
            return self.getToken(HaskellParser.OpenSquareBracket, 0)

        def CloseSquareBracket(self):
            return self.getToken(HaskellParser.CloseSquareBracket, 0)

        def BackQuote(self):
            return self.getToken(HaskellParser.BackQuote, 0)

        def OCURLY(self):
            return self.getToken(HaskellParser.OCURLY, 0)

        def CCURLY(self):
            return self.getToken(HaskellParser.CCURLY, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_special

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecial" ):
                listener.enterSpecial(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecial" ):
                listener.exitSpecial(self)




    def special(self):

        localctx = HaskellParser.SpecialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 498, self.RULE_special)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2934
            _la = self._input.LA(1)
            if not(((((_la - 100)) & ~0x3f) == 0 and ((1 << (_la - 100)) & ((1 << (HaskellParser.Semi - 100)) | (1 << (HaskellParser.Comma - 100)) | (1 << (HaskellParser.BackQuote - 100)) | (1 << (HaskellParser.OpenRoundBracket - 100)) | (1 << (HaskellParser.CloseRoundBracket - 100)) | (1 << (HaskellParser.OpenSquareBracket - 100)) | (1 << (HaskellParser.CloseSquareBracket - 100)) | (1 << (HaskellParser.OCURLY - 100)) | (1 << (HaskellParser.CCURLY - 100)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SymbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ascSymbol(self):
            return self.getTypedRuleContext(HaskellParser.AscSymbolContext,0)


        def getRuleIndex(self):
            return HaskellParser.RULE_symbol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSymbol" ):
                listener.enterSymbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSymbol" ):
                listener.exitSymbol(self)




    def symbol(self):

        localctx = HaskellParser.SymbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 500, self.RULE_symbol)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2936
            self.ascSymbol()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AscSymbolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Bang(self):
            return self.getToken(HaskellParser.Bang, 0)

        def Hash(self):
            return self.getToken(HaskellParser.Hash, 0)

        def Dollar(self):
            return self.getToken(HaskellParser.Dollar, 0)

        def Percent(self):
            return self.getToken(HaskellParser.Percent, 0)

        def Ampersand(self):
            return self.getToken(HaskellParser.Ampersand, 0)

        def Asterisk(self):
            return self.getToken(HaskellParser.Asterisk, 0)

        def Plus(self):
            return self.getToken(HaskellParser.Plus, 0)

        def Dot(self):
            return self.getToken(HaskellParser.Dot, 0)

        def Divide(self):
            return self.getToken(HaskellParser.Divide, 0)

        def Less(self):
            return self.getToken(HaskellParser.Less, 0)

        def Eq(self):
            return self.getToken(HaskellParser.Eq, 0)

        def Greater(self):
            return self.getToken(HaskellParser.Greater, 0)

        def QuestionMark(self):
            return self.getToken(HaskellParser.QuestionMark, 0)

        def Atsign(self):
            return self.getToken(HaskellParser.Atsign, 0)

        def ReverseSlash(self):
            return self.getToken(HaskellParser.ReverseSlash, 0)

        def Caret(self):
            return self.getToken(HaskellParser.Caret, 0)

        def Pipe(self):
            return self.getToken(HaskellParser.Pipe, 0)

        def Tilde(self):
            return self.getToken(HaskellParser.Tilde, 0)

        def Colon(self):
            return self.getToken(HaskellParser.Colon, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_ascSymbol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAscSymbol" ):
                listener.enterAscSymbol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAscSymbol" ):
                listener.exitAscSymbol(self)




    def ascSymbol(self):

        localctx = HaskellParser.AscSymbolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 502, self.RULE_ascSymbol)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2938
            _la = self._input.LA(1)
            if not(((((_la - 82)) & ~0x3f) == 0 and ((1 << (_la - 82)) & ((1 << (HaskellParser.Hash - 82)) | (1 << (HaskellParser.Less - 82)) | (1 << (HaskellParser.Greater - 82)) | (1 << (HaskellParser.Ampersand - 82)) | (1 << (HaskellParser.Pipe - 82)) | (1 << (HaskellParser.Bang - 82)) | (1 << (HaskellParser.Caret - 82)) | (1 << (HaskellParser.Plus - 82)) | (1 << (HaskellParser.Asterisk - 82)) | (1 << (HaskellParser.Percent - 82)) | (1 << (HaskellParser.Divide - 82)) | (1 << (HaskellParser.Tilde - 82)) | (1 << (HaskellParser.Atsign - 82)) | (1 << (HaskellParser.Dollar - 82)) | (1 << (HaskellParser.Dot - 82)) | (1 << (HaskellParser.QuestionMark - 82)) | (1 << (HaskellParser.Colon - 82)) | (1 << (HaskellParser.Eq - 82)) | (1 << (HaskellParser.ReverseSlash - 82)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL(self):
            return self.getToken(HaskellParser.DECIMAL, 0)

        def OCTAL(self):
            return self.getToken(HaskellParser.OCTAL, 0)

        def HEXADECIMAL(self):
            return self.getToken(HaskellParser.HEXADECIMAL, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_integer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)




    def integer(self):

        localctx = HaskellParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 504, self.RULE_integer)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2940
            _la = self._input.LA(1)
            if not(((((_la - 137)) & ~0x3f) == 0 and ((1 << (_la - 137)) & ((1 << (HaskellParser.DECIMAL - 137)) | (1 << (HaskellParser.OCTAL - 137)) | (1 << (HaskellParser.HEXADECIMAL - 137)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PfloatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(HaskellParser.FLOAT, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_pfloat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPfloat" ):
                listener.enterPfloat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPfloat" ):
                listener.exitPfloat(self)




    def pfloat(self):

        localctx = HaskellParser.PfloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 506, self.RULE_pfloat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2942
            self.match(HaskellParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PcharContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CHAR(self):
            return self.getToken(HaskellParser.CHAR, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_pchar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPchar" ):
                listener.enterPchar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPchar" ):
                listener.exitPchar(self)




    def pchar(self):

        localctx = HaskellParser.PcharContext(self, self._ctx, self.state)
        self.enterRule(localctx, 508, self.RULE_pchar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2944
            self.match(HaskellParser.CHAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PstringContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(HaskellParser.STRING, 0)

        def getRuleIndex(self):
            return HaskellParser.RULE_pstring

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPstring" ):
                listener.enterPstring(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPstring" ):
                listener.exitPstring(self)




    def pstring(self):

        localctx = HaskellParser.PstringContext(self, self._ctx, self.state)
        self.enterRule(localctx, 510, self.RULE_pstring)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2946
            self.match(HaskellParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





