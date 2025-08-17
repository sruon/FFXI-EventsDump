# 17347132 - Vauderame

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Horlais Peak (ID: 139) |
| Block Size       | 88 bytes               |
| Total Events     | 3                      |
| References Count | 8                      |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [32000](#event-32000)    | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     24 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0xFFFA058F  |  4294575503 |
|       1 | 0xFFFEE14E  |  4294893902 |
|       2 | 0x16F40     |       94016 |
|       3 | 0x0AE3      |        2787 |
|       4 | 0x0009      |           9 |
|       5 | 0xFFFA0256  |  4294574678 |
|       6 | 0xFFFEE97A  |  4294895994 |
|       7 | 0x16F9B     |       94107 |

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

### Event 32000

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
0000:       37 00 80 01 80 02  80 03 80 32 04 80 1F 00    7........2....
0010: 05 80 06 80 07 80 1F 01  6F 00                    ........o.      
```

#### Opcodes

```
  0: 0x0002 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-391.793*, z=-73.394*, y=94.016*, direction=244.9°*
  1: 0x000B [0x32] ExtData[1]->MainSpeed = 9* * 0.1
  2: 0x000E [0x1F] MOVE_ENTITY: EventEntity moves to X=-392.618*, Z=-71.302*, Y=94.107*
  3: 0x0016 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0018 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0019 [0x00] END_REQSTACK()
```
