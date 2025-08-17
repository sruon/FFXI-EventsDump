# 17744025 - Viresefilant

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Port Bastok (ID: 236) |
| Block Size       | 180 bytes             |
| Total Events     | 5                     |
| References Count | 18                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [296](#event-296)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     24 |              6 |
| [65535.2](#event-655352) | 0x001A       |     10 |              2 |
| [65535.3](#event-655353) | 0x0024       |     34 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFE7190  |  4294865296 |
|       2 | 0x55F0      |       22000 |
|       3 | 0xFFFFF830  |  4294965296 |
|       4 | 0xFFFE61F0  |  4294861296 |
|       5 | 0xFFFE7D48  |  4294868296 |
|       6 | 0x7148      |       29000 |
|       7 | 0x1388      |        5000 |
|       8 | 0x03E8      |        1000 |
|       9 | 0x0028      |          40 |
|      10 | 0xFFFE79E1  |  4294867425 |
|      11 | 0xA969      |       43369 |
|      12 | 0x128A      |        4746 |
|      13 | 0xFFFE7C7B  |  4294868091 |
|      14 | 0xAF67      |       44903 |
|      15 | 0x1322      |        4898 |
|      16 | 0xFFFE9DB8  |  4294876600 |
|      17 | 0xB411      |       46097 |

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

### Event 296

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
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 1F    2.............
0010: 00 04 80 02 80 03 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=-102.000*, Z=22.000*, Y=-2.000*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=-106.000*, Z=22.000*, Y=-2.000*
  4: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                37 05 80 06 80 07            7.....
0020: 80 08 80 00                                       ....            
```

#### Opcodes

```
  0: 0x001A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-99.000*, z=29.000*, y=5.000*, direction=87.9°*
  1: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 34 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             32 09 80 1F  00 0A 80 0B 80 0C 80 1F      2...........
0030: 01 1F 00 0D 80 0E 80 0F  80 1F 01 1F 00 10 80 11  ................
0040: 80 0F 80 1F 01 00                                 ......          
```

#### Opcodes

```
  0: 0x0024 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0027 [0x1F] MOVE_ENTITY: EventEntity moves to X=-99.871*, Z=43.369*, Y=4.746*
  2: 0x002F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0031 [0x1F] MOVE_ENTITY: EventEntity moves to X=-99.205*, Z=44.903*, Y=4.898*
  4: 0x0039 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x003B [0x1F] MOVE_ENTITY: EventEntity moves to X=-90.696*, Z=46.097*, Y=4.898*
  6: 0x0043 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x0045 [0x00] END_REQSTACK()
```
