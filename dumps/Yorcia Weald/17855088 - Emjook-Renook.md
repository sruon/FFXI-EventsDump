# 17855088 - Emjook-Renook

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Yorcia Weald (ID: 263) |
| Block Size       | 356 bytes              |
| Total Events     | 12                     |
| References Count | 17                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [106](#event-106)        | 0x0027       |     45 |             11 |
| [109](#event-109)        | 0x0054       |      1 |              1 |
| [65535.3](#event-655353) | 0x0055       |     30 |              8 |
| [110](#event-110)        | 0x0073       |     32 |             10 |
| [111](#event-111)        | 0x0093       |      1 |              1 |
| [112](#event-112)        | 0x0094       |     28 |              8 |
| [59](#event-59)          | 0x00B0       |      1 |              1 |
| [65535.4](#event-655354) | 0x00B1       |     14 |              4 |
| [60](#event-60)          | 0x00BF       |     32 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x221A      |        8730 |
|       3 | 0x221B      |        8731 |
|       4 | 0x58EEF     |      364271 |
|       5 | 0x2433F     |      148287 |
|       6 | 0x00CD      |         205 |
|       7 | 0x0031      |          49 |
|       8 | 0x1F44      |        8004 |
|       9 | 0x1F45      |        8005 |
|      10 | 0x1F58      |        8024 |
|      11 | 0x000D      |          13 |
|      12 | 0x58E4C     |      364108 |
|      13 | 0x244C6     |      148678 |
|      14 | 0x00D7      |         215 |
|      15 | 0x1F6D      |        8045 |
|      16 | 0x1F6E      |        8046 |

## String References

- **8004**: I can't say for sure, but I assume I lostaru my badge around the coordinates J-8, H-9, or I-8.
- **8005**: I'm beg-wegging you, please find it for me. I'm as good as dead without it!
- **8024**: Robertioux's abilities certainly rival-wival the Merciless One's, if not surpass them.
- **8045**: Borghest is right. The best option is to inform-worm the coalition representatives in Foret de Hennetiel and beseech their aid.
- **8046**: We're countaruing on you!
- **8730**: No one who has found this frontier station has ever returned to Adoulin, for Yorcia Weald is a veritable labyrinth-wabyrinth of vegetation.
- **8731**: Truth be told, it's a miracle you made it here in the firstaru place.

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30   f..........tlk0
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 22 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 5E 69   S........tlk0^i
0020: 64 6C 30 1C 01 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  1: 0x001E [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  2: 0x0023 [0x1C] WAIT(30* ticks)
  3: 0x0026 [0x00] END_REQSTACK()
```

### Event 106

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0027   |
| Data Size    | 45 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      1E  F0 FF FF 7F 6F 70 66 00         .....opf.
0030: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 1D 02 80  .........tlk0...
0040: 23 1D 03 80 23 53 F8 FF  FF 7F F8 FF FF 7F 74 6C  #...#S........tl
0050: 6B 30 21 00                                       k0!.            
```

#### Opcodes

```
  0: 0x0027 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x002C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x002D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x002E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  4: 0x003D [0x1D] PRINT_EVENT_MESSAGE(message_id=8730*)
    → "No one who has found this frontier station has ever returned to Adoulin, for Yorcia Weald is a veritable labyrinth-wabyrinth of vegetation."
  5: 0x0040 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0041 [0x1D] PRINT_EVENT_MESSAGE(message_id=8731*)
    → "Truth be told, it's a miracle you made it here in the firstaru place."
  7: 0x0044 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0045 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  9: 0x0052 [0x21] END_EVENT
 10: 0x0053 [0x00] END_REQSTACK()
```

### Event 109

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0054  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             00                                        .           
```

#### Opcodes

```
  0: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0055   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                32 00 80  1F 00 04 80 05 80 06 80       2..........
0060: 1F 01 1E F0 FF FF 7F 1C  01 80 1E 43 72 10 01 1C  ...........Cr...
0070: 01 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0055 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0058 [0x1F] MOVE_ENTITY: EventEntity moves to X=364.271*, Z=148.287*, Y=0.205*
  2: 0x0060 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0062 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x0067 [0x1C] WAIT(30* ticks)
  5: 0x006A [0x1E] EventEntity looks at Reepi-Molpi (ID: 17855043/0x01107243) and starts talking
  6: 0x006F [0x1C] WAIT(30* ticks)
  7: 0x0072 [0x00] END_REQSTACK()
```

### Event 110

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 32 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          1E F0 FF FF 7F  6F 70 66 07 80 F8 FF FF     .....opf.....
0080: 7F F8 FF FF 7F 74 6C 6B  30 1D 08 80 23 1D 09 80  .....tlk0...#...
0090: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x0073 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0078 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0079 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x007A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  4: 0x0089 [0x1D] PRINT_EVENT_MESSAGE(message_id=8004*)
    → "I can't say for sure, but I assume I lostaru my badge around the coordinates J-8, H-9, or I-8."
  5: 0x008C [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x008D [0x1D] PRINT_EVENT_MESSAGE(message_id=8005*)
    → "I'm beg-wegging you, please find it for me. I'm as good as dead without it!"
  7: 0x0090 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0091 [0x21] END_EVENT
  9: 0x0092 [0x00] END_REQSTACK()
```

### Event 111

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0093  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:          00                                          .            
```

#### Opcodes

```
  0: 0x0093 [0x00] END_REQSTACK()
```

### Event 112

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0094   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:             1E F0 FF FF  7F 6F 70 66 07 80 F8 FF      .....opf....
00A0: FF 7F F8 FF FF 7F 74 6C  6B 30 1D 0A 80 23 21 00  ......tlk0...#!.
```

#### Opcodes

```
  0: 0x0094 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0099 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x009A [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x009B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  4: 0x00AA [0x1D] PRINT_EVENT_MESSAGE(message_id=8024*)
    → "Robertioux's abilities certainly rival-wival the Merciless One's, if not surpass them."
  5: 0x00AD [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00AE [0x21] END_EVENT
  7: 0x00AF [0x00] END_REQSTACK()
```

### Event 59

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00B0  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0: 00                                                .               
```

#### Opcodes

```
  0: 0x00B0 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B1   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:    32 0B 80 1F 00 0C 80  0D 80 0E 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x00B1 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x00B4 [0x1F] MOVE_ENTITY: EventEntity moves to X=364.108*, Z=148.678*, Y=0.215*
  2: 0x00BC [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x00BE [0x00] END_REQSTACK()
```

### Event 60

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00BF   |
| Data Size    | 32 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                               1E                 .
00C0: F0 FF FF 7F 6F 70 66 07  80 F8 FF FF 7F F8 FF FF  ....opf.........
00D0: 7F 74 6C 6B 30 1D 0F 80  23 1D 10 80 23 21 00     .tlk0...#...#!. 
```

#### Opcodes

```
  0: 0x00BF [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00C4 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00C5 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00C6 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  4: 0x00D5 [0x1D] PRINT_EVENT_MESSAGE(message_id=8045*)
    → "Borghest is right. The best option is to inform-worm the coalition representatives in Foret de Hennetiel and beseech their aid."
  5: 0x00D8 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x00D9 [0x1D] PRINT_EVENT_MESSAGE(message_id=8046*)
    → "We're countaruing on you!"
  7: 0x00DC [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00DD [0x21] END_EVENT
  9: 0x00DE [0x00] END_REQSTACK()
```
