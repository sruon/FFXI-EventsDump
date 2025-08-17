# 17772550 - Heimji-Keimji

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 348 bytes                 |
| Total Events     | 10                        |
| References Count | 23                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      3 |              2 |
| [40](#event-40)          | 0x0003       |     12 |              3 |
| [131](#event-131)        | 0x000F       |     12 |              3 |
| [65535.1](#event-655351) | 0x001B       |     67 |             18 |
| [65535.2](#event-655352) | 0x005E       |     19 |              3 |
| [65535.3](#event-655353) | 0x0071       |     19 |              3 |
| [65535.4](#event-655354) | 0x0084       |     29 |              3 |
| [65535.5](#event-655355) | 0x00A1       |     29 |              3 |
| [65535.6](#event-655356) | 0x00BE       |      9 |              3 |
| [65535.7](#event-655357) | 0x00C7       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x8107      |       33031 |
|       1 | 0xFFFFD0CF  |  4294955215 |
|       2 | 0x2133      |        8499 |
|       3 | 0x0430      |        1072 |
|       4 | 0x8180      |       33152 |
|       5 | 0xFFFFD148  |  4294955336 |
|       6 | 0x0429      |        1065 |
|       7 | 0x003C      |          60 |
|       8 | 0x000D      |          13 |
|       9 | 0x8382      |       33666 |
|      10 | 0xFFFFD197  |  4294955415 |
|      11 | 0x2134      |        8500 |
|      12 | 0x8698      |       34456 |
|      13 | 0xFFFFD246  |  4294955590 |
|      14 | 0x2327      |        8999 |
|      15 | 0x8C7A      |       35962 |
|      16 | 0xFFFFD171  |  4294955377 |
|      17 | 0x8B6E      |       35694 |
|      18 | 0xFFFFC87E  |  4294953086 |
|      19 | 0x8190      |       33168 |
|      20 | 0xFFFFC847  |  4294953031 |
|      21 | 0x0028      |          40 |
|      22 | 0x002D      |          45 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 3 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 22 00 00                                          "..             
```

#### Opcodes

```
  0: 0x0000 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0002 [0x00] END_REQSTACK()
```

### Event 40

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          33 01 37 00 80  01 80 02 80 03 80 00        3.7......... 
```

#### Opcodes

```
  0: 0x0003 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0005 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=33.031*, z=-12.081*, y=8.499*, direction=94.2°*
  2: 0x000E [0x00] END_REQSTACK()
```

### Event 131

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               33                 3
0010: 01 37 04 80 05 80 02 80  06 80 00                 .7.........     
```

#### Opcodes

```
  0: 0x000F [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0011 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=33.152*, z=-11.960*, y=8.499*, direction=93.6°*
  2: 0x001A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 67 bytes |
| Instructions | 18       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   1C 07 80 32 08             ...2.
0020: 80 1F 00 09 80 0A 80 0B  80 1F 01 33 00 1F 00 0C  ...........3....
0030: 80 0D 80 0E 80 1F 01 1F  00 0F 80 10 80 0E 80 1F  ................
0040: 01 1F 00 11 80 12 80 0E  80 1F 01 1F 00 13 80 14  ................
0050: 80 0E 80 1F 01 6F 1E F0  FF FF 7F 6F 70 00        .....o.....op.  
```

#### Opcodes

```
  0: 0x001B [0x1C] WAIT(60* ticks)
  1: 0x001E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0021 [0x1F] MOVE_ENTITY: EventEntity moves to X=33.666*, Z=-11.881*, Y=8.500*
  3: 0x0029 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x002B [0x33] EventEntity->Render.Flags0 &= ~ 0x200000 // Bit 21 (flag=0x00)
  5: 0x002D [0x1F] MOVE_ENTITY: EventEntity moves to X=34.456*, Z=-11.706*, Y=8.999*
  6: 0x0035 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0037 [0x1F] MOVE_ENTITY: EventEntity moves to X=35.962*, Z=-11.919*, Y=8.999*
  8: 0x003F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  9: 0x0041 [0x1F] MOVE_ENTITY: EventEntity moves to X=35.694*, Z=-14.210*, Y=8.999*
 10: 0x0049 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 11: 0x004B [0x1F] MOVE_ENTITY: EventEntity moves to X=33.168*, Z=-14.265*, Y=8.999*
 12: 0x0053 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
 13: 0x0055 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 14: 0x0056 [0x1E] EventEntity looks at LocalPlayer and starts talking
 15: 0x005B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 16: 0x005C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 17: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005E   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            66 15                f.
0060: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 1C 07 80  .........tlk0...
0070: 00                                                .               
```

#### Opcodes

```
  0: 0x005E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  1: 0x006D [0x1C] WAIT(60* ticks)
  2: 0x0070 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0071   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:    66 15 80 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 31   f..........thk1
0080: 1C 07 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0071 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=40*
  1: 0x0080 [0x1C] WAIT(60* ticks)
  2: 0x0083 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0084   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:             66 15 80 F8  FF FF 7F F8 FF FF 7F 74      f..........t
0090: 68 6B 32 53 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 32  hk2S........thk2
00A0: 00                                                .               
```

#### Opcodes

```
  0: 0x0084 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=40*
  1: 0x0093 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  2: 0x00A0 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00A1   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:    66 16 80 F8 FF FF 7F  F8 FF FF 7F 73 6C 33 30   f..........sl30
00B0: 53 F8 FF FF 7F F8 FF FF  7F 73 6C 33 30 00        S........sl30.  
```

#### Opcodes

```
  0: 0x00A1 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "sl30" with entities [EventEntity, EventEntity], work=45*
  1: 0x00B0 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "sl30" with entities [EventEntity, EventEntity]
  2: 0x00BD [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00BE  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                                            5E 69                ^i
00C0: 64 6C 30 1C 07 80 00                              dl0....         
```

#### Opcodes

```
  0: 0x00BE [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x00C3 [0x1C] WAIT(60* ticks)
  2: 0x00C6 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00C7  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                      00                                  .        
```

#### Opcodes

```
  0: 0x00C7 [0x00] END_REQSTACK()
```
