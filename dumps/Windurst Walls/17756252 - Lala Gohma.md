# 17756252 - Lala Gohma

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 180 bytes                |
| Total Events     | 7                        |
| References Count | 4                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |      9 |              3 |
| [443](#event-443)        | 0x001A       |      7 |              2 |
| [328](#event-328)        | 0x0021       |     33 |             12 |
| [550](#event-550)        | 0x0042       |     26 |              8 |
| [551](#event-551)        | 0x005C       |     27 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x001E      |          30 |
|       2 | 0x1F0E      |        7950 |
|       3 | 0x1F0F      |        7951 |

## String References

- **7950**: Not only the Star Sibyl lives in Heavens Towerrr. Her ladies-in-waiting and the Mithra Sibyl Guards also serrrve her there.
- **7951**: Out of all the guards protecting the Star Sibyl, Semih Lafihna is the most powerrrful. And why shouldn't she be? She is the only Mithra worrrthy enough to accept our chieftainness's bow.

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
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=50*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0011  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    5E 69 64 6C 30 1C 01  80 00                     ^idl0....      
```

#### Opcodes

```
  0: 0x0011 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0016 [0x1C] WAIT(30* ticks)
  2: 0x0019 [0x00] END_REQSTACK()
```

### Event 443

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001A  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                92 01 F8 FF FF 7F            ......
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x001A [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0020 [0x00] END_REQSTACK()
```

### Event 328

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 33 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    1E F0 FF FF 7F 6F 70  29 0B 5C F0 0E 01 01 1D   .....op).\.....
0030: 02 80 23 1D 03 80 23 29  0B 5C F0 0E 01 02 20 00  ..#...#).\.... .
0040: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x0021 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0026 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0027 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0028 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Lala Gohma (ID: 17756252/0x010EF05C), tag_num=0x01)
  4: 0x002F [0x1D] PRINT_EVENT_MESSAGE(message_id=7950*)
    → "Not only the Star Sibyl lives in Heavens Towerrr. Her ladies-in-waiting and the Mithra Sibyl Guards also serrrve her there."
  5: 0x0032 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0033 [0x1D] PRINT_EVENT_MESSAGE(message_id=7951*)
    → "Out of all the guards protecting the Star Sibyl, Semih Lafihna is the most powerrrful. And why shouldn't she be? She is the only Mithra worrrthy enough to accept our chieftainness's bow."
  7: 0x0036 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0037 [0x29] REQ_SET_WAIT(priority=0x0B, entity_id=Lala Gohma (ID: 17756252/0x010EF05C), tag_num=0x02)
  9: 0x003E [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
 10: 0x0040 [0x21] END_EVENT
 11: 0x0041 [0x00] END_REQSTACK()
```

### Event 550

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0042   |
| Data Size    | 26 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       4A F8 FF FF 7F F0  FF FF 7F 4A F0 FF FF 7F    J........J....
0050: F8 FF FF 7F 6F 70 1D 05  10 23 21 00              ....op...#!.    
```

#### Opcodes

```
  0: 0x0042 [0x4A] EventEntity looks at LocalPlayer
  1: 0x004B [0x4A] LocalPlayer looks at EventEntity
  2: 0x0054 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0055 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0056 [0x1D] PRINT_EVENT_MESSAGE(message_id=Work_Zone[5])
  5: 0x0059 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x005A [0x21] END_EVENT
  7: 0x005B [0x00] END_REQSTACK()
```

### Event 551

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005C   |
| Data Size    | 27 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                      42 4A F8 FF              BJ..
0060: FF 7F F0 FF FF 7F 4A F0  FF FF 7F F8 FF FF 7F 6F  ......J........o
0070: 70 1D 05 10 23 21 00                              p...#!.         
```

#### Opcodes

```
  0: 0x005C [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x005D [0x4A] EventEntity looks at LocalPlayer
  2: 0x0066 [0x4A] LocalPlayer looks at EventEntity
  3: 0x006F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0070 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x0071 [0x1D] PRINT_EVENT_MESSAGE(message_id=Work_Zone[5])
  6: 0x0074 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0075 [0x21] END_EVENT
  8: 0x0076 [0x00] END_REQSTACK()
```
