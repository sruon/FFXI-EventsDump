# 17719614 - Hampu-Kampu

## Common Data

| Field            | Value                         |
|------------------|-------------------------------|
| Zone             | Southern San d'Oria (ID: 230) |
| Block Size       | 72 bytes                      |
| Total Events     | 3                             |
| References Count | 5                             |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [908](#event-908)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     21 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x06EE      |        1774 |
|       1 | 0x000D      |          13 |
|       2 | 0x24193     |      147859 |
|       3 | 0x3B77E     |      243582 |
|       4 | 0xFFFFE13E  |  4294959422 |

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

### Event 908

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
| Data Size    | 21 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       4B 3E 61 0E 01 00  80 32 01 80 1F 00 02 80    K>a....2......
0010: 03 80 04 80 1F 01 00                              .......         
```

#### Opcodes

```
  0: 0x0002 [0x4B] UPDATE_ENTITY_YAW(entity=Hampu-Kampu (ID: 17719614/0x010E613E), yaw=9.7°*)
  1: 0x0009 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x000C [0x1F] MOVE_ENTITY: EventEntity moves to X=147.859*, Z=243.582*, Y=-7.874*
  3: 0x0014 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0016 [0x00] END_REQSTACK()
```
