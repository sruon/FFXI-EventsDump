# 17928271 - Valaineral R Davilles

## Common Data

| Field            | Value               |
|------------------|---------------------|
| Zone             | Leafallia (ID: 281) |
| Block Size       | 240 bytes           |
| Total Events     | 10                  |
| References Count | 17                  |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |     16 |              2 |
| [65535.2](#event-655352) | 0x0011       |     14 |              2 |
| [78](#event-78)          | 0x001F       |      7 |              2 |
| [79](#event-79)          | 0x0026       |      7 |              2 |
| [65535.3](#event-655353) | 0x002D       |     21 |              2 |
| [65535.4](#event-655354) | 0x0042       |     21 |              2 |
| [65535.5](#event-655355) | 0x0057       |     15 |              5 |
| [65535.6](#event-655356) | 0x0066       |      7 |              3 |
| [65535.7](#event-655357) | 0x006D       |      7 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0029      |          41 |
|       1 | 0x0005      |           5 |
|       2 | 0x0019      |          25 |
|       3 | 0x0000      |           0 |
|       4 | 0x01D9      |         473 |
|       5 | 0x0065      |         101 |
|       6 | 0x0379      |         889 |
|       7 | 0x0003      |           3 |
|       8 | 0x001A      |          26 |
|       9 | 0x004D      |          77 |
|      10 | 0x018F      |         399 |
|      11 | 0x001D      |          29 |
|      12 | 0x000D      |          13 |
|      13 | 0xFFFFB580  |  4294948224 |
|      14 | 0x0CE7      |        3303 |
|      15 | 0xFFFF14A6  |  4294907046 |
|      16 | 0x0001      |           1 |

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
0000:    66 00 80 F8 FF FF 7F  F8 FF FF 7F 63 61 62 6B   f..........cabk
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "cabk" with entities [EventEntity, EventEntity], work=41*
  1: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 14 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    53 F8 FF FF 7F F8 FF  FF 7F 63 61 62 6B 00      S........cabk. 
```

#### Opcodes

```
  0: 0x0011 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "cabk" with entities [EventEntity, EventEntity]
  1: 0x001E [0x00] END_REQSTACK()
```

### Event 78

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x001F  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               92                 .
0020: 01 F8 FF FF 7F 00                                 ......          
```

#### Opcodes

```
  0: 0x001F [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0025 [0x00] END_REQSTACK()
```

### Event 79

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0026  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   92 01  F8 FF FF 7F 00                 .......   
```

#### Opcodes

```
  0: 0x0026 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         B6 0B 01               ...
0030: 80 02 80 03 80 04 80 05  80 04 80 05 80 06 80 03  ................
0040: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x002D [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=5*, hair=25*, head=0*, body=473*, hands=101*, legs=473*, feet=101*, main=889*, sub=0*)
  1: 0x0041 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0042   |
| Data Size    | 21 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:       B6 0B 07 80 08 80  09 80 09 80 09 80 09 80    ..............
0050: 09 80 0A 80 0B 80 00                              .......         
```

#### Opcodes

```
  0: 0x0042 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=3*, hair=26*, head=77*, body=77*, hands=77*, legs=77*, feet=77*, main=399*, sub=29*)
  1: 0x0056 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0057   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      32  0C 80 1F 00 0D 80 0E 80         2........
0060: 0F 80 1F 01 6F 00                                 ....o.          
```

#### Opcodes

```
  0: 0x0057 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005A [0x1F] MOVE_ENTITY: EventEntity moves to X=-19.072*, Z=3.303*, Y=-60.250*
  2: 0x0062 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0064 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0065 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0066  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                   AB 03  AC 01 10 80 00                 .......   
```

#### Opcodes

```
  0: 0x0066 [0xAB] EventEntity->Render.Flags0 ^= 0x20000 // Toggle bit 17
  1: 0x0068 [0xAC] EventEntity->StatusEvent = 1*
  2: 0x006C [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x006D  |
| Data Size    | 7 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                         AC 01 03               ...
0070: 80 AB 04 00                                       ....            
```

#### Opcodes

```
  0: 0x006D [0xAC] EventEntity->StatusEvent = 0*
  1: 0x0071 [0xAB] EventEntity->Render.Flags0 |= 0x40000 // Set bit 18
  2: 0x0073 [0x00] END_REQSTACK()
```
