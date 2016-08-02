<script type="text/javascript">
 MATHML_FEATURE = "org.w3c.dom.mathml"     //as per w3c specification
    MATHML_FEATURE_VERSION = "3.0"            //Any version number appears to work
    //Opps Chrome not natively supported yet
    var head = document.getElementsByTagName('head')[0];
var js = document.createElement("script");
js.async = true;
js.type = "text/javascript"
    if(document.implementation.hasFeature(MATHML_FEATURE, MATHML_FEATURE_VERSION ))
{}
    else
{
function () {
  var script = document.createElement("script");
  script.type = "text/javascript";
  script.src  = "http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML";
  document.getElementsByTagName("head")[0].appendChild(script);
}();
}
</script>
