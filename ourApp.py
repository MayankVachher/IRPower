from flask import *
from collections import Counter

app = Flask(__name__)

@app.route('/')
def render_homepage():
	return render_template("home.html")

@app.route('/result', methods=["POST"])
def goToResult():
	return render_template("result.html", codePrint=genNewCode(request.form['codePrint']))

def genNewCode(code):
	tempList = []
	newToken = ''
	for c in code:
		if c.isalnum() or c == '_':
			newToken += c
		else:
			if newToken != '':
				tempList.append(newToken.strip())
			newToken = ''
	
	if newToken != '':
		tempList.append(newToken.strip())
	
	tokenCount = Counter(tempList)
	print tokenCount
	minVal = min(tokenCount.items(), key=lambda x: x[1])[1]
	maxVal = max(tokenCount.items(), key=lambda x: x[1])[1]
	if minVal!=maxVal:
		for k in tokenCount.keys():
			tokenCount[k] = 5 + (abs(tokenCount[k] - maxVal) * 90)/(maxVal - minVal)
	else:
		for k in tokenCount.keys():
			tokenCount[k] = 95
	print tokenCount
	toRet_start = '<pre>'
	toRet_content = ''
	toRet_end = '</pre>'
	for x in range(0,105,5):
		toRet_content += genCodeThreshold(code, tokenCount, x)
	return toRet_start + toRet_content + toRet_end

def genCodeThreshold(code, threshDict, thresh):
	finalCode_start = '<code id="thresh_'+str(thresh)+'" style="display: none">'
	finalCode_content = ''
	newToken = ''
	for c in code:
		if c.isalnum() or c == '_':
			newToken += c
		else:
			if newToken != '':
				if threshDict[newToken] >= thresh:
					finalCode_content += newToken
			finalCode_content += c
			newToken = ''
	if newToken != '':
		if threshDict[newToken] >= thresh:
			finalCode_content += newToken
	finalCode_end = '</code>'
	return finalCode_start+finalCode_content+finalCode_end


if __name__ == '__main__':
	app.run(debug=True)
