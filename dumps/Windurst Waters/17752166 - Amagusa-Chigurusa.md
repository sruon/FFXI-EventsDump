# 17752166 - Amagusa-Chigurusa

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 272 bytes                 |
| Total Events     | 7                         |
| References Count | 9                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     22 |              4 |
| [65535.3](#event-655353) | 0x0027       |      9 |              3 |
| [562](#event-562)        | 0x0030       |     33 |             12 |
| [937](#event-937)        | 0x0051       |    107 |             19 |
| [1069](#event-1069)      | 0x00BC       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x001E      |          30 |
|       2 | 0x2261      |        8801 |
|       3 | 0x2262      |        8802 |
|       4 | 0x2FFE      |       12286 |
|       5 | 0x3001      |       12289 |
|       6 | 0x3002      |       12290 |
|       7 | 0x3003      |       12291 |
|       8 | 0x3004      |       12292 |

## String References

- **8801**: Don'taru you think the world's become all so rowdy-dowdy lately? The Manustery making Cardians like there's no tomorrow... The Orastery has gone and allowed the sale of high-level magic...
- **8802**: A guy's got to think of an escape plan in case the whole place gets pulled into a war or something.
- **12286**: <Player>'s badge flashes brightly.
- **12289**: Don'taru you think the world's become all so rowdy-dowdy lately? The Manustery's remodeling the Cardians like there's no tomorrow!
- **12290**: There could plausibly, possibly be a war soon! Could it entail...an expedient expedition to the Near East? No way, right!?

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

### Event 65535.3

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0027  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                      5E  69 64 6C 30 1C 01 80 00         ^idl0....
```

#### Opcodes

```
  0: 0x0027 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x002C [0x1C] WAIT(30* ticks)
  2: 0x002F [0x00] END_REQSTACK()
```

### Event 562

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 1E F0 FF FF 7F 6F 70 29  08 66 E0 0E 01 01 1D 02  .....op).f......
0040: 80 23 1D 03 80 23 29 08  66 E0 0E 01 02 20 00 21  .#...#).f.... .!
0050: 00                                                .               
```

#### Opcodes

```
  0: 0x0030 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0035 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0036 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0037 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Amagusa-Chigurusa (ID: 17752166/0x010EE066), tag_num=0x01)
  4: 0x003E [0x1D] PRINT_EVENT_MESSAGE(message_id=8801*)
    → "Don'taru you think the world's become all so rowdy-dowdy lately? The Manustery making Cardians like there's no tomorrow... The Orastery has gone and allowed the sale of high-level magic..."
  5: 0x0041 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0042 [0x1D] PRINT_EVENT_MESSAGE(message_id=8802*)
    → "A guy's got to think of an escape plan in case the whole place gets pulled into a war or something."
  7: 0x0045 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0046 [0x29] REQ_SET_WAIT(priority=0x08, entity_id=Amagusa-Chigurusa (ID: 17752166/0x010EE066), tag_num=0x02)
  9: 0x004D [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x004F [0x21] END_EVENT
 11: 0x0050 [0x00] END_REQSTACK()
```

### Event 937

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0051    |
| Data Size    | 107 bytes |
| Instructions | 19        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:    42 48 04 80 1E 67 E0  0E 01 1C 01 80 4A 67 E0   BH...g......Jg.
0060: 0E 01 66 E0 0E 01 66 00  80 F8 FF FF 7F F8 FF FF  ..f...f.........
0070: 7F 74 6C 6B 30 1D 05 80  23 1D 06 80 23 66 00 80  .tlk0...#...#f..
0080: F8 FF FF 7F F8 FF FF 7F  74 6C 6B 31 66 00 80 67  ........tlk1f..g
0090: E0 0E 01 67 E0 0E 01 74  6C 6B 30 2B 67 E0 0E 01  ...g...tlk0+g...
00A0: 07 80 23 2B 67 E0 0E 01  08 80 23 66 00 80 67 E0  ..#+g.....#f..g.
00B0: 0E 01 67 E0 0E 01 74 6C  6B 31 21 00              ..g...tlk1!.    
```

#### Opcodes

```
  0: 0x0051 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0052 [0x48] [System] [12286*]:
    → "<Player>'s badge flashes brightly."
  2: 0x0055 [0x1E] EventEntity looks at Kobite-Mojite (ID: 17752167/0x010EE067) and starts talking
  3: 0x005A [0x1C] WAIT(30* ticks)
  4: 0x005D [0x4A] Kobite-Mojite (ID: 17752167/0x010EE067) looks at Amagusa-Chigurusa (ID: 17752166/0x010EE066)
  5: 0x0066 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  6: 0x0075 [0x1D] PRINT_EVENT_MESSAGE(message_id=12289*)
    → "Don'taru you think the world's become all so rowdy-dowdy lately? The Manustery's remodeling the Cardians like there's no tomorrow!"
  7: 0x0078 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0079 [0x1D] PRINT_EVENT_MESSAGE(message_id=12290*)
    → "There could plausibly, possibly be a war soon! Could it entail...an expedient expedition to the Near East? No way, right!?"
  9: 0x007C [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x007D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
 11: 0x008C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Kobite-Mojite (ID: 17752167/0x010EE067), Kobite-Mojite (ID: 17752167/0x010EE067)], work=40*
 12: 0x009B [0x2B] Kobite-Mojite (ID: 17752167/0x010EE067) [12291*]:
    → "That should be none of your concern."
 13: 0x00A2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x00A3 [0x2B] Kobite-Mojite (ID: 17752167/0x010EE067) [12292*]:
    → "So long as the Star Sibyl blesses us with her presence, the peace of Windurst is a given."
 15: 0x00AA [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x00AB [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Kobite-Mojite (ID: 17752167/0x010EE067), Kobite-Mojite (ID: 17752167/0x010EE067)], work=40*
 17: 0x00BA [0x21] END_EVENT
 18: 0x00BB [0x00] END_REQSTACK()
```

### Event 1069

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00BC  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                      00                       .   
```

#### Opcodes

```
  0: 0x00BC [0x00] END_REQSTACK()
```
