# 17207833 - Coteaulepoint

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Batallia Downs (ID: 105) |
| Block Size       | 224 bytes                |
| Total Events     | 6                        |
| References Count | 16                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [904](#event-904)        | 0x0001       |     10 |              2 |
| [65535.1](#event-655351) | 0x000B       |     25 |              7 |
| [65535.2](#event-655352) | 0x0024       |     24 |              7 |
| [65535.3](#event-655353) | 0x003C       |     29 |              3 |
| [65535.4](#event-655354) | 0x0059       |     29 |              3 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x340DF     |      213215 |
|       1 | 0xFFF6BA95  |  4294359701 |
|       2 | 0x3D66      |       15718 |
|       3 | 0x0AB6      |        2742 |
|       4 | 0x000D      |          13 |
|       5 | 0x33BAD     |      211885 |
|       6 | 0xFFF6C175  |  4294361461 |
|       7 | 0x3A12      |       14866 |
|       8 | 0x33D14     |      212244 |
|       9 | 0xFFF6C812  |  4294363154 |
|      10 | 0x371F      |       14111 |
|      11 | 0x000A      |          10 |
|      12 | 0x31CC6     |      203974 |
|      13 | 0xFFF70115  |  4294377749 |
|      14 | 0x3D4A      |       15690 |
|      15 | 0x001D      |          29 |

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

### Event 904

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
  0: 0x0001 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=213.215*, z=-607.595*, y=15.718*, direction=241.0°*
  1: 0x000A [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000B   |
| Data Size    | 25 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                   32 04 80 1F 00             2....
0010: 05 80 06 80 07 80 1F 01  1F 00 08 80 09 80 0A 80  ................
0020: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x000B [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=211.885*, Z=-605.835*, Y=14.866*
  2: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0018 [0x1F] MOVE_ENTITY: EventEntity moves to X=212.244*, Z=-604.142*, Y=14.111*
  4: 0x0020 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0022 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  6: 0x0023 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0024   |
| Data Size    | 24 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             7B F8 FF FF  7F 1C 0B 80 32 04 80 1F      {.......2...
0030: 00 0C 80 0D 80 0E 80 1F  01 22 01 00              ........."..    
```

#### Opcodes

```
  0: 0x0024 [0x7B] EventEntity stops talking
  1: 0x0029 [0x1C] WAIT(10* ticks)
  2: 0x002C [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  3: 0x002F [0x1F] MOVE_ENTITY: EventEntity moves to X=203.974*, Z=-589.547*, Y=15.690*
  4: 0x0037 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  5: 0x0039 [0x22] ENTITY_HIDE_FLAG(enabled=0x01)
  6: 0x003B [0x00] END_REQSTACK()
```

### Event 65535.3

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x003C   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                                      66 0F 80 F8              f...
0040: FF FF 7F F8 FF FF 7F 74  6C 6B 30 53 F8 FF FF 7F  .......tlk0S....
0050: F8 FF FF 7F 74 6C 6B 30  00                       ....tlk0.       
```

#### Opcodes

```
  0: 0x003C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=29*
  1: 0x004B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
  2: 0x0058 [0x00] END_REQSTACK()
```

### Event 65535.4

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0059   |
| Data Size    | 29 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0050:                             66 0F 80 F8 FF FF 7F           f......
0060: F8 FF FF 7F 74 6C 6B 31  53 F8 FF FF 7F F8 FF FF  ....tlk1S.......
0070: 7F 74 6C 6B 31 00                                 .tlk1.          
```

#### Opcodes

```
  0: 0x0059 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=29*
  1: 0x0068 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk1" with entities [EventEntity, EventEntity]
  2: 0x0075 [0x00] END_REQSTACK()
```
