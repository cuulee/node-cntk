{
  "targets": [
  {
    "target_name": "node_cntk_bindings",
    "sources": [
      "src/CNTKModelObjectWrap.h",
      "src/CNTKModelObjectWrap.cc",
      "src/CNTKUtils.h",
      "src/CNTKUtils.cc",
      "src/EvalModelAsyncWorker.cc",
      "src/EvalModelAsyncWorker.h",
      "src/LoadModelAsyncWorker.cc",
      "src/LoadModelAsyncWorker.h",
      "src/node_cntk_bindings.cc",
    ],
    "include_dirs": [ 
      "<!(node -e \"require('nan')\")",
      "cntk/include"
    ],
    "conditions": [
      [ 'OS=="win"', {
        "libraries" : [
          "-l../cntk/lib/$(Platform)/$(Configuration)/Cntk.Core-2.0.lib"
        ],
        'msvs_settings': {
        'VCCLCompilerTool': {
            'AdditionalOptions': [ '/EHsc'] 
        }}
      }]
    ]
  }]
}