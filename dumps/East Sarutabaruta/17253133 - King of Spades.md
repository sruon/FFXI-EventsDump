# 17253133 - King of Spades

## Common Data

| Field            | Value                       |
|------------------|-----------------------------|
| Zone             | East Sarutabaruta (ID: 116) |
| Block Size       | 240 bytes                   |
| Total Events     | 8                           |
| References Count | 19                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [909](#event-909)        | 0x0001       |      7 |              2 |
| [910](#event-910)        | 0x0008       |      7 |              2 |
| [65535.1](#event-655351) | 0x000F       |     15 |              5 |
| [65535.2](#event-655352) | 0x001E       |     15 |              5 |
| [65535.3](#event-655353) | 0x002D       |     15 |              5 |
| [65535.4](#event-655354) | 0x003C       |     30 |              8 |
| [65535.5](#event-655355) | 0x005A       |     25 |              7 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x609DA     |      395738 |
|       2 | 0xACD0      |       44240 |
|       3 | 0xFFFFC198  |  4294951320 |
|       4 | 0x6013E     |      393534 |
|       5 | 0xB490      |       46224 |
|       6 | 0xFFFFC290  |  4294951568 |
|       7 | 0x60A6C     |      395884 |
|       8 | 0xB9EF      |       47599 |
|       9 | 0xFFFFC33C  |  4294951740 |
|      10 | 0x60421     |      394273 |
|      11 | 0xAB04      |       43780 |
|      12 | 0xFFFFC252  |  4294951506 |
|      13 | 0x6015E     |      393566 |
|      14 | 0x9E5C      |       40540 |
|      15 | 0xFFFFC2AA  |  4294951594 |
|      16 | 0x5F866     |      391270 |
|      17 | 0xA1EF      |       41455 |
|      18 | 0xFFFFC3CA  |  4294951882 |

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

### Event 909

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 910

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0008  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          92 01 F8 FF FF 7F 00             ....... 
```

#### Opcodes

```
  0: 0x0008 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x000E [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000F   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                               32                 2
0010: 00 80 1F 00 01 80 02 80  03 80 1F 01 6F 00        ............o.  
```

#### Opcodes

```
  0: 0x000F [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0012 [0x1F] MOVE_ENTITY: EventEntity moves to X=395.738*, Z=44.240*, Y=-15.976*
  2: 0x001A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001E   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            32 00                2.
0020: 80 1F 00 04 80 05 80 06  80 1F 01 6F 00           ...........o.   
```

#### Opcodes

```
  0: 0x001E [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0021 [0x1F] MOVE_ENTITY: EventEntity moves to X=393.534*, Z=46.224*, Y=-15.728*
  2: 0x0029 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x002C [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002D   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                         32 00 80               2..
0030: 1F 00 07 80 08 80 09 80  1F 01 6F 00              ..........o.    
```

#### Opcodes

```
  0: 0x002D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0030 [0x1F] MOVE_ENTITY: EventEntity moves to X=395.884*, Z=47.599*, Y=-15.556*
  2: 0x0038 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 30 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      32 00 80 1F              2...
0040: 00 0A 80 0B 80 0C 80 1F  01 6F 4A 0D 43 07 01 F0  .........oJ.C...
0050: FF FF 7F 6F 76 0D 43 07  01 00                    ...ov.C...      
```

#### Opcodes

```
  0: 0x003C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x003F [0x1F] MOVE_ENTITY: EventEntity moves to X=394.273*, Z=43.780*, Y=-15.790*
  2: 0x0047 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0049 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x004A [0x4A] King of Spades (ID: 17253133/0x0107430D) looks at LocalPlayer
  5: 0x0053 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0054 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until King of Spades (ID: 17253133/0x0107430D) Render.Flags0 and Render.Flags3 conditions are met
  7: 0x0059 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x005A   |
| Data Size    | 25 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                                32 00 80 1F 00 0D            2.....
0060: 80 0E 80 0F 80 1F 01 6F  1F 00 10 80 11 80 12 80  .......o........
0070: 1F 01 00                                          ...             
```

#### Opcodes

```
  0: 0x005A [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x005D [0x1F] MOVE_ENTITY: EventEntity moves to X=393.566*, Z=40.540*, Y=-15.702*
  2: 0x0065 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0067 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0068 [0x1F] MOVE_ENTITY: EventEntity moves to X=391.270*, Z=41.455*, Y=-15.414*
  5: 0x0070 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0072 [0x00] END_REQSTACK()
```
