# 17739937 - Valeriano

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Bastok Markets (ID: 235) |
| Block Size       | 112 bytes                |
| Total Events     | 4                        |
| References Count | 8                        |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [490](#event-490)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     31 |              7 |
| [65535.2](#event-655352) | 0x0021       |     14 |              4 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFEC6F2  |  4294887154 |
|       2 | 0xFFFDFF40  |  4294836032 |
|       3 | 0xFFFFED0F  |  4294962447 |
|       4 | 0x001E      |          30 |
|       5 | 0xFFFEC760  |  4294887264 |
|       6 | 0xFFFE1070  |  4294840432 |
|       7 | 0xFFFFEEB7  |  4294962871 |

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

### Event 490

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
| Data Size    | 31 bytes |
| Instructions | 7        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 4A    2............J
0010: F0 FF FF 7F A1 B0 0E 01  1E 20 B0 0E 01 1C 04 80  ......... ......
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=-80.142*, Z=-131.264*, Y=-4.849*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x4A] LocalPlayer looks at Valeriano (ID: 17739937/0x010EB0A1)
  4: 0x0018 [0x1E] EventEntity looks at Harmodios (ID: 17739808/0x010EB020) and starts talking
  5: 0x001D [0x1C] WAIT(30* ticks)
  6: 0x0020 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 14 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    32 00 80 1F 00 05 80  06 80 07 80 1F 01 00      2............. 
```

#### Opcodes

```
  0: 0x0021 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0024 [0x1F] MOVE_ENTITY: EventEntity moves to X=-80.032*, Z=-126.864*, Y=-4.425*
  2: 0x002C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002E [0x00] END_REQSTACK()
```
