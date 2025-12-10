# 17203821 - Millechairale

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Jugner Forest (ID: 104) |
| Block Size       | 264 bytes               |
| Total Events     | 8                       |
| References Count | 13                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [18](#event-18)          | 0x0001       |     16 |              3 |
| [65535.1](#event-655351) | 0x0011       |     14 |              4 |
| [65535.2](#event-655352) | 0x001F       |     16 |              5 |
| [65535.3](#event-655353) | 0x002F       |     29 |              3 |
| [65535.4](#event-655354) | 0x004C       |     29 |              3 |
| [65535.5](#event-655355) | 0x0069       |     29 |              3 |
| [65535.6](#event-655356) | 0x0086       |     29 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFB4F89  |  4294659977 |
|       1 | 0x61FD1     |      401361 |
|       2 | 0x01CE      |         462 |
|       3 | 0x09F3      |        2547 |
|       4 | 0x000D      |          13 |
|       5 | 0xFFFB4BC7  |  4294659015 |
|       6 | 0x628DD     |      403677 |
|       7 | 0x017F      |         383 |
|       8 | 0x0028      |          40 |
|       9 | 0xFFFB3874  |  4294654068 |
|      10 | 0x6C47A     |      443514 |
|      11 | 0xFFFFFBB6  |  4294966198 |
|      12 | 0x0014      |          20 |

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

### Event 18

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 16 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    94 01 F8 FF FF 7F 37  00 80 01 80 02 80 03 80   ......7........
0010: 00                                                .               
```

#### Opcodes

```
  0: 0x0001 [0x94] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-307.319*, z=401.361*, y=0.462*, direction=223.9°*
  2: 0x0010 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0011   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:    32 04 80 1F 00 05 80  06 80 07 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x0011 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0014 [0x1F] MOVE_ENTITY: EventEntity moves to X=-308.281*, Z=403.677*, Y=0.383*
  2: 0x001C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x001E [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 16 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               32                 2
0020: 08 80 1F 00 09 80 0A 80  0B 80 1F 01 22 01 00     ............".. 
```

#### Opcodes

```
  0: 0x001F [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0022 [0x1F] MOVE_ENTITY: EventEntity moves to X=-313.228*, Z=443.514*, Y=-1.098*
  2: 0x002A [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002C [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  4: 0x002E [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x002F   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:                                               66                 f
0030: 0C 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 30 53 F8  ..........tlk0S.
0040: FF FF 7F F8 FF FF 7F 74  6C 6B 30 00              .......tlk0.    
```

#### Opcodes

```
  0: 0x002F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  1: 0x003E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  2: 0x004B [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004C   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                      66 0C 80 F8              f...
0050: FF FF 7F F8 FF FF 7F 74  6C 6B 31 53 F8 FF FF 7F  .......tlk1S....
0060: F8 FF FF 7F 74 6C 6B 31  00                       ....tlk1.       
```

#### Opcodes

```
  0: 0x004C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=20*
  1: 0x005B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  2: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             66 0C 80 F8 FF FF 7F           f......
0070: F8 FF FF 7F 74 68 6B 31  53 F8 FF FF 7F F8 FF FF  ....thk1S.......
0080: 7F 74 68 6B 31 00                                 .thk1.          
```

#### Opcodes

```
  0: 0x0069 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=20*
  1: 0x0078 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  2: 0x0085 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0086   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0080:                   66 0C  80 F8 FF FF 7F F8 FF FF        f.........
0090: 7F 74 68 6B 32 53 F8 FF  FF 7F F8 FF FF 7F 74 68  .thk2S........th
00A0: 6B 32 00                                          k2.             
```

#### Opcodes

```
  0: 0x0086 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=20*
  1: 0x0095 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  2: 0x00A2 [0x00] END_REQSTACK()
```
