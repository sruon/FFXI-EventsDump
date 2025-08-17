# 17846804 - Gurren-Murren

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Ceizak Battlegrounds (ID: 261) |
| Block Size       | 312 bytes                      |
| Total Events     | 6                              |
| References Count | 12                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [2500](#event-2500)   | 0x0001       |     64 |             20 |
| [2501](#event-2501)   | 0x0041       |     44 |             10 |
| [2503](#event-2503)   | 0x006D       |     69 |             15 |
| [2507](#event-2507)   | 0x00B2       |     44 |             10 |
| [23](#event-23)       | 0x00DE       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x1D49      |        7497 |
|       2 | 0x1D4A      |        7498 |
|       3 | 0x1D4B      |        7499 |
|       4 | 0x1D4C      |        7500 |
|       5 | 0x1D4D      |        7501 |
|       6 | 0x1D4E      |        7502 |
|       7 | 0x1D4F      |        7503 |
|       8 | 0x1D50      |        7504 |
|       9 | 0x1D51      |        7505 |
|      10 | 0x00C9      |         201 |
|      11 | 0x0000      |           0 |

## String References

- **7497**: Have you ever seen a twitherym? They're creatarus with exquisite wings made of pure beauty, and they live deep within the jungles.
- **7498**: Stories abound of the magic contained in the dustaru their wings leave behind. Fathom that! So...I got to thinking. Maybe-waybe we can use that magic to help the colonization effort!
- **7499**: But every rose has its thorns. Not even experienced pioneers have laid so much as a finger-winger on them.
- **7500**: Yet there may be another way! They imbibe the sap from local trees, gaining nourishmentaru from the vitamins and minerals within. When they dance around the trees, their wings flutter and deposit trace amounts of dusty-wust on the sap, which then runs down the trunks and limbs.
- **7501**: That's where you come in, [Mister/Missus] Pioneer. Can you find some of this sap and deliver-wiver it to me? Think of the research! Think of the possibilities!
- **7502**: The butterflies nest to the south of here, where the most succulentaru trees reside. Take a gander and see if you can't locate any sap!
- **7503**: Stupendous-wendous! The sap you've brought back contains more dust than I could have hoped for!
- **7504**: So much progress in so little time! This sends my research forward by monthy-wonths! Only a tad longer and I'll be able to concoctaru something that'll knock the pioneering world flat on its backside!
- **7505**: Until then, I presentaru you with a token of my esteem.

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

### Event 2500

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 64 bytes |
| Instructions | 20       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 1E F0 FF FF 7F 6F  70 66 00 80 F8 FF FF 7F   B.....opf......
0010: F8 FF FF 7F 74 6C 6B 30  1D 01 80 23 1D 02 80 23  ....tlk0...#...#
0020: 1D 03 80 23 1D 04 80 23  1D 05 80 23 1D 06 80 23  ...#...#...#...#
0030: 66 00 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 31 21  f..........tlk1!
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0007 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0008 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0009 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  5: 0x0018 [0x1D] PRINT_EVENT_MESSAGE(message_id=7497*)
    → "Have you ever seen a twitherym? They're creatarus with exquisite wings made of pure beauty, and they live deep within the jungles."
  6: 0x001B [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x001C [0x1D] PRINT_EVENT_MESSAGE(message_id=7498*)
    → "Stories abound of the magic contained in the dustaru their wings leave behind. Fathom that! So...I got to thinking. Maybe-waybe we can use that magic to help the colonization effort!"
  8: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0020 [0x1D] PRINT_EVENT_MESSAGE(message_id=7499*)
    → "But every rose has its thorns. Not even experienced pioneers have laid so much as a finger-winger on them."
 10: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=7500*)
    → "Yet there may be another way! They imbibe the sap from local trees, gaining nourishmentaru from the vitamins and minerals within. When they dance around the trees, their wings flutter and deposit trace amounts of dusty-wust on the sap, which then runs down the trunks and limbs."
 12: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x0028 [0x1D] PRINT_EVENT_MESSAGE(message_id=7501*)
    → "That's where you come in, [Mister/Missus] Pioneer. Can you find some of this sap and deliver-wiver it to me? Think of the research! Think of the possibilities!"
 14: 0x002B [0x23] WAIT_FOR_DIALOG_INTERACTION
 15: 0x002C [0x1D] PRINT_EVENT_MESSAGE(message_id=7502*)
    → "The butterflies nest to the south of here, where the most succulentaru trees reside. Take a gander and see if you can't locate any sap!"
 16: 0x002F [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x0030 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
 18: 0x003F [0x21] END_EVENT
 19: 0x0040 [0x00] END_REQSTACK()
```

### Event 2501

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0041   |
| Data Size    | 44 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:    42 1E F0 FF FF 7F 6F  70 66 00 80 F8 FF FF 7F   B.....opf......
0050: F8 FF FF 7F 74 6C 6B 30  1D 06 80 23 66 00 80 F8  ....tlk0...#f...
0060: FF FF 7F F8 FF FF 7F 74  6C 6B 31 21 00           .......tlk1!.   
```

#### Opcodes

```
  0: 0x0041 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0042 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0047 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0048 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0049 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  5: 0x0058 [0x1D] PRINT_EVENT_MESSAGE(message_id=7502*)
    → "The butterflies nest to the south of here, where the most succulentaru trees reside. Take a gander and see if you can't locate any sap!"
  6: 0x005B [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x005C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
  8: 0x006B [0x21] END_EVENT
  9: 0x006C [0x00] END_REQSTACK()
```

### Event 2503

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006D   |
| Data Size    | 69 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         42 1E F0               B..
0070: FF FF 7F 6F 70 66 00 80  F8 FF FF 7F F8 FF FF 7F  ...opf..........
0080: 74 6C 6B 30 1D 07 80 23  1D 08 80 23 1D 09 80 23  tlk0...#...#...#
0090: 66 00 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 31 45  f..........tlk1E
00A0: 0A 80 F0 FF FF 7F F0 FF  FF 7F 71 73 74 63 0B 80  ..........qstc..
00B0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x006D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x006E [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0073 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0074 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0075 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  5: 0x0084 [0x1D] PRINT_EVENT_MESSAGE(message_id=7503*)
    → "Stupendous-wendous! The sap you've brought back contains more dust than I could have hoped for!"
  6: 0x0087 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0088 [0x1D] PRINT_EVENT_MESSAGE(message_id=7504*)
    → "So much progress in so little time! This sends my research forward by monthy-wonths! Only a tad longer and I'll be able to concoctaru something that'll knock the pioneering world flat on its backside!"
  8: 0x008B [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x008C [0x1D] PRINT_EVENT_MESSAGE(message_id=7505*)
    → "Until then, I presentaru you with a token of my esteem."
 10: 0x008F [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0090 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
 12: 0x009F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 13: 0x00B0 [0x21] END_EVENT
 14: 0x00B1 [0x00] END_REQSTACK()
```

### Event 2507

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B2   |
| Data Size    | 44 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:       42 1E F0 FF FF 7F  6F 70 66 00 80 F8 FF FF    B.....opf.....
00C0: 7F F8 FF FF 7F 74 6C 6B  30 1D 08 80 23 66 00 80  .....tlk0...#f..
00D0: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 21 00        ........tlk1!.  
```

#### Opcodes

```
  0: 0x00B2 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00B3 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x00B8 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00B9 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x00BA [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  5: 0x00C9 [0x1D] PRINT_EVENT_MESSAGE(message_id=7504*)
    → "So much progress in so little time! This sends my research forward by monthy-wonths! Only a tad longer and I'll be able to concoctaru something that'll knock the pioneering world flat on its backside!"
  6: 0x00CC [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00CD [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
  8: 0x00DC [0x21] END_EVENT
  9: 0x00DD [0x00] END_REQSTACK()
```

### Event 23

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00DE  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00D0:                                            00                   . 
```

#### Opcodes

```
  0: 0x00DE [0x00] END_REQSTACK()
```
