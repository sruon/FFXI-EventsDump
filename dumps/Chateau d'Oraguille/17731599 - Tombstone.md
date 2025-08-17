# 17731599 - Tombstone

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Chateau d'Oraguille (ID: 233) |
| Block Size       | 128 bytes                     |
| Total Events     | 4                             |
| References Count | 7                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [83](#event-83)          | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     53 |              5 |
| [111](#event-111)        | 0x0037       |     10 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000F      |          15 |
|       1 | 0x0085      |         133 |
|       2 | 0x0000      |           0 |
|       3 | 0xFFFE86B2  |  4294870706 |
|       4 | 0x1252F     |       75055 |
|       5 | 0x018E      |         398 |
|       6 | 0x0EA0      |        3744 |

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

### Event 83

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
| Data Size    | 53 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1C 00 80 45 01 80  F0 FF FF 7F F0 FF FF 7F    ...E..........
0010: 73 67 30 38 02 80 55 01  80 F0 FF FF 7F F0 FF FF  sg08..U.........
0020: 7F 73 67 30 38 45 01 80  F0 FF FF 7F F0 FF FF 7F  .sg08E..........
0030: 73 67 31 30 02 80 00                              sg10...         
```

#### Opcodes

```
  0: 0x0002 [0x1C] WAIT(15* ticks)
  1: 0x0005 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "sg08" with entities [LocalPlayer, LocalPlayer], work=[133*, 0*]
  2: 0x0016 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "sg08" with entities [LocalPlayer, LocalPlayer], work=133*
  3: 0x0025 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "sg10" with entities [LocalPlayer, LocalPlayer], work=[133*, 0*]
  4: 0x0036 [0x00] END_REQSTACK()
```

### Event 111

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0037   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                      37  03 80 04 80 05 80 06 80         7........
0040: 00                                                .               
```

#### Opcodes

```
  0: 0x0037 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-96.590*, z=75.055*, y=0.398*, direction=329.1°*
  1: 0x0040 [0x00] END_REQSTACK()
```
