# 17850991 - Donda-Bonda

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Foret de Hennetiel (ID: 262) |
| Block Size       | 72 bytes                     |
| Total Events     | 3                            |
| References Count | 5                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [528](#event-528)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     22 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x6B42B     |      439339 |
|       2 | 0xFFFBC0F7  |  4294689015 |
|       3 | 0xFFFFF830  |  4294965296 |
|       4 | 0x001E      |          30 |

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

### Event 528

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
| Data Size    | 22 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       32 00 80 1F 00 01  80 02 80 03 80 1F 01 1E    2.............
0010: 6B 62 10 01 1C 04 80 00                           kb......        
```

#### Opcodes

```
  0: 0x0002 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0005 [0x1F] MOVE_ENTITY: EventEntity moves to X=439.339*, Z=-278.281*, Y=-2.000*
  2: 0x000D [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x000F [0x1E] EventEntity looks at Davengrot (ID: 17850987/0x0110626B) and starts talking
  4: 0x0014 [0x1C] WAIT(30* ticks)
  5: 0x0017 [0x00] END_REQSTACK()
```
