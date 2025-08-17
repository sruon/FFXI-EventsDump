# 17101376 - Automaton

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Caedarva Mire (ID: 79) |
| Block Size       | 200 bytes              |
| Total Events     | 8                      |
| References Count | 20                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [15](#event-15)          | 0x0001       |      1 |              1 |
| [14](#event-14)          | 0x0002       |     10 |              2 |
| [65535.1](#event-655351) | 0x000C       |     14 |              4 |
| [65535.2](#event-655352) | 0x001A       |     10 |              2 |
| [65535.3](#event-655353) | 0x0024       |     11 |              3 |
| [65535.4](#event-655354) | 0x002F       |     11 |              3 |
| [65535.5](#event-655355) | 0x003A       |     11 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x23BCE     |      146382 |
|       1 | 0xFFF67347  |  4294341447 |
|       2 | 0x0123      |         291 |
|       3 | 0x070D      |        1805 |
|       4 | 0x000D      |          13 |
|       5 | 0x23864     |      145508 |
|       6 | 0xFFF67326  |  4294341414 |
|       7 | 0x00B6      |         182 |
|       8 | 0x200A7     |      131239 |
|       9 | 0xFFF667BD  |  4294338493 |
|      10 | 0x0505      |        1285 |
|      11 | 0x05D0      |        1488 |
|      12 | 0x22846     |      141382 |
|      13 | 0xFFF671AD  |  4294341037 |
|      14 | 0x0000      |           0 |
|      15 | 0x2183E     |      137278 |
|      16 | 0xFFF66821  |  4294338593 |
|      17 | 0x019A      |         410 |
|      18 | 0x227F7     |      141303 |
|      19 | 0xFFF66F22  |  4294340386 |

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

### Event 15

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

### Event 14

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
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=146.382*, z=-625.849*, y=0.291*, direction=158.6°*
  1: 0x000B [0x00] END_REQSTACK()
```

### Event 65535.1

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
0010: 00 05 80 06 80 07 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x000C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000F [0x1F] MOVE_ENTITY: EventEntity moves to X=145.508*, Z=-625.882*, Y=0.182*
  2: 0x0017 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0019 [0x00] END_REQSTACK()
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
0010:                                37 08 80 09 80 0A            7.....
0020: 80 0B 80 00                                       ....            
```

#### Opcodes

```
  0: 0x001A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=131.239*, z=-628.803*, y=1.285*, direction=130.8°*
  1: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             1F 00 0C 80  0D 80 0E 80 1F 01 00         ........... 
```

#### Opcodes

```
  0: 0x0024 [0x1F] MOVE_ENTITY: EventEntity moves to X=141.382*, Z=-626.259*, Y=0.000*
  1: 0x002C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               1F                 .
0030: 00 0F 80 10 80 11 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x002F [0x1F] MOVE_ENTITY: EventEntity moves to X=137.278*, Z=-628.703*, Y=0.410*
  1: 0x0037 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                1F 00 12 80 13 80            ......
0040: 0E 80 1F 01 00                                    .....           
```

#### Opcodes

```
  0: 0x003A [0x1F] MOVE_ENTITY: EventEntity moves to X=141.303*, Z=-626.910*, Y=0.000*
  1: 0x0042 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0044 [0x00] END_REQSTACK()
```
