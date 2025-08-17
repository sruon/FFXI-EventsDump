# 16908455 - Justinius

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Sealion's Den (ID: 32) |
| Block Size       | 164 bytes              |
| Total Events     | 5                      |
| References Count | 16                     |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |     13 |              3 |
| [13](#event-13)          | 0x000D       |     10 |              2 |
| [17](#event-17)          | 0x0017       |     10 |              2 |
| [65535.1](#event-655351) | 0x0021       |     15 |              5 |
| [65535.2](#event-655352) | 0x0030       |     15 |              5 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x953EB     |      611307 |
|       1 | 0xBEF8A     |      782218 |
|       2 | 0x2053D     |      132413 |
|       3 | 0x040B      |        1035 |
|       4 | 0x95A57     |      612951 |
|       5 | 0xBEDA1     |      781729 |
|       6 | 0x205BA     |      132538 |
|       7 | 0x03BD      |         957 |
|       8 | 0x0028      |          40 |
|       9 | 0x96017     |      614423 |
|      10 | 0xBDE0C     |      777740 |
|      11 | 0x20627     |      132647 |
|      12 | 0x000D      |          13 |
|      13 | 0x95C5E     |      613470 |
|      14 | 0xBD399     |      775065 |
|      15 | 0x2066E     |      132718 |

## Events

### Event 65535

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0000   |
| Data Size    | 13 bytes |
| Instructions | 3        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 94 00 F8 FF FF 7F 92 01  F8 FF FF 7F 00           .............   
```

#### Opcodes

```
  0: 0x0000 [0x94] EventEntity->Render.Flags3 = Flags3  // No change (flag=0)
  1: 0x0006 [0x92] EventEntity->Render.Flags3 ^= 0x01
  2: 0x000C [0x00] END_REQSTACK()
```

### Event 13

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x000D   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         37 00 80               7..
0010: 01 80 02 80 03 80 00                              .......         
```

#### Opcodes

```
  0: 0x000D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=611.307*, z=782.218*, y=132.413*, direction=91.0°*
  1: 0x0016 [0x00] END_REQSTACK()
```

### Event 17

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0017   |
| Data Size    | 10 bytes |
| Instructions | 2        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                      37  04 80 05 80 06 80 07 80         7........
0020: 00                                                .               
```

#### Opcodes

```
  0: 0x0017 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=612.951*, z=781.729*, y=132.538*, direction=84.1°*
  1: 0x0020 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0021   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:    32 08 80 1F 00 09 80  0A 80 0B 80 1F 01 6F 00   2............o.
```

#### Opcodes

```
  0: 0x0021 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  1: 0x0024 [0x1F] MOVE_ENTITY: EventEntity moves to X=614.423*, Z=777.740*, Y=132.647*
  2: 0x002C [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x002E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x002F [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 32 0C 80 1F 00 0D 80 0E  80 0F 80 1F 01 6F 00     2............o. 
```

#### Opcodes

```
  0: 0x0030 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  1: 0x0033 [0x1F] MOVE_ENTITY: EventEntity moves to X=613.470*, Z=775.065*, Y=132.718*
  2: 0x003B [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  3: 0x003D [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x003E [0x00] END_REQSTACK()
```
