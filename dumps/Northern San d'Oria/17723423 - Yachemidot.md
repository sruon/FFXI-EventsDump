# 17723423 - Yachemidot

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Northern San d'Oria (ID: 231) |
| Block Size       | 240 bytes                     |
| Total Events     | 8                             |
| References Count | 13                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [62](#event-62)          | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     16 |              5 |
| [65535.2](#event-655352) | 0x001B       |     31 |              8 |
| [65535.3](#event-655353) | 0x003A       |     19 |              3 |
| [65535.4](#event-655354) | 0x004D       |      9 |              3 |
| [65535.5](#event-655355) | 0x0056       |     19 |              3 |
| [65535.6](#event-655356) | 0x0069       |     32 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1722A     |       94762 |
|       1 | 0x1C4AB     |      115883 |
|       2 | 0x0000      |           0 |
|       3 | 0x0016      |          22 |
|       4 | 0x000D      |          13 |
|       5 | 0x17A06     |       96774 |
|       6 | 0x1C34F     |      115535 |
|       7 | 0x18035     |       98357 |
|       8 | 0x1D1E9     |      119273 |
|       9 | 0x177AB     |       96171 |
|      10 | 0x1E279     |      123513 |
|      11 | 0x0014      |          20 |
|      12 | 0x003C      |          60 |

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

### Event 62

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
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=94.762*, z=115.883*, y=0.000*, direction=1.9°*
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
0000:                                   22 00 32 04 80             ".2..
0010: 1F 00 05 80 06 80 02 80  1F 01 00                 ...........     
```

#### Opcodes

```
  0: 0x000B [0x22] ENTITY_HIDE_FLAG(enabled=0x00)
  1: 0x000D [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0010 [0x1F] MOVE_ENTITY: EventEntity moves to X=96.774*, Z=115.535*, Y=0.000*
  3: 0x0018 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x001A [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001B   |
| Data Size    | 31 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                   7B F8 FF FF 7F             {....
0020: 32 04 80 1F 00 07 80 08  80 02 80 1F 01 1F 00 09  2...............
0030: 80 0A 80 02 80 1F 01 22  01 00                    ......."..      
```

#### Opcodes

```
  0: 0x001B [0x7B] EventEntity stops talking
  1: 0x0020 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0023 [0x1F] MOVE_ENTITY: EventEntity moves to X=98.357*, Z=119.273*, Y=0.000*
  3: 0x002B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x002D [0x1F] MOVE_ENTITY: EventEntity moves to X=96.171*, Z=123.513*, Y=0.000*
  5: 0x0035 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  6: 0x0037 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  7: 0x0039 [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003A   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                66 0B 80 F8 FF FF            f.....
0040: 7F F8 FF FF 7F 74 6C 6B  30 1C 0C 80 00           .....tlk0....   
```

#### Opcodes

```
  0: 0x003A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=20*
  1: 0x0049 [0x1C] WAIT(60* ticks)
  2: 0x004C [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x004D  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                         5E 69 64               ^id
0050: 6C 30 1C 0C 80 00                                 l0....          
```

#### Opcodes

```
  0: 0x004D [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
  1: 0x0052 [0x1C] WAIT(60* ticks)
  2: 0x0055 [0x00] END_REQSTACK()
```

### Event 65535.5

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0056   |
| Data Size    | 19 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                   66 0B  80 F8 FF FF 7F F8 FF FF        f.........
0060: 7F 74 68 6B 31 1C 0C 80  00                       .thk1....       
```

#### Opcodes

```
  0: 0x0056 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=20*
  1: 0x0065 [0x1C] WAIT(60* ticks)
  2: 0x0068 [0x00] END_REQSTACK()
```

### Event 65535.6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0069   |
| Data Size    | 32 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0060:                             53 F8 FF FF 7F F8 FF           S......
0070: FF 7F 74 68 6B 31 66 0B  80 F8 FF FF 7F F8 FF FF  ..thk1f.........
0080: 7F 74 68 6B 32 1C 0C 80  00                       .thk2....       
```

#### Opcodes

```
  0: 0x0069 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  1: 0x0076 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=20*
  2: 0x0085 [0x1C] WAIT(60* ticks)
  3: 0x0088 [0x00] END_REQSTACK()
```
