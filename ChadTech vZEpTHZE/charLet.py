
#### Charlet (pronounced 'Charlotte', and short of the arbitrary 'Character Letter')
#### This is a dictionary whos keys are numbers, with values of the object
#### In hindsight, this likely was not the best way to code this action
#### However, it remains very functional.

charLet={
	
	1:lowercase__a,
	2:lowercase__b,
	3:lowercase__c,
	4:lowercase__d,
	5:lowercase__e,
	6:lowercase__f,
	7:lowercase__g,
	8:lowercase__h,
	9:lowercase__i,
	10:lowercase__j,
	11:lowercase__k,
	12:lowercase__l,
	13:lowercase__m,
	14:lowercase__n,
	15:lowercase__o,
	16:lowercase__p,
	17:lowercase__q,
	18:lowercase__r,
	19:lowercase__s,
	20:lowercase__t,
	21:lowercase__u,
	22:lowercase__v,
	23:lowercase__w,
	24:lowercase__x,
	25:lowercase__y,
	26:lowercase__z,
	27:uppercase__A,
	28:uppercase__B,
	29:uppercase__C,
	30:uppercase__D,
	31:uppercase__E,
	32:uppercase__F,
	33:uppercase__G,
	34:uppercase__H,
	35:uppercase__I,
	36:uppercase__J,
	37:uppercase__K,
	38:uppercase__L,
	39:uppercase__M,
	40:uppercase__N,
	41:uppercase__O,
	42:uppercase__P,
	43:uppercase__Q,
	44:uppercase__R,
	45:uppercase__S,
	46:uppercase__T,
	47:uppercase__U,
	48:uppercase__V,
	49:uppercase__W,
	50:uppercase__X,
	51:uppercase__Y,
	52:uppercase__Z,
	53:space,
	54:punctuation__period,
	55:punctuation__comma,
	56:punctuation__question,
	57:punctuation__semicolon,
	58:punctuation__colon,
	59:punctuation__exclaimation,
	60:punctuation__singlequote,
	61:punctuation__doublequote,
	62:numeral__ze,
	63:numeral__on,
	64:numeral__tw,
	65:numeral__th,
	66:numeral__fo,
	67:numeral__fi,
	68:numeral__si,
	69:numeral__se,
	70:numeral__ei,
	71:numeral__ni,
	72:modallogic__possible,
	73:modallogic__necessary,
	74:firstorderlogic__existential,
	75:firstorderlogic__forall,
	76:firstorderlogic__negation,
	77:firstorderlogic__implication,
	78:firstorderlogic__iff,
	79:firstorderlogic__xor,
	80:firstorderlogic__nand,
	81:firstorderlogic__and,
	82:math__equals,
	83:math__greaterthan,
	84:math__greaterthanorequal,
	85:math__lessthan,
	86:math__lessthanorequal,
	87:math__division,
	88:math__approximately,
	89:math__plus,
	90:math__minus,
	91:math__multiply,
	92:math__forwardslash,
	93:math__backslash,
	94:math__QED,
	95:math__squareroot,
	96:math__plusminus,
	97:math__integral,
	98:math__notequal,
	99:math__angle,
	100:math__triangle,
	101:math__gradient,
	102:math__divides,
	103:math__doesntdivide,
	104:math__infinity,
	105:brackets__leftparentheses,
	106:brackets__rightparentheses,
	107:brackets__leftbracket,
	108:brackets__rightbracket,
	109:brackets__leftcurly,
	110:brackets__rightcurly,
	111:brackets__leftchevron,
	112:brackets__rightchevron,
	113:enter,
	114:misc__numbersign,
	115:misc__dollarsign,
	116:misc__percentsign,
	117:misc__ambersand,
	118:misc__atsign,
	119:misc__carrot,
	120:prooftheory__singleturnstile,
	121:prooftheory__notsingleturnstile,
	122:prooftheory__doubleturnstile,
	123:prooftheory__notdoubleturnstile,
	124:prooftheory__logicalconstant,
	125:settheory__elementof,
	126:settheory__notelementof,
	127:settheory__nullset,
	128:settheory__intersection,
	129:settheory__union,
	130:settheory__superset,
	131:settheory__subset,
	132:settheory__notsuperset,
	133:settheory__notsubset,
	134:error,
	135:slanty__a,
	136:slanty__b,
	137:slanty__c,
	138:slanty__d,
	139:slanty__e,
	140:slanty__f,
	141:slanty__g,
	142:slanty__h,
	143:slanty__i,
	144:slanty__j,
	145:slanty__k,
	146:slanty__l,
	147:slanty__m,
	148:slanty__n,
	149:slanty__o,
	150:slanty__p,
	151:slanty__q,
	152:slanty__r,
	153:slanty__s,
	154:slanty__t,
	155:slanty__u,
	156:slanty__v,
	157:slanty__w,
	158:slanty__x,
	159:slanty__y,
	160:slanty__z,
	### 161 and 162 are codes for the super and sub scripts.
	161:error,
	162:error,
	163:firstorderlogic__altnegation,
	164:hamilton__On,
	165:hamilton__Tw,
	166:hamilton__Th,
	167:hamilton__Fo,
	168:greek_lowercasealpha,
	169:greek_lowercasebeta,
	170:greek_lowercasegamma,
	171:greek_lowercasedelta,
	172:greek_lowercaseepsilon,
	173:greek_lowercasezeta,
	174:greek_lowercaseeta,
	175:greek_lowercasetheta,
	176:greek_lowercaseiota,
	177:greek_lowercasekappa,
	178:greek_lowercaselambda,
	179:greek_lowercasemu,
	180:greek_lowercasenu,
	181:greek_lowercasexi,
	182:greek_lowercaseomicron,
	183:greek_lowercasepi,
	184:greek_lowercaserho,
	185:greek_lowercasesigma,
	186:greek_lowercasetau,
	187:greek_lowercaseupsilon,
	188:greek_lowercasephi,
	189:greek_lowercasechi,
	190:greek_lowercasepsi,
	191:greek_lowercaseomega,
	192:greek_uppercasealpha,
	193:greek_uppercasebeta,
	194:greek_uppercasegamma,
	195:greek_uppercasedelta,
	196:greek_uppercaseepsilon,
	197:greek_uppercasezeta,
	198:greek_uppercaseeta,
	199:greek_uppercasetheta,
	200:greek_uppercaseiota,
	201:greek_uppercasekappa,
	202:greek_uppercaselambda,
	203:greek_uppercasemu,
	204:greek_uppercasenu,
	205:greek_uppercasexi,
	206:greek_uppercaseomicron,
	207:greek_uppercasepi,
	208:greek_uppercaserho,
	209:greek_uppercasesigma,
	210:greek_uppercasetau,
	211:greek_uppercaseupsilon,
	212:greek_uppercasephi,
	213:greek_uppercasechi,
	214:greek_uppercasepsi,
	215:greek_uppercaseomega,
	216:math__arrowon,
	217:math__arrowtw,
	218:misc__asterisk

}