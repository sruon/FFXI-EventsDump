# 17760389 - Five of Clubs

## Common Data

| Field            | Value                   |
|------------------|-------------------------|
| Zone             | Port Windurst (ID: 240) |
| Block Size       | 100 bytes               |
| Total Events     | 5                       |
| References Count | 5                       |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [65535.1](#event-655351) | 0x0001       |      1 |              1 |
| [65535.2](#event-655352) | 0x0002       |      4 |              2 |
| [221](#event-221)        | 0x0006       |     19 |             10 |
| [448](#event-448)        | 0x0019       |     19 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0E36      |        3638 |
|       2 | 0x0E37      |        3639 |
|       3 | 0x2E55      |       11861 |
|       4 | 0x2E56      |       11862 |

## String References

- **3638**: HeRe$26IN$26pOrT$26WiNdUrSt$26Is tHE$26MaGe$26AcA-dEmY$26rUn By$26tHe$26ORa-STeRy!
- **3639**: tO$26Go$26tO tHe$26oRaStErY's$26MaGe$26AcA-dEmY hEAd$26WesT!$26It$26IS$26oPPo-SiTe$26tHe CoN-sUlAtE$26oF$26bAsToK!
- **11861**: WhAt$26iS$26FiVE's$26GRe-EtinG? OF COu-RSe$26iT$26Is$26"hEl-lO!"
- **11862**: SeEmS$26tHAt$26FIVE$26OF$26SPADES$26hAs$26lEaRnEd$26tHe$26WrOnG$26gREe-tINg!

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

### Event 65535.1

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

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0002  |
| Data Size    | 4 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1C 00 80 00                                   ....          
```

#### Opcodes

```
  0: 0x0002 [0x1C] WAIT(30* ticks)
  1: 0x0005 [0x00] END_REQSTACK()
```

### Event 221

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0006   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                   1E F0  FF FF 7F 6F 70 1D 01 80        .....op...
0010: 23 1D 02 80 23 20 00 21  00                       #...# .!.       
```

#### Opcodes

```
  0: 0x0006 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x000B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x000C [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x000D [0x1D] PRINT_EVENT_MESSAGE(message_id=3638*)
    → "HeRe$26IN$26pOrT$26WiNdUrSt$26Is tHE$26MaGe$26AcA-dEmY$26rUn By$26tHe$26ORa-STeRy!"
  4: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0011 [0x1D] PRINT_EVENT_MESSAGE(message_id=3639*)
    → "tO$26Go$26tO tHe$26oRaStErY's$26MaGe$26AcA-dEmY hEAd$26WesT!$26It$26IS$26oPPo-SiTe$26tHe CoN-sUlAtE$26oF$26bAsToK!"
  6: 0x0014 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0015 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x0017 [0x21] END_EVENT
  9: 0x0018 [0x00] END_REQSTACK()
```

### Event 448

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0019   |
| Data Size    | 19 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                             1E F0 FF FF 7F 6F 70           .....op
0020: 1D 03 80 23 1D 04 80 23  20 00 21 00              ...#...# .!.    
```

#### Opcodes

```
  0: 0x0019 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x001E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x001F [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0020 [0x1D] PRINT_EVENT_MESSAGE(message_id=11861*)
    → "WhAt$26iS$26FiVE's$26GRe-EtinG? OF COu-RSe$26iT$26Is$26"hEl-lO!""
  4: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0024 [0x1D] PRINT_EVENT_MESSAGE(message_id=11862*)
    → "SeEmS$26tHAt$26FIVE$26OF$26SPADES$26hAs$26lEaRnEd$26tHe$26WrOnG$26gREe-tINg!"
  6: 0x0027 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0028 [0x20] SET_CLI_EVENT_UC_FLAG: Unlock player control
  8: 0x002A [0x21] END_EVENT
  9: 0x002B [0x00] END_REQSTACK()
```
