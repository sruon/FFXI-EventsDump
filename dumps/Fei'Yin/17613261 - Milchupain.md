# 17613261 - Milchupain

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Fei'Yin (ID: 204) |
| Block Size       | 184 bytes         |
| Total Events     | 6                 |
| References Count | 11                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [23](#event-23)          | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     15 |              5 |
| [65535.2](#event-655352) | 0x001A       |     16 |              5 |
| [65535.3](#event-655353) | 0x002A       |     29 |              3 |
| [65535.4](#event-655354) | 0x0047       |     29 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFE4496  |  4294853782 |
|       1 | 0xFFFEDA17  |  4294892055 |
|       2 | 0xFFFFC3BF  |  4294951871 |
|       3 | 0x0204      |         516 |
|       4 | 0x0028      |          40 |
|       5 | 0xFFFE5461  |  4294857825 |
|       6 | 0xFFFEC9DB  |  4294887899 |
|       7 | 0xFFFDF902  |  4294834434 |
|       8 | 0xFFFF34E0  |  4294915296 |
|       9 | 0xFFFFC16B  |  4294951275 |
|      10 | 0x0018      |          24 |

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

### Event 23

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
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-113.514*, z=-75.241*, y=-15.425*, direction=45.4°*
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
0010: 05 80 06 80 02 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x000B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=-109.471*, Z=-79.397*, Y=-15.425*
  2: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0018 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0019 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001A   |
| Data Size    | 16 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                32 04 80 1F 00 07            2.....
0020: 80 08 80 09 80 1F 01 22  01 00                    ......."..      
```

#### Opcodes

```
  0: 0x001A [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x001D [0x1F] MOVE_ENTITY: EventEntity moves to X=-132.862*, Z=-52.000*, Y=-16.021*
  2: 0x0025 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0027 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  4: 0x0029 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002A   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                66 0A 80 F8 FF FF            f.....
0030: 7F F8 FF FF 7F 31 72 64  79 53 F8 FF FF 7F F8 FF  .....1rdyS......
0040: FF 7F 31 72 64 79 00                              ..1rdy.         
```

#### Opcodes

```
  0: 0x002A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "1rdy" with entities [EventEntity, EventEntity], work=24*
  1: 0x0039 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "1rdy" with entities [EventEntity, EventEntity]
  2: 0x0046 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0047   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                      66  0A 80 F8 FF FF 7F F8 FF         f........
0050: FF 7F 31 72 74 6E 53 F8  FF FF 7F F8 FF FF 7F 31  ..1rtnS........1
0060: 72 74 6E 00                                       rtn.            
```

#### Opcodes

```
  0: 0x0047 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "1rtn" with entities [EventEntity, EventEntity], work=24*
  1: 0x0056 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "1rtn" with entities [EventEntity, EventEntity]
  2: 0x0063 [0x00] END_REQSTACK()
```
