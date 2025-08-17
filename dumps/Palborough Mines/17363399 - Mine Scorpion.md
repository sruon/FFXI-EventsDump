# 17363399 - Mine Scorpion

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Palborough Mines (ID: 143) |
| Block Size       | 88 bytes                   |
| Total Events     | 3                          |
| References Count | 6                          |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [129](#event-129)        | 0x0001       |      7 |              2 |
| [65535.1](#event-655351) | 0x0008       |     28 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0032      |          50 |
|       1 | 0x001E      |          30 |
|       2 | 0x0028      |          40 |
|       3 | 0xADB2      |       44466 |
|       4 | 0xFFFE75DE  |  4294866398 |
|       5 | 0xFFFF835E  |  4294935390 |

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

### Event 129

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 7 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F 00                            .......        
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0008   |
| Data Size    | 28 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                          1C 00 80 1E C2 F1 08 01          ........
0010: 6F 70 1C 01 80 32 02 80  1F 00 03 80 04 80 05 80  op...2..........
0020: 1F 01 6F 00                                       ..o.            
```

#### Opcodes

```
  0: 0x0008 [0x1C] WAIT(50* ticks)
  1: 0x000B [0x1E] EventEntity looks at Gloom Phantom (ID: 17363394/0x0108F1C2) and starts talking
  2: 0x0010 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0011 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0012 [0x1C] WAIT(30* ticks)
  5: 0x0015 [0x32] ExtData[1]->MainSpeed = 40* * 0.1
  6: 0x0018 [0x1F] MOVE_ENTITY: EventEntity moves to X=44.466*, Z=-100.898*, Y=-31.906*
  7: 0x0020 [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  8: 0x0022 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  9: 0x0023 [0x00] END_REQSTACK()
```
