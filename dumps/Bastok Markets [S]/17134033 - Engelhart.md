# 17134033 - Engelhart

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | Bastok Markets [S] (ID: 87) |
| Block Size       | 584 bytes                   |
| Total Events     | 20                          |
| References Count | 25                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [104](#event-104)        | 0x0001       |     29 |              7 |
| [116](#event-116)        | 0x001E       |      1 |              1 |
| [117](#event-117)        | 0x001F       |     29 |              7 |
| [163](#event-163)        | 0x003C       |     34 |              8 |
| [118](#event-118)        | 0x005E       |      1 |              1 |
| [119](#event-119)        | 0x005F       |     29 |              7 |
| [120](#event-120)        | 0x007C       |      1 |              1 |
| [121](#event-121)        | 0x007D       |     29 |              7 |
| [124](#event-124)        | 0x009A       |      1 |              1 |
| [125](#event-125)        | 0x009B       |     29 |              7 |
| [126](#event-126)        | 0x00B8       |      1 |              1 |
| [127](#event-127)        | 0x00B9       |     29 |              7 |
| [164](#event-164)        | 0x00D6       |      1 |              1 |
| [165](#event-165)        | 0x00D7       |     29 |              7 |
| [18](#event-18)          | 0x00F4       |     33 |              9 |
| [32](#event-32)          | 0x0115       |      1 |              1 |
| [65535.1](#event-655351) | 0x0116       |     52 |             12 |
| [33](#event-33)          | 0x014A       |     29 |              7 |
| [36](#event-36)          | 0x0167       |     29 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0000      |           0 |
|       2 | 0x2E7C      |       11900 |
|       3 | 0x2E7B      |       11899 |
|       4 | 0x0397      |         919 |
|       5 | 0x2E7D      |       11901 |
|       6 | 0x2E8B      |       11915 |
|       7 | 0x2E9F      |       11935 |
|       8 | 0x2EAD      |       11949 |
|       9 | 0x2EB2      |       11954 |
|      10 | 0x2EE4      |       12004 |
|      11 | 0x30EA      |       12522 |
|      12 | 0x30EB      |       12523 |
|      13 | 0x0028      |          40 |
|      14 | 0xFFFF135F  |  4294906719 |
|      15 | 0xFFFE0218  |  4294836760 |
|      16 | 0xFFFFF060  |  4294963296 |
|      17 | 0xFFFF14BC  |  4294907068 |
|      18 | 0xFFFDF994  |  4294834580 |
|      19 | 0xFFFF1345  |  4294906693 |
|      20 | 0xFFFDED94  |  4294831508 |
|      21 | 0xFFFF0D7D  |  4294905213 |
|      22 | 0xFFFDE7A8  |  4294829992 |
|      23 | 0x3176      |       12662 |
|      24 | 0x317E      |       12670 |

## String References

- **11899**: The client is expecting you at the waterfall in North Gustaberg. Do not keep him waiting.
- **11900**: The people of Bastok live under a cloud of uncertainty. It's times like this that music can lift the weary spirit, don't you agree?
- **11901**: You have met with Senator Werner? Then you have your instructions: bring the $3 here to me.
- **11915**: A chance meeting has landed you right in the thick of things, my friend. I have a feeling we'll be getting to know each other very well indeed.
- **11935**: There are rumors that the Galkan elder Werei and his friend Gumbah are hoarding a stockpile of weapons. Go, and discover the truth behind their motives.
- **11949**: Head to Grauberg and see if you can confirm my suspicions about the stockpile of weapons.
- **11954**: I hope the senator was unharmed...
- **12004**: With the senator gone, I doubt I'll have any more tasks for you. Thank you for your competent, albeit brief, service.
- **12522**: The president has released a statement regarding Senator Werner's assassination.
- **12523**: It contained a message to the assassin: "You will not elude the grip of the Mythril Musketeers!"
- **12662**: Wh-what is it, <Player>? I'm a little occupied right now...
- **12670**: The Mythril Musketeers hauled me in for questioning. You didn't have anything to do with that, did you?

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 104

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1C 00  80 66 01 80 D1 71 05 01   ........f...q..
0010: D1 71 05 01 74 6C 6B 30  1D 02 80 23 21 00        .q..tlk0...#!.  
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1C] WAIT(30* ticks)
  2: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Engelhart (ID: 17134033/0x010571D1), Engelhart (ID: 17134033/0x010571D1)], work=0*
  3: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=11900*)
    → "The people of Bastok live under a cloud of uncertainty. It's times like this that music can lift the weary spirit, don't you agree?"
  4: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001C [0x21] END_EVENT
  6: 0x001D [0x00] END_REQSTACK()
```

### Event 116

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            00                   . 
```

#### Opcodes

```
  0: 0x001E [0x00] END_REQSTACK()
```

### Event 117

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               1E                 .
0020: F0 FF FF 7F 1C 00 80 66  01 80 D1 71 05 01 D1 71  .......f...q...q
0030: 05 01 74 6C 6B 30 1D 03  80 23 21 00              ..tlk0...#!.    
```

#### Opcodes

```
  0: 0x001F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0024 [0x1C] WAIT(30* ticks)
  2: 0x0027 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Engelhart (ID: 17134033/0x010571D1), Engelhart (ID: 17134033/0x010571D1)], work=0*
  3: 0x0036 [0x1D] PRINT_EVENT_MESSAGE(message_id=11899*)
    → "The client is expecting you at the waterfall in North Gustaberg. Do not keep him waiting."
  4: 0x0039 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x003A [0x21] END_EVENT
  6: 0x003B [0x00] END_REQSTACK()
```

### Event 163

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 34 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      1E F0 FF FF              ....
0040: 7F 1C 00 80 66 01 80 D1  71 05 01 D1 71 05 01 74  ....f...q...q..t
0050: 6C 6B 30 03 02 10 04 80  1D 05 80 23 21 00        lk0........#!.  
```

#### Opcodes

```
  0: 0x003C [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0041 [0x1C] WAIT(30* ticks)
  2: 0x0044 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Engelhart (ID: 17134033/0x010571D1), Engelhart (ID: 17134033/0x010571D1)], work=0*
  3: 0x0053 [0x03] Work_Zone[2] = 919*
  4: 0x0058 [0x1D] PRINT_EVENT_MESSAGE(message_id=11901*)
    → "You have met with Senator Werner? Then you have your instructions: bring the $3 here to me."
  5: 0x005B [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x005C [0x21] END_EVENT
  7: 0x005D [0x00] END_REQSTACK()
```

### Event 118

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x005E  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            00                   . 
```

#### Opcodes

```
  0: 0x005E [0x00] END_REQSTACK()
```

### Event 119

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005F   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                               1E                 .
0060: F0 FF FF 7F 1C 00 80 66  01 80 D1 71 05 01 D1 71  .......f...q...q
0070: 05 01 74 6C 6B 30 1D 06  80 23 21 00              ..tlk0...#!.    
```

#### Opcodes

```
  0: 0x005F [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0064 [0x1C] WAIT(30* ticks)
  2: 0x0067 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Engelhart (ID: 17134033/0x010571D1), Engelhart (ID: 17134033/0x010571D1)], work=0*
  3: 0x0076 [0x1D] PRINT_EVENT_MESSAGE(message_id=11915*)
    → "A chance meeting has landed you right in the thick of things, my friend. I have a feeling we'll be getting to know each other very well indeed."
  4: 0x0079 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x007A [0x21] END_EVENT
  6: 0x007B [0x00] END_REQSTACK()
```

### Event 120

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x007C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                      00                       .   
```

#### Opcodes

```
  0: 0x007C [0x00] END_REQSTACK()
```

### Event 121

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007D   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                         1E F0 FF               ...
0080: FF 7F 1C 00 80 66 01 80  D1 71 05 01 D1 71 05 01  .....f...q...q..
0090: 74 6C 6B 30 1D 07 80 23  21 00                    tlk0...#!.      
```

#### Opcodes

```
  0: 0x007D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0082 [0x1C] WAIT(30* ticks)
  2: 0x0085 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Engelhart (ID: 17134033/0x010571D1), Engelhart (ID: 17134033/0x010571D1)], work=0*
  3: 0x0094 [0x1D] PRINT_EVENT_MESSAGE(message_id=11935*)
    → "There are rumors that the Galkan elder Werei and his friend Gumbah are hoarding a stockpile of weapons. Go, and discover the truth behind their motives."
  4: 0x0097 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0098 [0x21] END_EVENT
  6: 0x0099 [0x00] END_REQSTACK()
```

### Event 124

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009A  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                00                           .     
```

#### Opcodes

```
  0: 0x009A [0x00] END_REQSTACK()
```

### Event 125

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009B   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                   1E F0 FF FF 7F             .....
00A0: 1C 00 80 66 01 80 D1 71  05 01 D1 71 05 01 74 6C  ...f...q...q..tl
00B0: 6B 30 1D 08 80 23 21 00                           k0...#!.        
```

#### Opcodes

```
  0: 0x009B [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00A0 [0x1C] WAIT(30* ticks)
  2: 0x00A3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Engelhart (ID: 17134033/0x010571D1), Engelhart (ID: 17134033/0x010571D1)], work=0*
  3: 0x00B2 [0x1D] PRINT_EVENT_MESSAGE(message_id=11949*)
    → "Head to Grauberg and see if you can confirm my suspicions about the stockpile of weapons."
  4: 0x00B5 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00B6 [0x21] END_EVENT
  6: 0x00B7 [0x00] END_REQSTACK()
```

### Event 126

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B8  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                          00                               .       
```

#### Opcodes

```
  0: 0x00B8 [0x00] END_REQSTACK()
```

### Event 127

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B9   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                             1E F0 FF FF 7F 1C 00           .......
00C0: 80 66 01 80 D1 71 05 01  D1 71 05 01 74 6C 6B 30  .f...q...q..tlk0
00D0: 1D 09 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x00B9 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00BE [0x1C] WAIT(30* ticks)
  2: 0x00C1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Engelhart (ID: 17134033/0x010571D1), Engelhart (ID: 17134033/0x010571D1)], work=0*
  3: 0x00D0 [0x1D] PRINT_EVENT_MESSAGE(message_id=11954*)
    → "I hope the senator was unharmed..."
  4: 0x00D3 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00D4 [0x21] END_EVENT
  6: 0x00D5 [0x00] END_REQSTACK()
```

### Event 164

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00D6  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                   00                                    .         
```

#### Opcodes

```
  0: 0x00D6 [0x00] END_REQSTACK()
```

### Event 165

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D7   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                      1E  F0 FF FF 7F 1C 00 80 66         ........f
00E0: 01 80 D1 71 05 01 D1 71  05 01 74 6C 6B 30 1D 0A  ...q...q..tlk0..
00F0: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x00D7 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00DC [0x1C] WAIT(30* ticks)
  2: 0x00DF [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Engelhart (ID: 17134033/0x010571D1), Engelhart (ID: 17134033/0x010571D1)], work=0*
  3: 0x00EE [0x1D] PRINT_EVENT_MESSAGE(message_id=12004*)
    → "With the senator gone, I doubt I'll have any more tasks for you. Thank you for your competent, albeit brief, service."
  4: 0x00F1 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00F2 [0x21] END_EVENT
  6: 0x00F3 [0x00] END_REQSTACK()
```

### Event 18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00F4   |
| Data Size    | 33 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00F0:             1E F0 FF FF  7F 1C 00 80 66 01 80 D1      ........f...
0100: 71 05 01 D1 71 05 01 74  6C 6B 30 1D 0B 80 23 1D  q...q..tlk0...#.
0110: 0C 80 23 21 00                                    ..#!.           
```

#### Opcodes

```
  0: 0x00F4 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00F9 [0x1C] WAIT(30* ticks)
  2: 0x00FC [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Engelhart (ID: 17134033/0x010571D1), Engelhart (ID: 17134033/0x010571D1)], work=0*
  3: 0x010B [0x1D] PRINT_EVENT_MESSAGE(message_id=12522*)
    → "The president has released a statement regarding Senator Werner's assassination."
  4: 0x010E [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x010F [0x1D] PRINT_EVENT_MESSAGE(message_id=12523*)
    → "It contained a message to the assassin: "You will not elude the grip of the Mythril Musketeers!""
  6: 0x0112 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0113 [0x21] END_EVENT
  8: 0x0114 [0x00] END_REQSTACK()
```

### Event 32

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0115  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                00                                      .          
```

#### Opcodes

```
  0: 0x0115 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0116   |
| Data Size    | 52 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0110:                   32 0D  80 1F 00 0E 80 0F 80 10        2.........
0120: 80 1F 01 1F 00 11 80 12  80 10 80 1F 01 1F 00 13  ................
0130: 80 14 80 10 80 1F 01 1F  00 15 80 16 80 10 80 1F  ................
0140: 01 1E 43 72 05 01 1C 00  80 00                    ..Cr......      
```

#### Opcodes

```
  0: 0x0116 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0119 [0x1F] MOVE_ENTITY: EventEntity moves to X=-60.577*, Z=-130.536*, Y=-4.000*
  2: 0x0121 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0123 [0x1F] MOVE_ENTITY: EventEntity moves to X=-60.228*, Z=-132.716*, Y=-4.000*
  4: 0x012B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x012D [0x1F] MOVE_ENTITY: EventEntity moves to X=-60.603*, Z=-135.788*, Y=-4.000*
  6: 0x0135 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0137 [0x1F] MOVE_ENTITY: EventEntity moves to X=-62.083*, Z=-137.304*, Y=-4.000*
  8: 0x013F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x0141 [0x1E] EventEntity looks at Ernestine (ID: 17134147/0x01057243) and starts talking
 10: 0x0146 [0x1C] WAIT(30* ticks)
 11: 0x0149 [0x00] END_REQSTACK()
```

### Event 33

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014A   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                1E F0 FF FF 7F 1C            ......
0150: 00 80 66 01 80 D1 71 05  01 D1 71 05 01 74 6C 6B  ..f...q...q..tlk
0160: 30 1D 17 80 23 21 00                              0...#!.         
```

#### Opcodes

```
  0: 0x014A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x014F [0x1C] WAIT(30* ticks)
  2: 0x0152 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Engelhart (ID: 17134033/0x010571D1), Engelhart (ID: 17134033/0x010571D1)], work=0*
  3: 0x0161 [0x1D] PRINT_EVENT_MESSAGE(message_id=12662*)
    → "Wh-what is it, <Player>? I'm a little occupied right now..."
  4: 0x0164 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0165 [0x21] END_EVENT
  6: 0x0166 [0x00] END_REQSTACK()
```

### Event 36

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0167   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0160:                      1E  F0 FF FF 7F 1C 00 80 66         ........f
0170: 01 80 D1 71 05 01 D1 71  05 01 74 6C 6B 30 1D 18  ...q...q..tlk0..
0180: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0167 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x016C [0x1C] WAIT(30* ticks)
  2: 0x016F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Engelhart (ID: 17134033/0x010571D1), Engelhart (ID: 17134033/0x010571D1)], work=0*
  3: 0x017E [0x1D] PRINT_EVENT_MESSAGE(message_id=12670*)
    → "The Mythril Musketeers hauled me in for questioning. You didn't have anything to do with that, did you?"
  4: 0x0181 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0182 [0x21] END_EVENT
  6: 0x0183 [0x00] END_REQSTACK()
```
