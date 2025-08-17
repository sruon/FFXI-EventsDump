# 16982440 - Sahnadjean

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Aht Urhgan Whitegate2 (ID: 50) |
| Block Size       | 188 bytes                      |
| Total Events     | 7                              |
| References Count | 15                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [894](#event-894)        | 0x0001       |      1 |              1 |
| [897](#event-897)        | 0x0002       |      1 |              1 |
| [65535.1](#event-655351) | 0x0003       |     15 |              5 |
| [65535.2](#event-655352) | 0x0012       |     20 |              6 |
| [65535.3](#event-655353) | 0x0026       |     15 |              5 |
| [65535.4](#event-655354) | 0x0035       |     29 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000C      |          12 |
|       1 | 0x12990     |       76176 |
|       2 | 0xFFFDFEB3  |  4294835891 |
|       3 | 0xFFFFE891  |  4294961297 |
|       4 | 0x000D      |          13 |
|       5 | 0x13359     |       78681 |
|       6 | 0xFFFDF613  |  4294833683 |
|       7 | 0xFFFFE890  |  4294961296 |
|       8 | 0x12FED     |       77805 |
|       9 | 0xFFFE13F2  |  4294841330 |
|      10 | 0x1513B     |       86331 |
|      11 | 0xFFFDEA8D  |  4294830733 |
|      12 | 0x043C      |        1084 |
|      13 | 0x14051     |       82001 |
|      14 | 0xFFFDEBA9  |  4294831017 |

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

### Event 894

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 897

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0003   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          32 00 80 1F 00  01 80 02 80 03 80 1F 01     2............
0010: 6F 00                                             o.              
```

#### Opcodes

```
  0: 0x0003 [0x32] ExtData[1]->MainSpeed = 12* * 0.1
  1: 0x0006 [0x1F] MOVE_ENTITY: EventEntity moves to X=76.176*, Z=-131.405*, Y=-5.999*
  2: 0x000E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0010 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0011 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0012   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:       32 04 80 1F 00 05  80 06 80 07 80 1F 01 6F    2............o
0020: 1E 5C 21 03 01 00                                 .\!...          
```

#### Opcodes

```
  0: 0x0012 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0015 [0x1F] MOVE_ENTITY: EventEntity moves to X=78.681*, Z=-133.613*, Y=-6.000*
  2: 0x001D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0020 [0x1E] EventEntity looks at Fari-Wari (ID: 16982364/0x0103215C) and starts talking
  5: 0x0025 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0026   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                   32 00  80 1F 00 08 80 09 80 07        2.........
0030: 80 1F 01 6F 00                                    ...o.           
```

#### Opcodes

```
  0: 0x0026 [0x32] ExtData[1]->MainSpeed = 12* * 0.1
  1: 0x0029 [0x1F] MOVE_ENTITY: EventEntity moves to X=77.805*, Z=-125.966*, Y=-6.000*
  2: 0x0031 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0033 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0034 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 29 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                37 0A 80  0B 80 07 80 0C 80 32 00       7........2.
0040: 80 1F 00 0D 80 0E 80 03  80 1F 01 6F 1E 5C 21 03  ...........o.\!.
0050: 01 00                                             ..              
```

#### Opcodes

```
  0: 0x0035 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=86.331*, z=-136.563*, y=-6.000*, direction=95.3°*
  1: 0x003E [0x32] ExtData[1]->MainSpeed = 12* * 0.1
  2: 0x0041 [0x1F] MOVE_ENTITY: EventEntity moves to X=82.001*, Z=-136.279*, Y=-5.999*
  3: 0x0049 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x004B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x004C [0x1E] EventEntity looks at Fari-Wari (ID: 16982364/0x0103215C) and starts talking
  6: 0x0051 [0x00] END_REQSTACK()
```
