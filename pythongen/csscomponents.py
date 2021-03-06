def defaultcomponents():
    default = "/*default*/tag{color: #f7f7f7; background-color: #333; border: 1px solid transparent; font-size: 1rem; padding: 0rem 0.4rem 0.25rem 0.4rem; /*top right bottom left*/ position: relative;}/*sizes*/.tag-rounded{border: 1px solid transparent; border-radius: 0.9rem;}.tag-small{font-size: 0.6rem; padding: 0rem 0.24rem 0.15rem 0.24rem;}.tag-large{font-size: 1.5rem; padding: 0rem 0.6rem 0.375rem 0.6rem;}.tag-xl{font-size: 2rem; padding: 0rem 0.8rem 0.5rem 0.8rem;}.tag-small.tag-rounded{font-size: 0.6rem; padding: 0rem 0.24rem 0.15rem 0.24rem; border-radius: 0.54rem;}.tag-large.tag-rounded{font-size: 1.5rem; padding: 0rem 0.6rem 0.375rem 0.6rem; border-radius: 1.35rem;}.tag-xl.tag-rounded{font-size: 2rem; padding: 0rem 0.8rem 0.5rem 0.8rem; border-radius: 1.8rem;}.col-sm{border: 1px solid #F66079; margin: 0.2rem; border-radius: 2rem;}"
    return default

def normalclass(tagname,color):
    tag = tagname + "{background:" + color + ";color:white;border-color:"+color+";}"
    return tag

def hollowclass(tagname,color):
    tag = tagname + "{background:transparent;color:" + color + ";border:1px solid " + color + ";}"
    return tag