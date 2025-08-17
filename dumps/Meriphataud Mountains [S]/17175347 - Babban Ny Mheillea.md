# 17175347 - Babban Ny Mheillea

## Common Data

| Field            | Value                              |
|------------------|------------------------------------|
| Zone             | Meriphataud Mountains [S] (ID: 97) |
| Block Size       | 64 bytes                           |
| Total Events     | 3                                  |
| References Count | 4                                  |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [105](#event-105)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     17 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0007      |           7 |
|       1 | 0xAE36E     |      713582 |
|       2 | 0x89FA6     |      565158 |
|       3 | 0xFFFFBF8D  |  4294950797 |

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

### Event 105

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
| Data Size    | 17 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       61 01 32 00 80 1F  00 01 80 02 80 03 80 1F    a.2...........
0010: 01 6F 00                                          .o.             
```

#### Opcodes

```
  0: 0x0002 [0x61] EventEntity->Render.Flags2 |= 0x00000001
  1: 0x0004 [0x32] ExtData[1]->MainSpeed = 7* * 0.1
  2: 0x0007 [0x1F] MOVE_ENTITY: EventEntity moves to X=713.582*, Z=565.158*, Y=-16.499*
  3: 0x000F [0x1F] MOVE_ENTITY: Update entity position (mode=1)
  4: 0x0011 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  5: 0x0012 [0x00] END_REQSTACK()
```
