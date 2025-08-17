# 17814116 - Wanzo-Unzozo

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Abyssea - Uleguerand (ID: 253) |
| Block Size       | 304 bytes                      |
| Total Events     | 7                              |
| References Count | 16                             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [329](#event-329)     | 0x0001       |     13 |              7 |
| [330](#event-330)     | 0x000E       |     47 |             15 |
| [331](#event-331)     | 0x003D       |     13 |              7 |
| [332](#event-332)     | 0x004A       |     83 |             23 |
| [333](#event-333)     | 0x009D       |     13 |              7 |
| [335](#event-335)     | 0x00AA       |     25 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1F65      |        8037 |
|       1 | 0x003C      |          60 |
|       2 | 0x0020      |          32 |
|       3 | 0x1F66      |        8038 |
|       4 | 0x0001      |           1 |
|       5 | 0x0300      |         768 |
|       6 | 0x1F67      |        8039 |
|       7 | 0x0002      |           2 |
|       8 | 0x1008      |        4104 |
|       9 | 0x1000      |        4096 |
|      10 | 0x0015      |          21 |
|      11 | 0x1F68      |        8040 |
|      12 | 0x1F69      |        8041 |
|      13 | 0x1F6A      |        8042 |
|      14 | 0x0019      |          25 |
|      15 | 0x1F6B      |        8043 |

## String References

- **8037**: Yeees? Is something the mattaru?
- **8038**: I say, it's posi-wositively freezing, wouldn't you say? I don't suppose you've seen anything around that could be used to startaru a nice, cozy fire, have you?
- **8039**: $0! With this I can start a fire to keep myself toasty-woasty and cook up a piping hot dinner! Rondipur? Oh, yes, I'll contactaru the old bore sooner or later.
- **8040**: $0! Wherever did you find this? Now I can start a fire to keep myself toasty-woasty and cook up a piping hot dinner! Rondipur? Don't worry, I'll contactaru the old bore sooner or later.
- **8041**: Ta-taru! See you 'round!
- **8042**: Now I can start a fire to keep myself toasty-woasty and cook up a piping hot dinner! Rondipur? Don't worry, I'll contact the old bore sooner or lataru.
- **8043**: Rondipur chewy-wewed me up good and proper. The nerve of that man! He could go a long way toward improving morale if he'd provision us with something tastier than buffalo jerky to eataru!

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

### Event 329

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 21 00         .....op...#!.  
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=8037*)
    → "Yeees? Is something the mattaru?"
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x21] END_EVENT
  6: 0x000D [0x00] END_REQSTACK()
```

### Event 330

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000E   |
| Data Size    | 47 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                            42 1E                B.
0010: F0 FF FF 7F 6F 70 1D 00  80 23 27 10 F0 FF FF 7F  ....op...#'.....
0020: 04 1C 01 80 27 10 F0 FF  FF 7F 05 6E 64 D2 0F 01  ....'......nd...
0030: 02 80 99 64 D2 0F 01 1D  03 80 23 21 00           ...d......#!.   
```

#### Opcodes

```
  0: 0x000E [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x000F [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0014 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0015 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0016 [0x1D] PRINT_EVENT_MESSAGE(message_id=8037*)
    → "Yeees? Is something the mattaru?"
  5: 0x0019 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001A [0x27] REQ_SET(priority=0x10, entity_id=LocalPlayer, tag_num=0x04)
  7: 0x0021 [0x1C] WAIT(60* ticks)
  8: 0x0024 [0x27] REQ_SET(priority=0x10, entity_id=LocalPlayer, tag_num=0x05)
  9: 0x002B [0x6E] Wanzo-Unzozo (ID: 17814116/0x010FD264) uses emote 32*
 10: 0x0032 [0x99] Wait for Wanzo-Unzozo (ID: 17814116/0x010FD264) animation to complete
 11: 0x0037 [0x1D] PRINT_EVENT_MESSAGE(message_id=8038*)
    → "I say, it's posi-wositively freezing, wouldn't you say? I don't suppose you've seen anything around that could be used to startaru a nice, cozy fire, have you?"
 12: 0x003A [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x003B [0x21] END_EVENT
 14: 0x003C [0x00] END_REQSTACK()
```

### Event 331

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003D   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                         1E F0 FF               ...
0040: FF 7F 6F 70 1D 03 80 23  21 00                    ..op...#!.      
```

#### Opcodes

```
  0: 0x003D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0042 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0043 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0044 [0x1D] PRINT_EVENT_MESSAGE(message_id=8038*)
    → "I say, it's posi-wositively freezing, wouldn't you say? I don't suppose you've seen anything around that could be used to startaru a nice, cozy fire, have you?"
  4: 0x0047 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0048 [0x21] END_EVENT
  6: 0x0049 [0x00] END_REQSTACK()
```

### Event 332

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 83 bytes |
| Instructions | 23       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                42 1E F0 FF FF 7F            B.....
0050: 6F 70 02 02 10 04 80 00  72 00 03 02 10 05 80 6E  op......r......n
0060: 64 D2 0F 01 04 80 99 64  D2 0F 01 1D 06 80 23 01  d......d......#.
0070: 97 00 02 02 10 07 80 00  82 00 03 02 10 08 80 01  ................
0080: 87 00 03 02 10 09 80 6E  64 D2 0F 01 0A 80 99 64  .......nd......d
0090: D2 0F 01 1D 0B 80 23 1D  0C 80 23 21 00           ......#...#!.   
```

#### Opcodes

```
  0: 0x004A [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x004B [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0050 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0051 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0052 [0x02] IF !(Work_Zone[2] == 1*) GOTO 0x0072
  5: 0x005A [0x03] Work_Zone[2] = 768*
  6: 0x005F [0x6E] Wanzo-Unzozo (ID: 17814116/0x010FD264) uses emote 1*
  7: 0x0066 [0x99] Wait for Wanzo-Unzozo (ID: 17814116/0x010FD264) animation to complete
  8: 0x006B [0x1D] PRINT_EVENT_MESSAGE(message_id=8039*)
    → "$0! With this I can start a fire to keep myself toasty-woasty and cook up a piping hot dinner! Rondipur? Oh, yes, I'll contactaru the old bore sooner or later."
  9: 0x006E [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x006F [0x01] GOTO 0x0097
 11: 0x0072 [0x02] IF !(Work_Zone[2] == 2*) GOTO 0x0082
 12: 0x007A [0x03] Work_Zone[2] = 4104*
 13: 0x007F [0x01] GOTO 0x0087
 14: 0x0082 [0x03] Work_Zone[2] = 4096*

SUBROUTINE_0087:
 15: 0x0087 [0x6E] Wanzo-Unzozo (ID: 17814116/0x010FD264) uses emote 21*
 16: 0x008E [0x99] Wait for Wanzo-Unzozo (ID: 17814116/0x010FD264) animation to complete
 17: 0x0093 [0x1D] PRINT_EVENT_MESSAGE(message_id=8040*)
    → "$0! Wherever did you find this? Now I can start a fire to keep myself toasty-woasty and cook up a piping hot dinner! Rondipur? Don't worry, I'll contactaru the old bore sooner or later."
 18: 0x0096 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_0097:
 19: 0x0097 [0x1D] PRINT_EVENT_MESSAGE(message_id=8041*)
    → "Ta-taru! See you 'round!"
 20: 0x009A [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x009B [0x21] END_EVENT
 22: 0x009C [0x00] END_REQSTACK()
```

### Event 333

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x009D   |
| Data Size    | 13 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                         1E F0 FF               ...
00A0: FF 7F 6F 70 1D 0D 80 23  21 00                    ..op...#!.      
```

#### Opcodes

```
  0: 0x009D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00A2 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00A3 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00A4 [0x1D] PRINT_EVENT_MESSAGE(message_id=8042*)
    → "Now I can start a fire to keep myself toasty-woasty and cook up a piping hot dinner! Rondipur? Don't worry, I'll contact the old bore sooner or lataru."
  4: 0x00A7 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00A8 [0x21] END_EVENT
  6: 0x00A9 [0x00] END_REQSTACK()
```

### Event 335

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00AA   |
| Data Size    | 25 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                                1E F0 FF FF 7F 6F            .....o
00B0: 70 6E 64 D2 0F 01 0E 80  99 64 D2 0F 01 1D 0F 80  pnd......d......
00C0: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x00AA [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x00AF [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x00B0 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x00B1 [0x6E] Wanzo-Unzozo (ID: 17814116/0x010FD264) uses emote 25*
  4: 0x00B8 [0x99] Wait for Wanzo-Unzozo (ID: 17814116/0x010FD264) animation to complete
  5: 0x00BD [0x1D] PRINT_EVENT_MESSAGE(message_id=8043*)
    → "Rondipur chewy-wewed me up good and proper. The nerve of that man! He could go a long way toward improving morale if he'd provision us with something tastier than buffalo jerky to eataru!"
  6: 0x00C0 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x00C1 [0x21] END_EVENT
  8: 0x00C2 [0x00] END_REQSTACK()
```
