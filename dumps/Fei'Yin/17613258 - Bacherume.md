# 17613258 - Bacherume

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Fei'Yin (ID: 204) |
| Block Size       | 160 bytes         |
| Total Events     | 5                 |
| References Count | 9                 |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [23](#event-23)          | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     16 |              5 |
| [65535.2](#event-655352) | 0x001B       |     29 |              3 |
| [65535.3](#event-655353) | 0x0038       |     29 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFE7440  |  4294865984 |
|       1 | 0xFFFEB258  |  4294881880 |
|       2 | 0xFFFFC365  |  4294951781 |
|       3 | 0x0A42      |        2626 |
|       4 | 0x0028      |          40 |
|       5 | 0xFFFEE456  |  4294894678 |
|       6 | 0xFFFEFBBD  |  4294900669 |
|       7 | 0xFFFFC180  |  4294951296 |
|       8 | 0x0018      |          24 |

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
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-101.312*, z=-85.416*, y=-15.515*, direction=230.8°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 16 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   32 04 80 1F 00             2....
0010: 05 80 06 80 07 80 1F 01  22 01 00                 ........"..     
```

#### Opcodes

```
  0: 0x000B [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=-72.618*, Z=-66.627*, Y=-16.000*
  2: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0018 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  4: 0x001A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   66 08 80 F8 FF             f....
0020: FF 7F F8 FF FF 7F 31 72  64 79 53 F8 FF FF 7F F8  ......1rdyS.....
0030: FF FF 7F 31 72 64 79 00                           ...1rdy.        
```

#### Opcodes

```
  0: 0x001B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "1rdy" with entities [EventEntity, EventEntity], work=24*
  1: 0x002A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "1rdy" with entities [EventEntity, EventEntity]
  2: 0x0037 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0038   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                          66 08 80 F8 FF FF 7F F8          f.......
0040: FF FF 7F 31 72 74 6E 53  F8 FF FF 7F F8 FF FF 7F  ...1rtnS........
0050: 31 72 74 6E 00                                    1rtn.           
```

#### Opcodes

```
  0: 0x0038 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "1rtn" with entities [EventEntity, EventEntity], work=24*
  1: 0x0047 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "1rtn" with entities [EventEntity, EventEntity]
  2: 0x0054 [0x00] END_REQSTACK()
```
