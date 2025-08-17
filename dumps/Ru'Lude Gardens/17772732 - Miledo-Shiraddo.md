# 17772732 - Miledo-Shiraddo

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ru'Lude Gardens (ID: 243) |
| Block Size       | 224 bytes                 |
| Total Events     | 5                         |
| References Count | 23                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [10070](#event-10070)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     28 |              6 |
| [65535.2](#event-655352) | 0x001E       |     28 |              6 |
| [65535.3](#event-655353) | 0x003A       |     38 |              8 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0324      |         804 |
|       1 | 0x4882      |       18562 |
|       2 | 0x0BB7      |        2999 |
|       3 | 0x0CD5      |        3285 |
|       4 | 0x0028      |          40 |
|       5 | 0x005F      |          95 |
|       6 | 0x11B4      |        4532 |
|       7 | 0x0274      |         628 |
|       8 | 0xFFFF942D  |  4294939693 |
|       9 | 0x2329      |        9001 |
|      10 | 0x02DE      |         734 |
|      11 | 0x2A6F      |       10863 |
|      12 | 0xFFFF3C65  |  4294917221 |
|      13 | 0x2327      |        8999 |
|      14 | 0x7AD4      |       31444 |
|      15 | 0xFFFF3421  |  4294915105 |
|      16 | 0x232B      |        9003 |
|      17 | 0x0065      |         101 |
|      18 | 0xB254      |       45652 |
|      19 | 0xFFFF263B  |  4294911547 |
|      20 | 0xB967      |       47463 |
|      21 | 0xFFFF0340  |  4294902592 |
|      22 | 0x270F      |        9999 |

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

### Event 10070

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
| Data Size    | 28 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       37 00 80 01 80 02  80 03 80 80 BC 30 0F 01    7..........0..
0010: 32 04 80 1F 00 05 80 06  80 02 80 1F 01 00        2.............  
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.804*, z=18.562*, y=2.999*, direction=288.7°*
  1: 0x000B [0x80] LOAD_WAIT(entity=Miledo-Shiraddo (ID: 17772732/0x010F30BC))
  2: 0x0010 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  3: 0x0013 [0x1F] MOVE_ENTITY: EventEntity moves to X=0.095*, Z=4.532*, Y=2.999*
  4: 0x001B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x001D [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001E   |
| Data Size    | 28 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                            37 07                7.
0020: 80 08 80 09 80 0A 80 80  BC 30 0F 01 32 04 80 1F  .........0..2...
0030: 00 0B 80 0C 80 0D 80 1F  01 00                    ..........      
```

#### Opcodes

```
  0: 0x001E [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=0.628*, z=-27.603*, y=9.001*, direction=64.5°*
  1: 0x0027 [0x80] LOAD_WAIT(entity=Miledo-Shiraddo (ID: 17772732/0x010F30BC))
  2: 0x002C [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  3: 0x002F [0x1F] MOVE_ENTITY: EventEntity moves to X=10.863*, Z=-50.075*, Y=8.999*
  4: 0x0037 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 38 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                37 0E 80 0F 80 10            7.....
0040: 80 11 80 80 BC 30 0F 01  32 04 80 1F 00 12 80 13  .....0..2.......
0050: 80 0D 80 1F 01 1F 00 14  80 15 80 16 80 1F 01 00  ................
```

#### Opcodes

```
  0: 0x003A [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=31.444*, z=-52.191*, y=9.003*, direction=8.9°*
  1: 0x0043 [0x80] LOAD_WAIT(entity=Miledo-Shiraddo (ID: 17772732/0x010F30BC))
  2: 0x0048 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  3: 0x004B [0x1F] MOVE_ENTITY: EventEntity moves to X=45.652*, Z=-55.749*, Y=8.999*
  4: 0x0053 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0055 [0x1F] MOVE_ENTITY: EventEntity moves to X=47.463*, Z=-64.704*, Y=9.999*
  6: 0x005D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  7: 0x005F [0x00] END_REQSTACK()
```
