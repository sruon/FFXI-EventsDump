# 17383486 - Raptorlegs Gedwad

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Qulun Dome (ID: 148) |
| Block Size       | 228 bytes            |
| Total Events     | 7                    |
| References Count | 22                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [60](#event-60)          | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     15 |              5 |
| [65535.2](#event-655352) | 0x001A       |     34 |              8 |
| [65535.3](#event-655353) | 0x003C       |     14 |              4 |
| [61](#event-61)          | 0x004A       |     10 |              2 |
| [65](#event-65)          | 0x0054       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x6246      |       25158 |
|       1 | 0xEDA7      |       60839 |
|       2 | 0x5D3F      |       23871 |
|       3 | 0x0009      |           9 |
|       4 | 0x0028      |          40 |
|       5 | 0x3A90      |       14992 |
|       6 | 0xEFEA      |       61418 |
|       7 | 0x5D1D      |       23837 |
|       8 | 0x000D      |          13 |
|       9 | 0x366D      |       13933 |
|      10 | 0xE8C6      |       59590 |
|      11 | 0x5D2E      |       23854 |
|      12 | 0x33DE      |       13278 |
|      13 | 0xE72E      |       59182 |
|      14 | 0x5CF2      |       23794 |
|      15 | 0x2F8A      |       12170 |
|      16 | 0xE78C      |       59276 |
|      17 | 0x5CC0      |       23744 |
|      18 | 0x110C      |        4364 |
|      19 | 0xE6EC      |       59116 |
|      20 | 0x5DD0      |       24016 |
|      21 | 0x0800      |        2048 |

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

### Event 60

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
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=25.158*, z=60.839*, y=23.871*, direction=0.8°*
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
  0: 0x000B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=14.992*, Z=61.418*, Y=23.837*
  2: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0018 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 34 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                32 08 80 1F 00 09            2.....
0020: 80 0A 80 0B 80 1F 01 1F  00 0C 80 0D 80 0E 80 1F  ................
0030: 01 1F 00 0F 80 10 80 11  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x001A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x001D [0x1F] MOVE_ENTITY: EventEntity moves to X=13.933*, Z=59.590*, Y=23.854*
  2: 0x0025 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0027 [0x1F] MOVE_ENTITY: EventEntity moves to X=13.278*, Z=59.182*, Y=23.794*
  4: 0x002F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0031 [0x1F] MOVE_ENTITY: EventEntity moves to X=12.170*, Z=59.276*, Y=23.744*
  6: 0x0039 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      32 08 80 1F              2...
0040: 00 12 80 13 80 14 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x003C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003F [0x1F] MOVE_ENTITY: EventEntity moves to X=4.364*, Z=59.116*, Y=24.016*
  2: 0x0047 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0049 [0x00] END_REQSTACK()
```

### Event 61

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                37 05 80 06 80 07            7.....
0050: 80 15 80 00                                       ....            
```

#### Opcodes

```
  0: 0x004A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=14.992*, z=61.418*, y=23.837*, direction=180.0°*
  1: 0x0053 [0x00] END_REQSTACK()
```

### Event 65

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             37 05 80 06  80 07 80 15 80 00            7.........  
```

#### Opcodes

```
  0: 0x0054 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=14.992*, z=61.418*, y=23.837*, direction=180.0°*
  1: 0x005D [0x00] END_REQSTACK()
```
