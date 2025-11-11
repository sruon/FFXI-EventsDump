# 17748199 - Curator Moogle

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Metalworks (ID: 237) |
| Block Size       | 1024 bytes           |
| Total Events     | 2                    |
| References Count | 62                   |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [1061](#event-1061)   | 0x0001       |    751 |            160 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x2D04      |       11524 |
|       1 | 0x0000      |           0 |
|       2 | 0x0001      |           1 |
|       3 | 0xFFFFFFFF  |  4294967295 |
|       4 | 0x0007      |           7 |
|       5 | 0x0010      |          16 |
|       6 | 0x0008      |           8 |
|       7 | 0x0014      |          20 |
|       8 | 0x2D05      |       11525 |
|       9 | 0x2D09      |       11529 |
|      10 | 0x2D06      |       11526 |
|      11 | 0x2D08      |       11528 |
|      12 | 0x0004      |           4 |
|      13 | 0x2D07      |       11527 |
|      14 | 0x50B9      |       20665 |
|      15 | 0x02E9      |         745 |
|      16 | 0x02CE      |         718 |
|      17 | 0x18C8      |        6344 |
|      18 | 0x0E67      |        3687 |
|      19 | 0x05A9      |        1449 |
|      20 | 0x0381      |         897 |
|      21 | 0x170C      |        5900 |
|      22 | 0x03A2      |         930 |
|      23 | 0x170E      |        5902 |
|      24 | 0x039C      |         924 |
|      25 | 0x170D      |        5901 |
|      26 | 0x0457      |        1111 |
|      27 | 0x170B      |        5899 |
|      28 | 0x0370      |         880 |
|      29 | 0x170A      |        5898 |
|      30 | 0x00BC      |         188 |
|      31 | 0x1262      |        4706 |
|      32 | 0x1263      |        4707 |
|      33 | 0x10CA      |        4298 |
|      34 | 0x50AF      |       20655 |
|      35 | 0x05AC      |        1452 |
|      36 | 0x026E      |         622 |
|      37 | 0x0397      |         919 |
|      38 | 0x1708      |        5896 |
|      39 | 0x1160      |        4448 |
|      40 | 0x1707      |        5895 |
|      41 | 0x027C      |         636 |
|      42 | 0x039B      |         923 |
|      43 | 0x1709      |        5897 |
|      44 | 0x05AF      |        1455 |
|      45 | 0x03AF      |         943 |
|      46 | 0x170F      |        5903 |
|      47 | 0x039A      |         922 |
|      48 | 0x1710      |        5904 |
|      49 | 0x03BB      |         955 |
|      50 | 0x1711      |        5905 |
|      51 | 0x672C      |       26412 |
|      52 | 0x00BD      |         189 |
|      53 | 0x12F2      |        4850 |
|      54 | 0x10CE      |        4302 |
|      55 | 0x6731      |       26417 |
|      56 | 0x0465      |        1125 |
|      57 | 0x03A5      |         933 |
|      58 | 0x1989      |        6537 |
|      59 | 0x0E28      |        3624 |
|      60 | 0x53F2      |       21490 |
|      61 | 0x0EA1      |        3745 |

## String References

- **11524**: Hail, adventurer! Take a look and see if there's anything you like, kupo! No gil necessary, jusst a quick little item in exchange!
- **11526**: If so, then I require that you trade me the following all at once in exchange for the $30.
- **11527**: $ $0 .
- **11528**: $ $0 .
- **11529**: Come again soon, kupo!

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

### Event 1061

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 751 bytes |
| Instructions | 18        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  1D 00 80 23 05 03 00 03   .....op...#....
0010: 04 00 01 80 02 03 00 02  80 00 A2 00 03 00 00 03  ................
0020: 80 03 02 00 01 80 03 0D  00 04 80 02 02 00 05 80  ................
0030: 03 5B 00 3D 00 00 02 00  02 80 9D 00 F0 01 01 00  .[.=............
0040: 0D 00 9D 05 C0 01 01 00  02 00 D4 03 02 00 01 00  ................
0050: 0B 02 00 07 0D 00 06 80  01 2B 00 3D 00 00 07 80  .........+.=....
0060: 02 80 D4 02 08 80 04 00  00 00 25 02 00 10 07 80  ..........%.....
0070: 00 7D 00 1D 09 80 23 06  03 00 01 9F 00 02 00 10  .}....#.........
0080: 07 80 03 9C 00 03 04 00  00 10 9D 00 C0 01 16 17  ................
0090: 04 00 1D 0A 80 23 1A A4  00 01 9F 00 06 03 00 01  .....#..........
00A0: 14 00 21 00 03 0D 00 04  00 14 0D 00 06 80 03 02  ..!.............
00B0: 00 01 80 03 10 00 01 80  02 02 00 04 80 03 EE 00  ................
00C0: 9D 00 F0 01 01 00 0D 00  9D 05 B0 01 01 00 02 00  ................
00D0: 0B 0D 00 02 01 00 01 80  00 E8 00 02 10 00 01 80  ................
00E0: 00 E8 00 03 10 00 02 00  0B 02 00 01 B8 00 02 10  ................
00F0: 00 01 80 00 FB 00 03 10  00 02 00 9D 00 F0 01 0C  ................
0100: 00 0D 00 03 0D 00 04 00  14 0D 00 06 80 03 0E 00  ................
0110: 01 80 03 18 00 01 80 03  15 00 01 80 03 17 00 01  ................
0120: 80 02 0E 00 10 00 03 AF  01 3E 15 00 0E 00 33 01  .........>....3.
0130: 01 A9 01 9D 00 B0 01 13  00 0E 00 03 16 00 13 00  ................
0140: 03 12 00 02 80 03 0F 00  0E 00 0B 0F 00 02 0F 00  ................
0150: 10 00 05 75 01 9D 00 B0  01 14 00 0F 00 02 14 00  ...u............
0160: 16 00 00 6F 01 0B 12 00  3C 15 00 0F 00 02 80 0B  ...o....<.......
0170: 0F 00 01 4D 01 03 17 17  13 00 03 18 17 12 00 07  ...M............
0180: 17 00 12 00 0B 18 00 02  17 00 10 00 00 96 01 48  ...............H
0190: 0B 80 23 01 A9 01 02 18  00 0C 80 00 A5 01 48 0B  ..#...........H.
01A0: 80 23 01 A9 01 48 0D 80  23 0B 0E 00 01 21 01 1B  .#...H..#....!..
01B0: 05 00 06 00 07 00 08 00  09 00 0A 00 0B 00 01 80  ................
01C0: 02 10 03 10 04 10 05 10  06 10 07 10 08 10 09 10  ................
01D0: 00 17 01 17 02 17 03 17  04 17 05 17 06 17 07 17  ................
01E0: 08 17 09 17 0A 17 0B 17  0C 17 0D 17 0E 17 0F 17  ................
01F0: 0E 80 0F 80 10 80 11 80  01 80 01 80 01 80 12 80  ................
0200: 13 80 14 80 01 80 01 80  01 80 01 80 01 80 15 80  ................
0210: 13 80 16 80 01 80 01 80  01 80 01 80 01 80 17 80  ................
0220: 13 80 18 80 01 80 01 80  01 80 01 80 01 80 19 80  ................
0230: 13 80 1A 80 01 80 01 80  01 80 01 80 01 80 1B 80  ................
0240: 13 80 1C 80 01 80 01 80  01 80 01 80 01 80 1D 80  ................
0250: 0E 80 1E 80 1F 80 20 80  21 80 01 80 01 80 22 80  ...... .!.....".
0260: 23 80 24 80 25 80 01 80  01 80 01 80 01 80 26 80  #.$.%.........&.
0270: 23 80 24 80 27 80 01 80  01 80 01 80 01 80 28 80  #.$.'.........(.
0280: 23 80 29 80 2A 80 01 80  01 80 01 80 01 80 2B 80  #.).*.........+.
0290: 2C 80 2D 80 01 80 01 80  01 80 01 80 01 80 2E 80  ,.-.............
02A0: 2C 80 2F 80 01 80 01 80  01 80 01 80 01 80 30 80  ,./...........0.
02B0: 2C 80 31 80 01 80 01 80  01 80 01 80 01 80 32 80  ,.1...........2.
02C0: 33 80 34 80 35 80 36 80  01 80 01 80 01 80 37 80  3.4.5.6.......7.
02D0: 38 80 39 80 39 80 01 80  01 80 01 80 01 80 3A 80  8.9.9.........:.
02E0: 3B 80 3C 80 01 80 01 80  01 80 01 80 01 80 3D 80  ;.<...........=.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x1D] PRINT_EVENT_MESSAGE(message_id=11524*)
    → "Hail, adventurer! Take a look and see if there's anything you like, kupo! No gil necessary, jusst a quick little item in exchange!"
  4: 0x000B [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x000C [0x05] ExtData[1]->WorkLocal[3] = 1
  6: 0x000F [0x03] ExtData[1]->WorkLocal[4] = 0*
  7: 0x0014 [0x02] IF !(ExtData[1]->WorkLocal[3] == 1*) GOTO 0x00A2
  8: 0x001C [0x03] ExtData[1]->WorkLocal[0] = 4294967295*
  9: 0x0021 [0x03] ExtData[1]->WorkLocal[2] = 0*
 10: 0x0026 [0x03] ExtData[1]->WorkLocal[13] = 7*
 11: 0x002B [0x02] IF !(ExtData[1]->WorkLocal[2] >= 16*) GOTO 0x005B
 12: 0x0033 [0x3D] CLEAR_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[0], bit_index_work_offset=ExtData[1]->WorkLocal[2], condition_work_offset=1*)
 13: 0x003A [0x9D] ExtData[1]->WorkLocal[1] = 0x01F0[ExtData[1]->WorkLocal[13]] // Read WORD
 14: 0x0042 [0x9D] 0x01C0[ExtData[1]->WorkLocal[2] * 2] = ExtData[1]->WorkLocal[1] // Write WORD
 15: 0x004A [0xD4] MAP_QUERY_WINDOW: Prepare buffer configuration A (buffer=[02 00 01 00 0B 02 00 07...])
 16: 0x0068 [0x00] END_REQSTACK()
 17: 0x0069 [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x006A [0x25] WAIT_DIALOG_SELECT()
     0x006B [0x02] IF !(Work_Zone[0] == 20*) GOTO 0x007D
     0x0073 [0x1D] PRINT_EVENT_MESSAGE(message_id=11529*)
    → "Come again soon, kupo!"
     0x0076 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0077 [0x06] ExtData[1]->WorkLocal[3] = 0
     0x007A [0x01] GOTO 0x009F
     0x007D [0x02] IF !(Work_Zone[0] >= 20*) GOTO 0x009C
     0x0085 [0x03] ExtData[1]->WorkLocal[4] = Work_Zone[0]
     0x008A [0x9D] Work_Zone_1700[22] = 0x01C0[ExtData[1]->WorkLocal[4]] // Read WORD
     0x0092 [0x1D] PRINT_EVENT_MESSAGE(message_id=11526*)
    → "If so, then I require that you trade me the following all at once in exchange for the $30."
     0x0095 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0096 [0x1A] CALL_SUBROUTINE(address=0x00A4)
     0x0099 [0x01] GOTO 0x009F
     0x009C [0x06] ExtData[1]->WorkLocal[3] = 0
     0x009F [0x01] GOTO 0x0014
     0x00A4 [0x03] ExtData[1]->WorkLocal[13] = ExtData[1]->WorkLocal[4]
     0x00A9 [0x14] ExtData[1]->WorkLocal[13] *= 8*
     0x00AE [0x03] ExtData[1]->WorkLocal[2] = 0*
     0x00B3 [0x03] ExtData[1]->WorkLocal[16] = 0*
     0x00B8 [0x02] IF !(ExtData[1]->WorkLocal[2] >= 7*) GOTO 0x00EE
     0x00C0 [0x9D] ExtData[1]->WorkLocal[1] = 0x01F0[ExtData[1]->WorkLocal[13]] // Read WORD
     0x00C8 [0x9D] 0x01B0[ExtData[1]->WorkLocal[2] * 2] = ExtData[1]->WorkLocal[1] // Write WORD
     0x00D0 [0x0B] ExtData[1]->WorkLocal[13]++
     0x00D3 [0x02] IF !(ExtData[1]->WorkLocal[1] == 0*) GOTO 0x00E8
     0x00DB [0x02] IF !(ExtData[1]->WorkLocal[16] == 0*) GOTO 0x00E8
     0x00E3 [0x03] ExtData[1]->WorkLocal[16] = ExtData[1]->WorkLocal[2]
     0x00E8 [0x0B] ExtData[1]->WorkLocal[2]++
     0x00EB [0x01] GOTO 0x00B8
     0x00EE [0x02] IF !(ExtData[1]->WorkLocal[16] == 0*) GOTO 0x00FB
     0x00F6 [0x03] ExtData[1]->WorkLocal[16] = ExtData[1]->WorkLocal[2]
     0x00FB [0x9D] ExtData[1]->WorkLocal[12] = 0x01F0[ExtData[1]->WorkLocal[13]] // Read WORD
     0x0103 [0x03] ExtData[1]->WorkLocal[13] = ExtData[1]->WorkLocal[4]
     0x0108 [0x14] ExtData[1]->WorkLocal[13] *= 8*
     0x010D [0x03] ExtData[1]->WorkLocal[14] = 0*
     0x0112 [0x03] ExtData[1]->WorkLocal[24] = 0*
     0x0117 [0x03] ExtData[1]->WorkLocal[21] = 0*
     0x011C [0x03] ExtData[1]->WorkLocal[23] = 0*
     0x0121 [0x02] IF !(ExtData[1]->WorkLocal[14] >= ExtData[1]->WorkLocal[16]) GOTO 0x01AF
     0x0129 [0x3E] IF !(ExtData[1]->WorkLocal[21] bit ExtData[1]->WorkLocal[14]) GOTO 0x0133
     0x0130 [0x01] GOTO 0x01A9
     0x0133 [0x9D] ExtData[1]->WorkLocal[19] = 0x01B0[ExtData[1]->WorkLocal[14]] // Read WORD
     0x013B [0x03] ExtData[1]->WorkLocal[22] = ExtData[1]->WorkLocal[19]
     0x0140 [0x03] ExtData[1]->WorkLocal[18] = 1*
     0x0145 [0x03] ExtData[1]->WorkLocal[15] = ExtData[1]->WorkLocal[14]
     0x014A [0x0B] ExtData[1]->WorkLocal[15]++
     0x014D [0x02] IF !(ExtData[1]->WorkLocal[15] > ExtData[1]->WorkLocal[16]) GOTO 0x0175
     0x0155 [0x9D] ExtData[1]->WorkLocal[20] = 0x01B0[ExtData[1]->WorkLocal[15]] // Read WORD
     0x015D [0x02] IF !(ExtData[1]->WorkLocal[20] == ExtData[1]->WorkLocal[22]) GOTO 0x016F
     0x0165 [0x0B] ExtData[1]->WorkLocal[18]++
     0x0168 [0x3C] SET_BIT_FLAG_CONDITIONAL(target_work_offset=ExtData[1]->WorkLocal[21], bit_index_work_offset=ExtData[1]->WorkLocal[15], condition_work_offset=1*)
     0x016F [0x0B] ExtData[1]->WorkLocal[15]++
     0x0172 [0x01] GOTO 0x014D
     0x0175 [0x03] Work_Zone_1700[23] = ExtData[1]->WorkLocal[19]
     0x017A [0x03] Work_Zone_1700[24] = ExtData[1]->WorkLocal[18]
     0x017F [0x07] ExtData[1]->WorkLocal[23] += ExtData[1]->WorkLocal[18]
     0x0184 [0x0B] ExtData[1]->WorkLocal[24]++
     0x0187 [0x02] IF !(ExtData[1]->WorkLocal[23] == ExtData[1]->WorkLocal[16]) GOTO 0x0196
     0x018F [0x48] [System] [11528*]:
    → "$ $0 ."
     0x0192 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x0193 [0x01] GOTO 0x01A9
     0x0196 [0x02] IF !(ExtData[1]->WorkLocal[24] == 4*) GOTO 0x01A5
     0x019E [0x48] [System] [11528*]:
    → "$ $0 ."
     0x01A1 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x01A2 [0x01] GOTO 0x01A9
     0x01A5 [0x48] [System] [11527*]:
    → "$ $0 ."
     0x01A8 [0x23] WAIT_FOR_DIALOG_INTERACTION
     0x01A9 [0x0B] ExtData[1]->WorkLocal[14]++
     0x01AC [0x01] GOTO 0x0121
     0x01AF [0x1B] RETURN
     0x01B0 [0x05] 0x0600 = 1
     0x01B3 [0x00] END_REQSTACK()
     0x01B4 [0x07] 0x0800 += 0x0900
     0x01B9 [0x00] END_REQSTACK()
     0x01BA [0x0A] 0x0B00 &= ~(1 << 0x0100)
     0x01BF [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 268636162/0x10031002))
     0x01C4 [0x04] DEPRECATED_NOP(unused=0x0510)
     0x01C7 [0x10] Work_Zone[6] <<= Work_Zone[7]
     0x01CC [0x08] 0x0910 -= ExtData[1]->WorkLocal[16]
     0x01D1 [0x17] Work_Zone_1700[1] = cos(Work_Zone_1700[2]) * Work_Zone_1700[3]
     0x01D8 [0x04] DEPRECATED_NOP(unused=0x0517)
     0x01DB [0x17] Work_Zone_1700[6] = cos(Work_Zone_1700[7]) * Work_Zone_1700[8]
     0x01E2 [0x09] 0x0A17 |= (1 << 0x0B17)
     0x01E7 [0x17] Work_Zone_1700[12] = cos(Work_Zone_1700[13]) * Work_Zone_1700[14]
     0x01EE [0x0F] 0x0E17 ^= 0x0F80
     0x01F3 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2148630544/0x80118010))
     0x01F8 [0x01] GOTO 0x0180
     0x01FB [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2148696065/0x80128001))
     0x0200 [0x13] 0x1480 = rand() % 0x0180
     0x0205 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2147581953/0x80018001))
     0x020A [0x01] GOTO 0x0180
     0x020D [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2148761621/0x80138015))
     0x0212 [0x16] 0x0180 = sin(0x0180) * 0x0180
     0x0219 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2147581953/0x80018001))
     0x021E [0x17] 0x1380 = cos(0x1880) * 0x0180
     0x0225 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2147581953/0x80018001))
     0x022A [0x01] GOTO 0x0180
     0x022D [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2148761625/0x80138019))
     0x0232 [0x1A] CALL_SUBROUTINE(address=0x0180)
     0x0235 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2147581953/0x80018001))
     0x023A [0x01] GOTO 0x0180
     0x023D [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2148761627/0x8013801B))
     0x0242 [0x1C] WAIT(0x0180 ticks)
     0x0245 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2147581953/0x80018001))
     0x024A [0x01] GOTO 0x0180
     0x024D [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2148433949/0x800E801D))
     0x0252 [0x1E] EventEntity looks at Unknown NPC (ID: 545267584/0x20801F80) and starts talking
     0x0257 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2147581985/0x80018021))
     0x025C [0x01] GOTO 0x2280
     0x025F [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2149875747/0x80248023))
     0x0264 [0x25] WAIT_DIALOG_SELECT()
     0x0265 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2147581953/0x80018001))
     0x026A [0x01] GOTO 0x0180
     0x026D [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2149810214/0x80238026))
     0x0272 [0x24] CREATE_DIALOG(message_id=0x2780, default_option=0x0180, option_flags=0x0180)
     0x0279 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2147581953/0x80018001))
     0x027E [0x28] REQ_SET_WITH_CONDITIONS(priority=0x80, target_entity=Unknown NPC (ID: 2150203427/0x80298023), tag_num=0x2A)
     0x0285 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2147581953/0x80018001))
     0x028A [0x01] GOTO 0x0180
     0x028D [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2150400043/0x802C802B))
     0x0292 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler 0x2E800180 with entities [Unknown NPC (ID: 25166208/0x01800180), Unknown NPC (ID: 25166208/0x01800180)]
     0x029F [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2150596652/0x802F802C))
     0x02A4 [0x01] GOTO 0x0180
     0x02A7 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2147581953/0x80018001))
     0x02AC [0x01] GOTO 0x3080
     0x02AF [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2150727724/0x8031802C))
     0x02B4 [0x01] GOTO 0x0180
     0x02B7 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2147581953/0x80018001))
     0x02BC [0x01] GOTO 0x3280
     0x02BF [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2150924339/0x80348033))
     0x02C4 [0x35] LOAD_ZONE_NO_CLOSE(zone_id=0x3680)
     0x02C7 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2147581953/0x80018001))
     0x02CC [0x01] GOTO 0x3780
     0x02CF [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2151252024/0x80398038))
     0x02D4 [0x39] SET_ENTITY_DIRECTION(direction=0x0180)
     0x02D7 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2147581953/0x80018001))
     0x02DC [0x01] GOTO 0x3A80
     0x02DF [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2151448635/0x803C803B))
     0x02E4 [0x01] GOTO 0x0180
     0x02E7 [0x80] LOAD_WAIT(entity=Unknown NPC (ID: 2147581953/0x80018001))
     0x02EC [0x01] GOTO 0x3D80
```
