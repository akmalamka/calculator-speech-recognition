# calculator-speech-recognition

## Step 1. The Task Grammar

command: HParse gram wdnet

## Step 2. The Dictionary

command: HDMan -m -w wlist -n monophones1 -l dlog dict VoxForgeDict.txt

## Step 3. Recording The Data

no command, tinggal record pake audacity, gausah pake HSLab

Pembagian recording ada di prompts
1 - 20 Akmal
21 - 40 - Rickboi
41 - 60 - Fariz
61 - 80 Sena
81 - 100 Hafidh

## Step 4. Creating the Transcription Files

command 1: julia prompts2mlf.jl prompts.txt words.mlf

command 2: HLEd -A -D -T 1 -l '*' -d dict -i phones0.mlf mkphones0.led words.mlf

command 3: HLEd -A -D -T 1 -l '*' -d dict -i phones1.mlf mkphones1.led words.mlf (kyknya ini opsional)

## Step 5. Coding The (Audio) Data

command 1: HCopy -A -D -T 1 -C wav_config -S codetrain.scp

