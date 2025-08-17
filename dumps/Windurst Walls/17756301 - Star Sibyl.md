# 17756301 - Star Sibyl

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Windurst Walls (ID: 239) |
| Block Size       | 308 bytes                |
| Total Events     | 12                       |
| References Count | 30                       |

## List of Events

| Event ID                   | Entrypoint   |   Size |   Instructions |
|----------------------------|--------------|--------|----------------|
| [65535](#event-65535)      | 0x0000       |      1 |              1 |
| [443](#event-443)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351)   | 0x0002       |     10 |              2 |
| [65535.2](#event-655352)   | 0x000C       |     14 |              4 |
| [65535.3](#event-655353)   | 0x001A       |     10 |              2 |
| [65535.4](#event-655354)   | 0x0024       |     24 |              6 |
| [65535.5](#event-655355)   | 0x003C       |     10 |              2 |
| [65535.6](#event-655356)   | 0x0046       |     14 |              4 |
| [65535.7](#event-655357)   | 0x0054       |     10 |              2 |
| [65535.8](#event-655358)   | 0x005E       |     14 |              4 |
| [65535.9](#event-655359)   | 0x006C       |     10 |              4 |
| [65535.10](#event-6553510) | 0x0076       |      5 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x012C      |         300 |
|       1 | 0x20EE0     |      134880 |
|       2 | 0xFFFFBE93  |  4294950547 |
|       3 | 0x0400      |        1024 |
|       4 | 0x000D      |          13 |
|       5 | 0x1E3E8     |      123880 |
|       6 | 0xFFFFE2B8  |  4294959800 |
|       7 | 0x1F686     |      128646 |
|       8 | 0xFFFFC180  |  4294951296 |
|       9 | 0x0735      |        1845 |
|      10 | 0xFFFFC914  |  4294953236 |
|      11 | 0x1F00A     |      126986 |
|      12 | 0xFFFFA620  |  4294944288 |
|      13 | 0x2048F     |      132239 |
|      14 | 0xFFFF6B05  |  4294929157 |
|      15 | 0x20BD2     |      134098 |
|      16 | 0x068F      |        1679 |
|      17 | 0xFFFF34F1  |  4294915313 |
|      18 | 0x1EE7C     |      126588 |
|      19 | 0xFFFFCB44  |  4294953796 |
|      20 | 0xFFFEB177  |  4294881655 |
|      21 | 0x1C9A0     |      117152 |
|      22 | 0xFFFFE423  |  4294960163 |
|      23 | 0x0B96      |        2966 |
|      24 | 0xFFFEB22A  |  4294881834 |
|      25 | 0x1D92F     |      121135 |
|      26 | 0xFFFFE94E  |  4294961486 |
|      27 | 0x0050      |          80 |
|      28 | 0x2366      |        9062 |
|      29 | 0x2367      |        9063 |

## String References

- **9062**: d $3TThose who found the light again were those who knew themselves. Those who knew courage. Those who knew justice. Those who knew truth.
- **9063**: R $3TAnd then there came one whose determination would create a new future. That radiance would be as a beacon for all that lay ahead.

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

### Event 443

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

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 00                7.........    
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.300*, z=134.880*, y=-16.749*, direction=90.0°*
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000C   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                      32 04 80 1F              2...
0010: 00 00 80 05 80 02 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x000C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=0.300*, Z=123.880*, Y=-16.749*
  2: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                37 06 80 07 80 08            7.....
0020: 80 09 80 00                                       ....            
```

#### Opcodes

```
  0: 0x001A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-7.496*, z=128.646*, y=-16.000*, direction=162.2°*
  1: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             32 04 80 1F  00 0A 80 0B 80 08 80 1F      2...........
0030: 01 1F 00 0C 80 0D 80 08  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x0024 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0027 [0x1F] MOVE_ENTITY: EventEntity moves to X=-14.060*, Z=126.986*, Y=-16.000*
  2: 0x002F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0031 [0x1F] MOVE_ENTITY: EventEntity moves to X=-23.008*, Z=132.239*, Y=-16.000*
  4: 0x0039 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      37 0E 80 0F              7...
0040: 80 08 80 10 80 00                                 ......          
```

#### Opcodes

```
  0: 0x003C [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-38.139*, z=134.098*, y=-16.000*, direction=147.6°*
  1: 0x0045 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0046   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                   32 04  80 5A 00 11 80 12 80 13        2..Z......
0050: 80 5A 01 00                                       .Z..            
```

#### Opcodes

```
  0: 0x0046 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0049 [0x5A] UPDATE_EVENT_POSITION: Set EventEntity MovePosition to X=-51.983*, Z=126.588*, Y=-13.500*
  2: 0x0051 [0x5A] UPDATE_EVENT_POSITION: Move EventEntity incrementally towards MovePosition
  3: 0x0053 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0054   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:             37 14 80 15  80 16 80 17 80 00            7.........  
```

#### Opcodes

```
  0: 0x0054 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-85.641*, z=117.152*, y=-7.133*, direction=260.7°*
  1: 0x005D [0x00] END_REQSTACK()
```

### Event 65535.8

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005E   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                            32 04                2.
0060: 80 1F 00 18 80 19 80 1A  80 1F 01 00              ............    
```

#### Opcodes

```
  0: 0x005E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0061 [0x1F] MOVE_ENTITY: EventEntity moves to X=-85.462*, Z=121.135*, Y=-5.810*
  2: 0x0069 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x006B [0x00] END_REQSTACK()
```

### Event 65535.9

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x006C   |
| Data Size    | 10 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                                      67 1B 80 1B              g...
0070: 80 48 1C 80 23 00                                 .H..#.          
```

#### Opcodes

```
  0: 0x006C [0x67] HIDE_HUD_ELEMENTS(param1=0x801B, param2=0x801B)
  1: 0x0071 [0x48] [System] [9062*]:
    → "d $3TThose who found the light again were those who knew themselves. Those who knew courage. Those who knew justice. Those who knew truth."
  2: 0x0074 [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x0075 [0x00] END_REQSTACK()
```

### Event 65535.10

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0076  |
| Data Size    | 5 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                   48 1D  80 23 00                       H..#.     
```

#### Opcodes

```
  0: 0x0076 [0x48] [System] [9063*]:
    → "R $3TAnd then there came one whose determination would create a new future. That radiance would be as a beacon for all that lay ahead."
  1: 0x0079 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x007A [0x00] END_REQSTACK()
```
