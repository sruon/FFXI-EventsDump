# 17780746 - Paya-Sabya

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Lower Jeuno (ID: 245) |
| Block Size       | 328 bytes             |
| Total Events     | 9                     |
| References Count | 25                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [111](#event-111)        | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     43 |             11 |
| [65535.2](#event-655352) | 0x0036       |     33 |              8 |
| [65535.3](#event-655353) | 0x0057       |     12 |              3 |
| [65535.4](#event-655354) | 0x0063       |     18 |              6 |
| [65535.5](#event-655355) | 0x0075       |     19 |              3 |
| [65535.6](#event-655356) | 0x0088       |     29 |              3 |
| [65535.7](#event-655357) | 0x00A5       |      9 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x5081      |       20609 |
|       1 | 0xFFFF382E  |  4294916142 |
|       2 | 0x0F3D      |        3901 |
|       3 | 0x084F      |        2127 |
|       4 | 0x0078      |         120 |
|       5 | 0x0028      |          40 |
|       6 | 0x4A81      |       19073 |
|       7 | 0xFFFF37C8  |  4294916040 |
|       8 | 0x465A      |       18010 |
|       9 | 0xFFFF3036  |  4294914102 |
|      10 | 0x0F3B      |        3899 |
|      11 | 0x4C0A      |       19466 |
|      12 | 0xFFFF2339  |  4294910777 |
|      13 | 0x0F1D      |        3869 |
|      14 | 0x1A78      |        6776 |
|      15 | 0x10D91     |       69009 |
|      16 | 0x07D0      |        2000 |
|      17 | 0x0F10      |        3856 |
|      18 | 0x2E21      |       11809 |
|      19 | 0x1154B     |       70987 |
|      20 | 0x07CF      |        1999 |
|      21 | 0x027E      |         638 |
|      22 | 0x0055      |          85 |
|      23 | 0x001E      |          30 |
|      24 | 0x003C      |          60 |

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

### Event 111

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
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=20.609*, z=-51.154*, y=3.901*, direction=186.9°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 43 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   1C 04 80 32 05             ...2.
0010: 80 1F 00 06 80 07 80 02  80 1F 01 1F 00 08 80 09  ................
0020: 80 0A 80 1F 01 1F 00 0B  80 0C 80 0D 80 1F 01 6F  ...............o
0030: 1E 07 50 0F 01 00                                 ..P...          
```

#### Opcodes

```
  0: 0x000B [0x1C] WAIT(120* ticks)
  1: 0x000E [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  2: 0x0011 [0x1F] MOVE_ENTITY: EventEntity moves to X=19.073*, Z=-51.256*, Y=3.901*
  3: 0x0019 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x001B [0x1F] MOVE_ENTITY: EventEntity moves to X=18.010*, Z=-53.194*, Y=3.899*
  5: 0x0023 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0025 [0x1F] MOVE_ENTITY: EventEntity moves to X=19.466*, Z=-56.519*, Y=3.869*
  7: 0x002D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x002F [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  9: 0x0030 [0x1E] EventEntity looks at Aldo (ID: 17780743/0x010F5007) and starts talking
 10: 0x0035 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0036   |
| Data Size    | 33 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                   1F 00  08 80 09 80 0A 80 1F 01        ..........
0040: 1F 00 06 80 07 80 02 80  1F 01 1F 00 00 80 01 80  ................
0050: 02 80 1F 01 22 01 00                              ...."..         
```

#### Opcodes

```
  0: 0x0036 [0x1F] MOVE_ENTITY: EventEntity moves to X=18.010*, Z=-53.194*, Y=3.899*
  1: 0x003E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x0040 [0x1F] MOVE_ENTITY: EventEntity moves to X=19.073*, Z=-51.256*, Y=3.901*
  3: 0x0048 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x004A [0x1F] MOVE_ENTITY: EventEntity moves to X=20.609*, Z=-51.154*, Y=3.901*
  5: 0x0052 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0054 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  7: 0x0056 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0057   |
| Data Size    | 12 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                      22  00 37 0E 80 0F 80 10 80         ".7......
0060: 11 80 00                                          ...             
```

#### Opcodes

```
  0: 0x0057 [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x0059 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=6.776*, z=69.009*, y=2.000*, direction=338.9°*
  2: 0x0062 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0063   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:          32 05 80 1F 00  12 80 13 80 14 80 1F 01     2............
0070: 6F 39 15 80 00                                    o9...           
```

#### Opcodes

```
  0: 0x0063 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0066 [0x1F] MOVE_ENTITY: EventEntity moves to X=11.809*, Z=70.987*, Y=1.999*
  2: 0x006E [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0070 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0071 [0x39] SET_ENTITY_DIRECTION(direction=3.5°*)
  5: 0x0074 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0075   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                5B 16 80  F8 FF FF 7F F8 FF FF 7F       [..........
0080: 74 6C 6B 30 1C 17 80 00                           tlk0....        
```

#### Opcodes

```
  0: 0x0075 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=85*
  1: 0x0084 [0x1C] WAIT(30* ticks)
  2: 0x0087 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0088   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                          5B 16 80 F8 FF FF 7F F8          [.......
0090: FF FF 7F 70 61 73 30 53  F8 FF FF 7F F8 FF FF 7F  ...pas0S........
00A0: 70 61 73 30 00                                    pas0.           
```

#### Opcodes

```
  0: 0x0088 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "pas0" with entities [EventEntity, EventEntity], work=85*
  1: 0x0097 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "pas0" with entities [EventEntity, EventEntity]
  2: 0x00A4 [0x00] END_REQSTACK()
```

### Event 65535.7

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x00A5  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00A0:                5E 69 64  6C 30 1C 18 80 00             ^idl0....  
```

#### Opcodes

```
  0: 0x00A5 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x00AA [0x1C] WAIT(60* ticks)
  2: 0x00AD [0x00] END_REQSTACK()
```
