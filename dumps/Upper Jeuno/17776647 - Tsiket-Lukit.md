# 17776647 - Tsiket-Lukit

## Common Data

| Field            | Value                 |
|------------------|-----------------------|
| Zone             | Upper Jeuno (ID: 244) |
| Block Size       | 176 bytes             |
| Total Events     | 6                     |
| References Count | 10                    |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      6 |              3 |
| [33](#event-33)          | 0x0006       |     10 |              2 |
| [65535.1](#event-655351) | 0x0010       |     11 |              3 |
| [65535.2](#event-655352) | 0x001B       |     29 |              3 |
| [65535.3](#event-655353) | 0x0038       |     29 |              3 |
| [65535.4](#event-655354) | 0x0055       |      9 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFFB74C  |  4294948684 |
|       2 | 0x11998     |       72088 |
|       3 | 0xFFFFE62E  |  4294960686 |
|       4 | 0x0951      |        2385 |
|       5 | 0xFFFFB910  |  4294949136 |
|       6 | 0x108FC     |       67836 |
|       7 | 0xFFFFE72A  |  4294960938 |
|       8 | 0x0031      |          49 |
|       9 | 0x003C      |          60 |

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 6 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 22 01 32 00 80 00                                 ".2...          
```

#### Opcodes

```
  0: 0x0000 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  1: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0005 [0x00] END_REQSTACK()
```

### Event 33

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0006   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   37 01  80 02 80 03 80 04 80 00        7.........
```

#### Opcodes

```
  0: 0x0006 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-18.612*, z=72.088*, y=-6.610*, direction=209.6°*
  1: 0x000F [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 11 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 1F 00 05 80 06 80 07 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x0010 [0x1F] MOVE_ENTITY: EventEntity moves to X=-18.160*, Z=67.836*, Y=-6.358*
  1: 0x0018 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  2: 0x001A [0x00] END_REQSTACK()
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
0020: FF 7F F8 FF FF 7F 74 6C  6B 30 53 F8 FF FF 7F F8  ......tlk0S.....
0030: FF FF 7F 74 6C 6B 30 00                           ...tlk0.        
```

#### Opcodes

```
  0: 0x001B [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=49*
  1: 0x002A [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
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
0040: FF FF 7F 74 6C 6B 31 53  F8 FF FF 7F F8 FF FF 7F  ...tlk1S........
0050: 74 6C 6B 31 00                                    tlk1.           
```

#### Opcodes

```
  0: 0x0038 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=49*
  1: 0x0047 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  2: 0x0054 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0055  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                5E 69 64  6C 30 1C 09 80 00             ^idl0....  
```

#### Opcodes

```
  0: 0x0055 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x005A [0x1C] WAIT(60* ticks)
  2: 0x005D [0x00] END_REQSTACK()
```
