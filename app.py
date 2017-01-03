from flask import Flask, jsonify
from flask import render_template


app = Flask(__name__)


@app.route("/")
def index():
	#navigation = [{"caption" : "Home"}, {"caption" : "Resumes"}]
	blurb = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas libero leo, finibus vel orci posuere, eleifend varius risus. Nam maximus metus eget velit feugiat, sit amet bibendum felis porta. Etiam eleifend luctus porttitor. Nam dapibus nunc nunc, ut imperdiet lacus efficitur hendrerit. Nulla facilisi. Sed pellentesque metus ligula, a laoreet mauris interdum eu. Integer iaculis dignissim neque in iaculis. Etiam varius est non lacus rhoncus tempor in ut ligula. Donec tincidunt dapibus odio, blandit scelerisque lacus. Nullam vel accumsan risus. Nulla facilisi. Aliquam fermentum, leo a lobortis interdum, neque erat rhoncus sapien, sit amet auctor nulla velit at erat. Praesent quis ornare purus. Fusce semper mollis neque a eleifend. Phasellus blandit dui eget leo ultrices, nec consectetur ipsum posuere. Nulla eros ipsum, vulputate sed dui at, pharetra commodo lacus. Integer ipsum ante, convallis vitae interdum in, fermentum at tellus. Vivamus varius justo dolor, sed dictum magna condimentum vitae. In molestie faucibus pellentesque. Integer odio massa, cursus nec augue vel, bibendum sollicitudin nisl. Duis gravida, lacus et lacinia consectetur, velit ante vehicula nisl, sed auctor nulla ipsum quis felis. Sed ultricies eget velit luctus pretium. Vivamus pretium rhoncus convallis. asellus id ex id metus posuere lacinia ac vel turpis. Praesent ligula dui, eleifend quis scelerisque in, elementum sed eros. Duis rutrum convallis tellus, eu malesuada augue vehicula eget. Fusce hendrerit tempor imperdiet. Ut suscipit erat eget turpis rutrum, vitae fermentum lorem sagittis. Proin justo orci, varius nec diam eget, dapibus dictum orci. Phasellus finibus finibus feugiat. Aliquam sit amet gravida mauris. Cras vulputate eros vel libero commodo sagittis. Vivamus pretium justo egestas diam fringilla, ac cursus nisi accumsan. Donec efficitur, sem sit amet tristique facilisis, mi mi scelerisque lacus, vitae laoreet erat mi sed dolor. Pellentesque dapibus nisl nisi, et vestibulum arcu pellentesque sit amet. Praesent vel volutpat turpis, a consequat purus. Sed aliquam arcu vel gravida blandit. Curabitur at velit sit amet leo luctus venenatis. Cras malesuada nibh quis risus pretium consectetur. Nam sollicitudin luctus dui, non condimentum justo ornare nec. Ut cursus odio vel feugiat elementum. Integer et turpis eros. Pellentesque porttitor gravida lorem nec porta. In hac habitasse platea dictumst. Nulla aliquam eros in est mattis accumsan. Vestibulum eget turpis sem. Aenean laoreet libero accumsan nunc fermentum egestas id vel libero. "
	return render_template("Index.html", blurb=blurb)



if __name__=="__main__":
	app.run(debug=True)