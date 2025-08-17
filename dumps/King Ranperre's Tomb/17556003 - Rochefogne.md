# 17556003 - Rochefogne

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | King Ranperre's Tomb (ID: 190) |
| Block Size       | 388 bytes                      |
| Total Events     | 12                             |
| References Count | 29                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [14](#event-14)          | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     15 |              5 |
| [65535.2](#event-655352) | 0x001A       |     15 |              5 |
| [65535.3](#event-655353) | 0x0029       |     11 |              3 |
| [8](#event-8)            | 0x0034       |     38 |              4 |
| [65535.4](#event-655354) | 0x005A       |     14 |              4 |
| [65535.5](#event-655355) | 0x0068       |     11 |              3 |
| [65535.6](#event-655356) | 0x0073       |     38 |              6 |
| [65535.7](#event-655357) | 0x0099       |     29 |              3 |
| [65535.8](#event-655358) | 0x00B6       |     12 |              4 |
| [65535.9](#event-655359) | 0x00C2       |     11 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFF7F0F  |  4294934287 |
|       1 | 0x5B84      |       23428 |
|       2 | 0x1CD1      |        7377 |
|       3 | 0x061D      |        1565 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFF77F0  |  4294932464 |
|       6 | 0x5438      |       21560 |
|       7 | 0x1D4B      |        7499 |
|       8 | 0xFFFF5E7B  |  4294925947 |
|       9 | 0x5248      |       21064 |
|      10 | 0x1F3F      |        7999 |
|      11 | 0xFFFEF714  |  4294899476 |
|      12 | 0x5633      |       22067 |
|      13 | 0x2327      |        8999 |
|      14 | 0x0613      |        1555 |
|      15 | 0xFFFF1797  |  4294907799 |
|      16 | 0x4DFC      |       19964 |
|      17 | 0x080A      |        2058 |
|      18 | 0x0014      |          20 |
|      19 | 0xFFFF0652  |  4294903378 |
|      20 | 0xFFFEF0D8  |  4294897880 |
|      21 | 0x4E81      |       20097 |
|      22 | 0xFFFEE62B  |  4294895147 |
|      23 | 0x4EA3      |       20131 |
|      24 | 0x222E      |        8750 |
|      25 | 0x0000      |           0 |
|      26 | 0x003C      |          60 |
|      27 | 0xFFFF0B9B  |  4294904731 |
|      28 | 0x4E04      |       19972 |

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

### Event 14

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    37 00 80 01 80 02 80  03 80 00                  7.........     
```

#### Opcodes

```
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-33.009*, z=23.428*, y=7.377*, direction=137.5°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   32 04 80 1F 00             2....
0010: 05 80 06 80 07 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x000B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=-34.832*, Z=21.560*, Y=7.499*
  2: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0018 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                32 04 80 1F 00 08            2.....
0020: 80 09 80 0A 80 1F 01 6F  00                       .......o.       
```

#### Opcodes

```
  0: 0x001A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001D [0x1F] MOVE_ENTITY: EventEntity moves to X=-41.349*, Z=21.064*, Y=7.999*
  2: 0x0025 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0027 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0028 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0029   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                             84 37 0B 80 0C 80 0D           .7.....
0030: 80 0E 80 00                                       ....            
```

#### Opcodes

```
  0: 0x0029 [0x84] ADJUST_RENDER_FLAGS3_BIT0()
  1: 0x002A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-67.820*, z=22.067*, y=8.999*, direction=136.7°*
  2: 0x0033 [0x00] END_REQSTACK()
```

### Event 8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0034   |
| Data Size    | 38 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:             37 0F 80 10  80 0D 80 11 80 66 12 80      7........f..
0040: F8 FF FF 7F F8 FF FF 7F  00 FE FE FE 53 F8 FF FF  ............S...
0050: 7F F8 FF FF 7F 00 FE FE  FE 00                    ..........      
```

#### Opcodes

```
  0: 0x0034 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-59.497*, z=19.964*, y=8.999*, direction=180.9°*
  1: 0x003D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler 0xFEFEFE00 with entities [EventEntity, EventEntity], work=20*
  2: 0x004C [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler 0xFEFEFE00 with entities [EventEntity, EventEntity]
  3: 0x0059 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                32 04 80 1F 00 13            2.....
0060: 80 10 80 0D 80 1F 01 00                           ........        
```

#### Opcodes

```
  0: 0x005A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005D [0x1F] MOVE_ENTITY: EventEntity moves to X=-63.918*, Z=19.964*, Y=8.999*
  2: 0x0065 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0067 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0068   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                          1F 00 14 80 15 80 0D 80          ........
0070: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x0068 [0x1F] MOVE_ENTITY: EventEntity moves to X=-69.416*, Z=20.097*, Y=8.999*
  1: 0x0070 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0072 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0073   |
| Data Size    | 38 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:          1F 00 16 80 17  80 18 80 1F 01 6F 2C F8     ..........o,.
0080: FF FF 7F F8 FF FF 7F 72  65 73 30 53 F8 FF FF 7F  .......res0S....
0090: F8 FF FF 7F 72 65 73 30  00                       ....res0.       
```

#### Opcodes

```
  0: 0x0073 [0x1F] MOVE_ENTITY: EventEntity moves to X=-72.149*, Z=20.131*, Y=8.750*
  1: 0x007B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x007D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x007E [0x2C] CREATE_SCHEDULER_TASK: Create scheduler "res0" with entities [EventEntity, EventEntity]
  4: 0x008B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "res0" with entities [EventEntity, EventEntity]
  5: 0x0098 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0099   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                             66 12 80 F8 FF FF 7F           f......
00A0: F8 FF FF 7F 70 61 73 30  53 F8 FF FF 7F F8 FF FF  ....pas0S.......
00B0: 7F 70 61 73 30 00                                 .pas0.          
```

#### Opcodes

```
  0: 0x0099 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=20*
  1: 0x00A8 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  2: 0x00B5 [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00B6   |
| Data Size    | 12 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00B0:                   7B F8  FF FF 7F 39 19 80 1C 1A        {....9....
00C0: 80 00                                             ..              
```

#### Opcodes

```
  0: 0x00B6 [0x7B] EventEntity stops talking
  1: 0x00BB [0x39] SET_ENTITY_DIRECTION(direction=0.0°*)
  2: 0x00BE [0x1C] WAIT(60* ticks)
  3: 0x00C1 [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x00C2   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:       1F 00 1B 80 1C 80  0D 80 1F 01 00             ...........   
```

#### Opcodes

```
  0: 0x00C2 [0x1F] MOVE_ENTITY: EventEntity moves to X=-62.565*, Z=19.972*, Y=8.999*
  1: 0x00CA [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x00CC [0x00] END_REQSTACK()
```
