from inference import InferencePipeline
from inference.core.interfaces.stream.sinks import render_boxes

pipeline = InferencePipeline.init(
    model_id="wpn_pintol_di_kita/1", 
    video_reference='./test.mp4', 
    on_prediction=render_boxes, 
)
pipeline.start()
pipeline.join()
