# 17756210 - Zayhi-Bauhi

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 504 bytes                |
| Total Events     | 17                       |
| References Count | 17                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      6 |              2 |
| [299](#event-299)        | 0x0017       |     19 |             10 |
| [61](#event-61)          | 0x002A       |     19 |             10 |
| [64](#event-64)          | 0x003D       |     11 |              4 |
| [65535.3](#event-655353) | 0x0048       |      9 |              5 |
| [69](#event-69)          | 0x0051       |     29 |             10 |
| [70](#event-70)          | 0x006E       |     30 |             11 |
| [73](#event-73)          | 0x008C       |     30 |             11 |
| [74](#event-74)          | 0x00AA       |     30 |             11 |
| [75](#event-75)          | 0x00C8       |     88 |             18 |
| [65535.4](#event-655354) | 0x0120       |     19 |              5 |
| [65535.5](#event-655355) | 0x0133       |      5 |              3 |
| [65535.6](#event-655356) | 0x0138       |      5 |              3 |
| [65535.7](#event-655357) | 0x013D       |      5 |              3 |
| [78](#event-78)          | 0x0142       |     29 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x1EDA      |        7898 |
|       2 | 0x1EDB      |        7899 |
|       3 | 0x1C49      |        7241 |
|       4 | 0x1C4A      |        7242 |
|       5 | 0x1C4D      |        7245 |
|       6 | 0x1C4E      |        7246 |
|       7 | 0x1C54      |        7252 |
|       8 | 0x1C57      |        7255 |
|       9 | 0x1C58      |        7256 |
|      10 | 0x00C9      |         201 |
|      11 | 0x0000      |           0 |
|      12 | 0x1C59      |        7257 |
|      13 | 0x1C5C      |        7260 |
|      14 | 0x1C5D      |        7261 |
|      15 | 0x1C5E      |        7262 |
|      16 | 0x1C64      |        7268 |

## String References

- **7241**: That we can now live here in peace...under the blessed shadow of the Great Star Tree...is all thanks to the great hero, Karaha-Baruha...!
- **7242**: Let the name of the great hero, Karaha-Baruha, not be forgotten! May we exalt the name of Karaha-Baruha on high!
- **7245**: Ha-hummm...we...arrrk...owe...our... <Cough>...peace...Hrmmm... A-hrmmm! <Cough> A-hrr-hrr-hrr-hrrmmm...!
- **7246**: Ha-hrr-hrr-hrrmmm...! A-hrr-hrr-hrr-hrr-hurrummm...!?
- **7252**: Ack...<cough!?> What's... A-hrmmm! this...? A-hrr-hrr-hrr-hrrmmm...!
- **7255**: A-ha! Ha-hrrmmm... That's a... A-hrr-hrrmmm little better...A-hrr-hrr-hurrummm. Quick! <Cough> Need more honey! A-hrr-hrr-hrr-hrrmmm!
- **7256**: A-hrrmmm. Feels like it's getting a lot better! But there's still some irritation... A-hrr-hrr-hrr-hrrmmm. See! <Hack>
- **7257**: Oh......
- **7260**: ......
- **7261**: My...tooth...
- **7262**: ...hurths...!
- **7268**: ...... Ouch...! My tooth hurths... Oo\`hhwww...
- **7898**: That we can now live here in peace...under the blessed shadow of the Great Star Tree...is all thanks to the great hero, Karaha-Baruha...!
- **7899**: Let the name of the great hero, Karaha-Baruha, not be forgotten! May we exalt the name of Karaha-Baruha on high!

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

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 6 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    5E 69 64 6C 30 00                               ^idl0.         
```

#### Opcodes

```
  0: 0x0011 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 299

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      1E  F0 FF FF 7F 6F 70 1D 01         .....op..
0020: 80 23 1D 02 80 23 20 00  21 00                    .#...# .!.      
```

#### Opcodes

```
  0: 0x0017 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x001D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x001E [0x1D] PRINT_EVENT_MESSAGE(message_id=7898*)
    → "That we can now live here in peace...under the blessed shadow of the Great Star Tree...is all thanks to the great hero, Karaha-Baruha...!"
  4: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0022 [0x1D] PRINT_EVENT_MESSAGE(message_id=7899*)
    → "Let the name of the great hero, Karaha-Baruha, not be forgotten! May we exalt the name of Karaha-Baruha on high!"
  6: 0x0025 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0026 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0028 [0x21] END_EVENT
  9: 0x0029 [0x00] END_REQSTACK()
```

### Event 61

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                1E F0 FF FF 7F 6F            .....o
0030: 70 1D 03 80 23 1D 04 80  23 20 00 21 00           p...#...# .!.   
```

#### Opcodes

```
  0: 0x002A [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x002F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0030 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0031 [0x1D] PRINT_EVENT_MESSAGE(message_id=7241*)
    → "That we can now live here in peace...under the blessed shadow of the Great Star Tree...is all thanks to the great hero, Karaha-Baruha...!"
  4: 0x0034 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0035 [0x1D] PRINT_EVENT_MESSAGE(message_id=7242*)
    → "Let the name of the great hero, Karaha-Baruha, not be forgotten! May we exalt the name of Karaha-Baruha on high!"
  6: 0x0038 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0039 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x003B [0x21] END_EVENT
  9: 0x003C [0x00] END_REQSTACK()
```

### Event 64

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 11 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         29 0B 32               ).2
0040: F0 0E 01 06 20 00 21 00                           .... .!.        
```

#### Opcodes

```
  0: 0x003D [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Zayhi-Bauhi (ID: 17756210/0x010EF032), tag_num=0x06)
  1: 0x0044 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  2: 0x0046 [0x21] END_EVENT
  3: 0x0047 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0048  |
| Data Size    | 9 bytes |
| Instructions | 5       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                          1D 05 80 23 1D 06 80 23          ...#...#
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0048 [0x1D] PRINT_EVENT_MESSAGE(message_id=7245*)
    → "Ha-hummm...we...arrrk...owe...our... <Cough>...peace...Hrmmm... A-hrmmm! <Cough> A-hrr-hrr-hrr-hrrmmm...!"
  1: 0x004B [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x004C [0x1D] PRINT_EVENT_MESSAGE(message_id=7246*)
    → "Ha-hrr-hrr-hrrmmm...! A-hrr-hrr-hrr-hrr-hurrummm...!?"
  3: 0x004F [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0050 [0x00] END_REQSTACK()
```

### Event 69

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0051   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    1E F0 FF FF 7F 6F 70  29 0B 32 F0 0E 01 01 1D   .....op).2.....
0060: 06 80 23 29 0B 32 F0 0E  01 02 20 00 21 00        ..#).2.... .!.  
```

#### Opcodes

```
  0: 0x0051 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0056 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0057 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0058 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Zayhi-Bauhi (ID: 17756210/0x010EF032), tag_num=0x01)
  4: 0x005F [0x1D] PRINT_EVENT_MESSAGE(message_id=7246*)
    → "Ha-hrr-hrr-hrrmmm...! A-hrr-hrr-hrr-hrr-hurrummm...!?"
  5: 0x0062 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0063 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Zayhi-Bauhi (ID: 17756210/0x010EF032), tag_num=0x02)
  7: 0x006A [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x006C [0x21] END_EVENT
  9: 0x006D [0x00] END_REQSTACK()
```

### Event 70

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006E   |
| Data Size    | 30 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                            42 1E                B.
0070: F0 FF FF 7F 6F 70 29 0B  32 F0 0E 01 01 1D 07 80  ....op).2.......
0080: 23 29 0B 32 F0 0E 01 02  20 00 21 00              #).2.... .!.    
```

#### Opcodes

```
  0: 0x006E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x006F [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0074 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0075 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0076 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Zayhi-Bauhi (ID: 17756210/0x010EF032), tag_num=0x01)
  5: 0x007D [0x1D] PRINT_EVENT_MESSAGE(message_id=7252*)
    → "Ack...<cough!?> What's... A-hrmmm! this...? A-hrr-hrr-hrr-hrrmmm...!"
  6: 0x0080 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0081 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Zayhi-Bauhi (ID: 17756210/0x010EF032), tag_num=0x02)
  8: 0x0088 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x008A [0x21] END_EVENT
 10: 0x008B [0x00] END_REQSTACK()
```

### Event 73

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x008C   |
| Data Size    | 30 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                                      42 1E F0 FF              B...
0090: FF 7F 6F 70 29 0B 32 F0  0E 01 01 1D 08 80 23 29  ..op).2.......#)
00A0: 0B 32 F0 0E 01 02 20 00  21 00                    .2.... .!.      
```

#### Opcodes

```
  0: 0x008C [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x008D [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0092 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0093 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0094 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Zayhi-Bauhi (ID: 17756210/0x010EF032), tag_num=0x01)
  5: 0x009B [0x1D] PRINT_EVENT_MESSAGE(message_id=7255*)
    → "A-ha! Ha-hrrmmm... That's a... A-hrr-hrrmmm little better...A-hrr-hrr-hurrummm. Quick! <Cough> Need more honey! A-hrr-hrr-hrr-hrrmmm!"
  6: 0x009E [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x009F [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Zayhi-Bauhi (ID: 17756210/0x010EF032), tag_num=0x02)
  8: 0x00A6 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x00A8 [0x21] END_EVENT
 10: 0x00A9 [0x00] END_REQSTACK()
```

### Event 74

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AA   |
| Data Size    | 30 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                42 1E F0 FF FF 7F            B.....
00B0: 6F 70 29 0B 32 F0 0E 01  01 1D 09 80 23 29 0B 32  op).2.......#).2
00C0: F0 0E 01 02 20 00 21 00                           .... .!.        
```

#### Opcodes

```
  0: 0x00AA [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00AB [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x00B0 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x00B1 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x00B2 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Zayhi-Bauhi (ID: 17756210/0x010EF032), tag_num=0x01)
  5: 0x00B9 [0x1D] PRINT_EVENT_MESSAGE(message_id=7256*)
    → "A-hrrmmm. Feels like it's getting a lot better! But there's still some irritation... A-hrr-hrr-hrr-hrrmmm. See! <Hack>"
  6: 0x00BC [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00BD [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Zayhi-Bauhi (ID: 17756210/0x010EF032), tag_num=0x02)
  8: 0x00C4 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  9: 0x00C6 [0x21] END_EVENT
 10: 0x00C7 [0x00] END_REQSTACK()
```

### Event 75

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C8   |
| Data Size    | 88 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                          42 20 01 1E F0 FF FF 7F          B ......
00D0: 6F 70 29 0E 32 F0 0E 01  0C 29 0E 34 F0 0E 01 0C  op).2....).4....
00E0: 29 0E 33 F0 0E 01 0C 29  0E 32 F0 0E 01 0D 29 0E  ).3....).2....).
00F0: 32 F0 0E 01 0E 29 0E 34  F0 0E 01 0D 29 0E 32 F0  2....).4....).2.
0100: 0E 01 0F 29 0E 33 F0 0E  01 0D 45 0A 80 F0 FF FF  ...).3....E.....
0110: 7F F0 FF FF 7F 71 73 74  63 0B 80 2E 20 00 21 00  .....qstc... .!.
```

#### Opcodes

```
  0: 0x00C8 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x00C9 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  2: 0x00CB [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x00D0 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x00D1 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x00D2 [0x29] REQ_SET_WAIT(priority=0x0E, entity_id=Zayhi-Bauhi (ID: 17756210/0x010EF032), tag_num=0x0C)
  6: 0x00D9 [0x29] REQ_SET_WAIT(priority=0x0E, entity_id=Kalupa-Tawalupa (ID: 17756212/0x010EF034), tag_num=0x0C)
  7: 0x00E0 [0x29] REQ_SET_WAIT(priority=0x0E, entity_id=Rutango-Botango (ID: 17756211/0x010EF033), tag_num=0x0C)
  8: 0x00E7 [0x29] REQ_SET_WAIT(priority=0x0E, entity_id=Zayhi-Bauhi (ID: 17756210/0x010EF032), tag_num=0x0D)
  9: 0x00EE [0x29] REQ_SET_WAIT(priority=0x0E, entity_id=Zayhi-Bauhi (ID: 17756210/0x010EF032), tag_num=0x0E)
 10: 0x00F5 [0x29] REQ_SET_WAIT(priority=0x0E, entity_id=Kalupa-Tawalupa (ID: 17756212/0x010EF034), tag_num=0x0D)
 11: 0x00FC [0x29] REQ_SET_WAIT(priority=0x0E, entity_id=Zayhi-Bauhi (ID: 17756210/0x010EF032), tag_num=0x0F)
 12: 0x0103 [0x29] REQ_SET_WAIT(priority=0x0E, entity_id=Rutango-Botango (ID: 17756211/0x010EF033), tag_num=0x0D)
 13: 0x010A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 14: 0x011B [0x2E] SET_CLI_EVENT_CANCEL_FLAGS()
 15: 0x011C [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 16: 0x011E [0x21] END_EVENT
 17: 0x011F [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0120   |
| Data Size    | 19 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0120: 29 0B 32 F0 0E 01 01 1D  0C 80 23 29 0B 32 F0 0E  ).2.......#).2..
0130: 01 02 00                                          ...             
```

#### Opcodes

```
  0: 0x0120 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Zayhi-Bauhi (ID: 17756210/0x010EF032), tag_num=0x01)
  1: 0x0127 [0x1D] PRINT_EVENT_MESSAGE(message_id=7257*)
    → "Oh......"
  2: 0x012A [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x012B [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Zayhi-Bauhi (ID: 17756210/0x010EF032), tag_num=0x02)
  4: 0x0132 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0133  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:          1D 0D 80 23 00                              ...#.        
```

#### Opcodes

```
  0: 0x0133 [0x1D] PRINT_EVENT_MESSAGE(message_id=7260*)
    → "......"
  1: 0x0136 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0137 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0138  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                          1D 0E 80 23 00                   ...#.   
```

#### Opcodes

```
  0: 0x0138 [0x1D] PRINT_EVENT_MESSAGE(message_id=7261*)
    → "My...tooth..."
  1: 0x013B [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x013C [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x013D  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0130:                                         1D 0F 80               ...
0140: 23 00                                             #.              
```

#### Opcodes

```
  0: 0x013D [0x1D] PRINT_EVENT_MESSAGE(message_id=7262*)
    → "...hurths...!"
  1: 0x0140 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0141 [0x00] END_REQSTACK()
```

### Event 78

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0142   |
| Data Size    | 29 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:       1E F0 FF FF 7F 6F  70 29 0B 32 F0 0E 01 01    .....op).2....
0150: 1D 10 80 23 29 0B 32 F0  0E 01 02 20 00 21 00     ...#).2.... .!. 
```

#### Opcodes

```
  0: 0x0142 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0147 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0148 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0149 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Zayhi-Bauhi (ID: 17756210/0x010EF032), tag_num=0x01)
  4: 0x0150 [0x1D] PRINT_EVENT_MESSAGE(message_id=7268*)
    → "...... Ouch...! My tooth hurths... Oo`hhwww..."
  5: 0x0153 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0154 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Zayhi-Bauhi (ID: 17756210/0x010EF032), tag_num=0x02)
  7: 0x015B [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x015D [0x21] END_EVENT
  9: 0x015E [0x00] END_REQSTACK()
```
