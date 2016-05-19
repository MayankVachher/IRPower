from flask import *
from collections import Counter

app = Flask(__name__)

# @app.route('/surprise', methods=["GET","POST"])
# def hello_world():
# 	t = request.method
# 	resp = ""
# 	if t == "GET":
# 		resp = resp = render_template("home_surprise.html", query='', reco='', hasError='', notFirstTime=None)
# 	else:
# 		user_inp = request.form["user_var"]
# 		user_inp = user_inp.strip()
# 		hasError = not set(user_inp.strip().lower()).issubset(set('abcdefghijklmnopqrstuvwxyz_'))
		
# 		reco_gen = check(user_inp.lower())
# 		hasError = None
# 		resp = render_template("home_surprise.html", query=user_inp, reco=reco_gen, hasError=hasError, notFirstTime=True)
# 	return resp

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
		if c.isalnum() or c == '_' or c == '.':
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
		if c.isalnum() or c == '_' or c == '.':
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
