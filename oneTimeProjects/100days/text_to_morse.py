import sys
import getopt

seps = " "
morse_alps = {
	"a":"...","b":"-...","c":"-.-.","d":"-..","e":".",
	"f":"..-.","g":"--.","h":"....","i":"..","j":".---",
	"k":"-.-","l":".-..","m":"--","n":"-.","o":"---",
	"p":".--.","q":"--.-","r":".-.","s":"...","t":"-",
	"u":"..-","v":"...-","w":".--","x":"-..-",
	"y":"-.--","z":"--.."
}

def usage():
    print("Text to Morse")
    print("Usage: python text_to_morse.py -t text")
    print("Usage: python text_to_morse.py -t text -s separator{default ' '}")

def main():
	try:
		opts, args = getopt.getopt(sys.argv[1:], 'h:t', ["help", "text="])
		print(opts,args)
	except Exception as e:
		raise e
	else:
		for o,a in opts:
			if o in ("-h", "--help"):
				usage()
			elif o in ("-t", "--text"):
				text = ""
				for char in a.lower():
					if char in morse_alps.keys():
						text = text + morse_alps[char] + seps
				print(f"Your Morse Code:\n{text}")


if __name__ == '__main__':
	main()