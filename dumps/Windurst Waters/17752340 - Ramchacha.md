# 17752340 - Ramchacha

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Windurst Waters (ID: 238) |
| Block Size       | 72 bytes                  |
| Total Events     | 3                         |
| References Count | 4                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [977](#event-977)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     24 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFFF89B  |  4294965403 |
|       2 | 0xFFFD7D59  |  4294802777 |
|       3 | 0xFFFFF061  |  4294963297 |

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

### Event 977

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
| Data Size    | 24 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1E F0 FF FF 7F 32  00 80 1F 00 01 80 02 80    .....2........
0010: 03 80 1F 01 1E F0 FF FF  7F 00                    ..........      
```

#### Opcodes

```
  0: 0x0002 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0007 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x000A [0x1F] MOVE_ENTITY: EventEntity moves to X=-1.893*, Z=-164.519*, Y=-3.999*
  3: 0x0012 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0014 [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x0019 [0x00] END_REQSTACK()
```
