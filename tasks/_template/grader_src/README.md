# Grader source (white-box probe only)

Put the grader's scoring code and config here. It is shown READ-ONLY to the white-box exploit probe.
Hidden test data and secret seeds go under a path matched by `grader.secret_globs` (e.g. grader_src/hidden/)
and are listed in task.yaml `hidden_data`; they are withheld from the white-box copy and from every other stage.
