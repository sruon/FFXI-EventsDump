# 17162756 - Shahr Yagenmhi

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Windurst Waters [S] (ID: 94) |
| Block Size       | 76 bytes                     |
| Total Events     | 5                            |
| References Count | 4                            |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [124](#event-124)        | 0x0001       |      1 |              1 |
| [125](#event-125)        | 0x0002       |      1 |              1 |
| [127](#event-127)        | 0x0003       |      1 |              1 |
| [65535.1](#event-655351) | 0x0004       |     20 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0x2048      |        8264 |
|       2 | 0xFFFD825C  |  4294804060 |
|       3 | 0xFFFFEF67  |  4294963047 |

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

### Event 124

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

### Event 125

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       00                                            .             
```

#### Opcodes

```
  0: 0x0002 [0x00] END_REQSTACK()
```

### Event 127

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0004   |
| Data Size    | 20 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             32 00 80 1F  00 01 80 02 80 03 80 1F      2...........
0010: 01 6F 1E F0 FF FF 7F 00                           .o......        
```

#### Opcodes

```
  0: 0x0004 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0007 [0x1F] MOVE_ENTITY: EventEntity moves to X=8.264*, Z=-163.236*, Y=-4.249*
  2: 0x000F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x0011 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x0012 [0x1E] EventEntity looks at LocalPlayer and starts talking
  5: 0x0017 [0x00] END_REQSTACK()
```
