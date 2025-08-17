# 17449518 - Fondactiont

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Garlaige Citadel [S] (ID: 164) |
| Block Size       | 316 bytes                      |
| Total Events     | 6                              |
| References Count | 14                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [25](#event-25)       | 0x0001       |     15 |              7 |
| [26](#event-26)       | 0x0010       |     62 |             18 |
| [27](#event-27)       | 0x004E       |     15 |              7 |
| [28](#event-28)       | 0x005D       |    115 |             19 |
| [29](#event-29)       | 0x00D0       |     11 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1E10      |        7696 |
|       1 | 0x1E11      |        7697 |
|       2 | 0x0014      |          20 |
|       3 | 0x1E12      |        7698 |
|       4 | 0x1E13      |        7699 |
|       5 | 0x1E14      |        7700 |
|       6 | 0x1E15      |        7701 |
|       7 | 0x03C9      |         969 |
|       8 | 0x1E16      |        7702 |
|       9 | 0x1E17      |        7703 |
|      10 | 0x1E18      |        7704 |
|      11 | 0x00C9      |         201 |
|      12 | 0x0000      |           0 |
|      13 | 0x1E19      |        7705 |

## String References

- **7696**: I am a friar from the San d'Orian Cathedral.
- **7697**: I was journeying on my pilgrimage when I inadvertently wandered into the front line of the beasthorde offensive. Fortunately, the Royal Knights discovered me first, and took me into their custody. Even though I am thankful, I wish the knights would grant me leave to continue my journey.
- **7698**: Would you perhaps be a soldier of the Allied Forces? I am in desperate need of your assistance. I beg you, please hear me out.
- **7699**: It is a rather embarrassing story... When I was attacked by monsters in Grauberg, in my blind panic I threw whatever was on hand in an attempt to drive away the beasts. It was too late when I realized I had hurled a package of great import, entrusted to me from the Cathedral, straight into the river. I would have retrieved it myself, but I was...uh...distracted.
- **7700**: If you were to chance upon an ornate package while traveling through Grauberg, could you please bring it back to me?
- **7701**: I pray that it has not been washed downstream. I would be indebted if you could locate the package...and not spread the tale of my "exploits."
- **7702**: Why, be that not the $3? That is indeed the item I hurled--I mean, dropped!
- **7703**: I thank you from the bottom of my heart. The package contains tools such as paint, to be used to repair the Goddess's image should she be damaged during the course of the war.
- **7704**: This is not much, but please accept it. This white magic will allow the user to teleport straight to the battlefield within the blink of an eye.
- **7705**: It pains me to wonder what may have become of the cathedral... O merciful Altana! Please grant us your divine protection!

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

### Event 25

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 1D 00  80 23 1D 01 80 23 21 00   ........#...#!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x1D] PRINT_EVENT_MESSAGE(message_id=7696*)
    → "I am a friar from the San d'Orian Cathedral."
  2: 0x0009 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000A [0x1D] PRINT_EVENT_MESSAGE(message_id=7697*)
    → "I was journeying on my pilgrimage when I inadvertently wandered into the front line of the beasthorde offensive. Fortunately, the Royal Knights discovered me first, and took me into their custody. Even though I am thankful, I wish the knights would grant me leave to continue my journey."
  4: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000E [0x21] END_EVENT
  6: 0x000F [0x00] END_REQSTACK()
```

### Event 26

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 62 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 42 1E F0 FF FF 7F 1D 00  80 23 1D 01 80 23 5B 02  B........#...#[.
0020: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 1D 03 80  .........tlk0...
0030: 23 1D 04 80 23 1D 05 80  23 1D 06 80 23 5B 02 80  #...#...#...#[..
0040: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 21 00        ........tlk1!.  
```

#### Opcodes

```
  0: 0x0010 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0011 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0016 [0x1D] PRINT_EVENT_MESSAGE(message_id=7696*)
    → "I am a friar from the San d'Orian Cathedral."
  3: 0x0019 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x001A [0x1D] PRINT_EVENT_MESSAGE(message_id=7697*)
    → "I was journeying on my pilgrimage when I inadvertently wandered into the front line of the beasthorde offensive. Fortunately, the Royal Knights discovered me first, and took me into their custody. Even though I am thankful, I wish the knights would grant me leave to continue my journey."
  5: 0x001D [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001E [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  7: 0x002D [0x1D] PRINT_EVENT_MESSAGE(message_id=7698*)
    → "Would you perhaps be a soldier of the Allied Forces? I am in desperate need of your assistance. I beg you, please hear me out."
  8: 0x0030 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0031 [0x1D] PRINT_EVENT_MESSAGE(message_id=7699*)
    → "It is a rather embarrassing story... When I was attacked by monsters in Grauberg, in my blind panic I threw whatever was on hand in an attempt to drive away the beasts. It was too late when I realized I had hurled a package of great import, entrusted to me from the Cathedral, straight into the river. I would have retrieved it myself, but I was...uh...distracted."
 10: 0x0034 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0035 [0x1D] PRINT_EVENT_MESSAGE(message_id=7700*)
    → "If you were to chance upon an ornate package while traveling through Grauberg, could you please bring it back to me?"
 12: 0x0038 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0039 [0x1D] PRINT_EVENT_MESSAGE(message_id=7701*)
    → "I pray that it has not been washed downstream. I would be indebted if you could locate the package...and not spread the tale of my "exploits.""
 14: 0x003C [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x003D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
 16: 0x004C [0x21] END_EVENT
 17: 0x004D [0x00] END_REQSTACK()
```

### Event 27

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004E   |
| Data Size    | 15 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                            1E F0                ..
0050: FF FF 7F 1D 05 80 23 1D  06 80 23 21 00           ......#...#!.   
```

#### Opcodes

```
  0: 0x004E [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0053 [0x1D] PRINT_EVENT_MESSAGE(message_id=7700*)
    → "If you were to chance upon an ornate package while traveling through Grauberg, could you please bring it back to me?"
  2: 0x0056 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0057 [0x1D] PRINT_EVENT_MESSAGE(message_id=7701*)
    → "I pray that it has not been washed downstream. I would be indebted if you could locate the package...and not spread the tale of my "exploits.""
  4: 0x005A [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x005B [0x21] END_EVENT
  6: 0x005C [0x00] END_REQSTACK()
```

### Event 28

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x005D    |
| Data Size    | 115 bytes |
| Instructions | 19        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                         42 1E F0               B..
0060: FF FF 7F 6F 70 5B 02 80  F8 FF FF 7F F8 FF FF 7F  ...op[..........
0070: 74 6C 6B 30 03 02 10 07  80 1D 08 80 23 5B 02 80  tlk0........#[..
0080: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 1D 09 80 23  ........tlk1...#
0090: 53 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 31 5B 02 80  S........tlk1[..
00A0: F8 FF FF 7F F8 FF FF 7F  70 61 73 30 1D 0A 80 23  ........pas0...#
00B0: 53 F8 FF FF 7F F8 FF FF  7F 70 61 73 30 45 0B 80  S........pas0E..
00C0: F8 FF FF 7F F8 FF FF 7F  71 73 74 63 0C 80 21 00  ........qstc..!.
```

#### Opcodes

```
  0: 0x005D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x005E [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0063 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0064 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0065 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  5: 0x0074 [0x03] Work_Zone[2] = 969*
  6: 0x0079 [0x1D] PRINT_EVENT_MESSAGE(message_id=7702*)
    → "Why, be that not the $3? That is indeed the item I hurled--I mean, dropped!"
  7: 0x007C [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x007D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
  9: 0x008C [0x1D] PRINT_EVENT_MESSAGE(message_id=7703*)
    → "I thank you from the bottom of my heart. The package contains tools such as paint, to be used to repair the Goddess's image should she be damaged during the course of the war."
 10: 0x008F [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0090 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
 12: 0x009D [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=20*
 13: 0x00AC [0x1D] PRINT_EVENT_MESSAGE(message_id=7704*)
    → "This is not much, but please accept it. This white magic will allow the user to teleport straight to the battlefield within the blink of an eye."
 14: 0x00AF [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x00B0 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
 16: 0x00BD [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [EventEntity, EventEntity], work=[201*, 0*]
 17: 0x00CE [0x21] END_EVENT
 18: 0x00CF [0x00] END_REQSTACK()
```

### Event 29

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00D0   |
| Data Size    | 11 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0: 1E F0 FF FF 7F 1D 0D 80  23 21 00                 ........#!.     
```

#### Opcodes

```
  0: 0x00D0 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00D5 [0x1D] PRINT_EVENT_MESSAGE(message_id=7705*)
    → "It pains me to wonder what may have become of the cathedral... O merciful Altana! Please grant us your divine protection!"
  2: 0x00D8 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x00D9 [0x21] END_EVENT
  4: 0x00DA [0x00] END_REQSTACK()
```
