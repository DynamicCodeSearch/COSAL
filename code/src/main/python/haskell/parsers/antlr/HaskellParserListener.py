# Generated from HaskellParser.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .HaskellParser import HaskellParser
else:
    from HaskellParser import HaskellParser

# This class defines a complete listener for a parse tree produced by HaskellParser.
class HaskellParserListener(ParseTreeListener):

    # Enter a parse tree produced by HaskellParser#module.
    def enterModule(self, ctx:HaskellParser.ModuleContext):
        pass

    # Exit a parse tree produced by HaskellParser#module.
    def exitModule(self, ctx:HaskellParser.ModuleContext):
        pass


    # Enter a parse tree produced by HaskellParser#module_content.
    def enterModule_content(self, ctx:HaskellParser.Module_contentContext):
        pass

    # Exit a parse tree produced by HaskellParser#module_content.
    def exitModule_content(self, ctx:HaskellParser.Module_contentContext):
        pass


    # Enter a parse tree produced by HaskellParser#where_module.
    def enterWhere_module(self, ctx:HaskellParser.Where_moduleContext):
        pass

    # Exit a parse tree produced by HaskellParser#where_module.
    def exitWhere_module(self, ctx:HaskellParser.Where_moduleContext):
        pass


    # Enter a parse tree produced by HaskellParser#module_body.
    def enterModule_body(self, ctx:HaskellParser.Module_bodyContext):
        pass

    # Exit a parse tree produced by HaskellParser#module_body.
    def exitModule_body(self, ctx:HaskellParser.Module_bodyContext):
        pass


    # Enter a parse tree produced by HaskellParser#pragmas.
    def enterPragmas(self, ctx:HaskellParser.PragmasContext):
        pass

    # Exit a parse tree produced by HaskellParser#pragmas.
    def exitPragmas(self, ctx:HaskellParser.PragmasContext):
        pass


    # Enter a parse tree produced by HaskellParser#pragma.
    def enterPragma(self, ctx:HaskellParser.PragmaContext):
        pass

    # Exit a parse tree produced by HaskellParser#pragma.
    def exitPragma(self, ctx:HaskellParser.PragmaContext):
        pass


    # Enter a parse tree produced by HaskellParser#language_pragma.
    def enterLanguage_pragma(self, ctx:HaskellParser.Language_pragmaContext):
        pass

    # Exit a parse tree produced by HaskellParser#language_pragma.
    def exitLanguage_pragma(self, ctx:HaskellParser.Language_pragmaContext):
        pass


    # Enter a parse tree produced by HaskellParser#options_ghc.
    def enterOptions_ghc(self, ctx:HaskellParser.Options_ghcContext):
        pass

    # Exit a parse tree produced by HaskellParser#options_ghc.
    def exitOptions_ghc(self, ctx:HaskellParser.Options_ghcContext):
        pass


    # Enter a parse tree produced by HaskellParser#simple_options.
    def enterSimple_options(self, ctx:HaskellParser.Simple_optionsContext):
        pass

    # Exit a parse tree produced by HaskellParser#simple_options.
    def exitSimple_options(self, ctx:HaskellParser.Simple_optionsContext):
        pass


    # Enter a parse tree produced by HaskellParser#extension.
    def enterExtension(self, ctx:HaskellParser.ExtensionContext):
        pass

    # Exit a parse tree produced by HaskellParser#extension.
    def exitExtension(self, ctx:HaskellParser.ExtensionContext):
        pass


    # Enter a parse tree produced by HaskellParser#body.
    def enterBody(self, ctx:HaskellParser.BodyContext):
        pass

    # Exit a parse tree produced by HaskellParser#body.
    def exitBody(self, ctx:HaskellParser.BodyContext):
        pass


    # Enter a parse tree produced by HaskellParser#impdecls.
    def enterImpdecls(self, ctx:HaskellParser.ImpdeclsContext):
        pass

    # Exit a parse tree produced by HaskellParser#impdecls.
    def exitImpdecls(self, ctx:HaskellParser.ImpdeclsContext):
        pass


    # Enter a parse tree produced by HaskellParser#exports.
    def enterExports(self, ctx:HaskellParser.ExportsContext):
        pass

    # Exit a parse tree produced by HaskellParser#exports.
    def exitExports(self, ctx:HaskellParser.ExportsContext):
        pass


    # Enter a parse tree produced by HaskellParser#exprt.
    def enterExprt(self, ctx:HaskellParser.ExprtContext):
        pass

    # Exit a parse tree produced by HaskellParser#exprt.
    def exitExprt(self, ctx:HaskellParser.ExprtContext):
        pass


    # Enter a parse tree produced by HaskellParser#impdecl.
    def enterImpdecl(self, ctx:HaskellParser.ImpdeclContext):
        pass

    # Exit a parse tree produced by HaskellParser#impdecl.
    def exitImpdecl(self, ctx:HaskellParser.ImpdeclContext):
        pass


    # Enter a parse tree produced by HaskellParser#impspec.
    def enterImpspec(self, ctx:HaskellParser.ImpspecContext):
        pass

    # Exit a parse tree produced by HaskellParser#impspec.
    def exitImpspec(self, ctx:HaskellParser.ImpspecContext):
        pass


    # Enter a parse tree produced by HaskellParser#himport.
    def enterHimport(self, ctx:HaskellParser.HimportContext):
        pass

    # Exit a parse tree produced by HaskellParser#himport.
    def exitHimport(self, ctx:HaskellParser.HimportContext):
        pass


    # Enter a parse tree produced by HaskellParser#cname.
    def enterCname(self, ctx:HaskellParser.CnameContext):
        pass

    # Exit a parse tree produced by HaskellParser#cname.
    def exitCname(self, ctx:HaskellParser.CnameContext):
        pass


    # Enter a parse tree produced by HaskellParser#fixity.
    def enterFixity(self, ctx:HaskellParser.FixityContext):
        pass

    # Exit a parse tree produced by HaskellParser#fixity.
    def exitFixity(self, ctx:HaskellParser.FixityContext):
        pass


    # Enter a parse tree produced by HaskellParser#ops.
    def enterOps(self, ctx:HaskellParser.OpsContext):
        pass

    # Exit a parse tree produced by HaskellParser#ops.
    def exitOps(self, ctx:HaskellParser.OpsContext):
        pass


    # Enter a parse tree produced by HaskellParser#topdecls.
    def enterTopdecls(self, ctx:HaskellParser.TopdeclsContext):
        pass

    # Exit a parse tree produced by HaskellParser#topdecls.
    def exitTopdecls(self, ctx:HaskellParser.TopdeclsContext):
        pass


    # Enter a parse tree produced by HaskellParser#topdecl.
    def enterTopdecl(self, ctx:HaskellParser.TopdeclContext):
        pass

    # Exit a parse tree produced by HaskellParser#topdecl.
    def exitTopdecl(self, ctx:HaskellParser.TopdeclContext):
        pass


    # Enter a parse tree produced by HaskellParser#cl_decl.
    def enterCl_decl(self, ctx:HaskellParser.Cl_declContext):
        pass

    # Exit a parse tree produced by HaskellParser#cl_decl.
    def exitCl_decl(self, ctx:HaskellParser.Cl_declContext):
        pass


    # Enter a parse tree produced by HaskellParser#ty_decl.
    def enterTy_decl(self, ctx:HaskellParser.Ty_declContext):
        pass

    # Exit a parse tree produced by HaskellParser#ty_decl.
    def exitTy_decl(self, ctx:HaskellParser.Ty_declContext):
        pass


    # Enter a parse tree produced by HaskellParser#standalone_kind_sig.
    def enterStandalone_kind_sig(self, ctx:HaskellParser.Standalone_kind_sigContext):
        pass

    # Exit a parse tree produced by HaskellParser#standalone_kind_sig.
    def exitStandalone_kind_sig(self, ctx:HaskellParser.Standalone_kind_sigContext):
        pass


    # Enter a parse tree produced by HaskellParser#sks_vars.
    def enterSks_vars(self, ctx:HaskellParser.Sks_varsContext):
        pass

    # Exit a parse tree produced by HaskellParser#sks_vars.
    def exitSks_vars(self, ctx:HaskellParser.Sks_varsContext):
        pass


    # Enter a parse tree produced by HaskellParser#inst_decl.
    def enterInst_decl(self, ctx:HaskellParser.Inst_declContext):
        pass

    # Exit a parse tree produced by HaskellParser#inst_decl.
    def exitInst_decl(self, ctx:HaskellParser.Inst_declContext):
        pass


    # Enter a parse tree produced by HaskellParser#overlap_pragma.
    def enterOverlap_pragma(self, ctx:HaskellParser.Overlap_pragmaContext):
        pass

    # Exit a parse tree produced by HaskellParser#overlap_pragma.
    def exitOverlap_pragma(self, ctx:HaskellParser.Overlap_pragmaContext):
        pass


    # Enter a parse tree produced by HaskellParser#deriv_strategy_no_via.
    def enterDeriv_strategy_no_via(self, ctx:HaskellParser.Deriv_strategy_no_viaContext):
        pass

    # Exit a parse tree produced by HaskellParser#deriv_strategy_no_via.
    def exitDeriv_strategy_no_via(self, ctx:HaskellParser.Deriv_strategy_no_viaContext):
        pass


    # Enter a parse tree produced by HaskellParser#deriv_strategy_via.
    def enterDeriv_strategy_via(self, ctx:HaskellParser.Deriv_strategy_viaContext):
        pass

    # Exit a parse tree produced by HaskellParser#deriv_strategy_via.
    def exitDeriv_strategy_via(self, ctx:HaskellParser.Deriv_strategy_viaContext):
        pass


    # Enter a parse tree produced by HaskellParser#deriv_standalone_strategy.
    def enterDeriv_standalone_strategy(self, ctx:HaskellParser.Deriv_standalone_strategyContext):
        pass

    # Exit a parse tree produced by HaskellParser#deriv_standalone_strategy.
    def exitDeriv_standalone_strategy(self, ctx:HaskellParser.Deriv_standalone_strategyContext):
        pass


    # Enter a parse tree produced by HaskellParser#opt_injective_info.
    def enterOpt_injective_info(self, ctx:HaskellParser.Opt_injective_infoContext):
        pass

    # Exit a parse tree produced by HaskellParser#opt_injective_info.
    def exitOpt_injective_info(self, ctx:HaskellParser.Opt_injective_infoContext):
        pass


    # Enter a parse tree produced by HaskellParser#injectivity_cond.
    def enterInjectivity_cond(self, ctx:HaskellParser.Injectivity_condContext):
        pass

    # Exit a parse tree produced by HaskellParser#injectivity_cond.
    def exitInjectivity_cond(self, ctx:HaskellParser.Injectivity_condContext):
        pass


    # Enter a parse tree produced by HaskellParser#inj_varids.
    def enterInj_varids(self, ctx:HaskellParser.Inj_varidsContext):
        pass

    # Exit a parse tree produced by HaskellParser#inj_varids.
    def exitInj_varids(self, ctx:HaskellParser.Inj_varidsContext):
        pass


    # Enter a parse tree produced by HaskellParser#where_type_family.
    def enterWhere_type_family(self, ctx:HaskellParser.Where_type_familyContext):
        pass

    # Exit a parse tree produced by HaskellParser#where_type_family.
    def exitWhere_type_family(self, ctx:HaskellParser.Where_type_familyContext):
        pass


    # Enter a parse tree produced by HaskellParser#ty_fam_inst_eqn_list.
    def enterTy_fam_inst_eqn_list(self, ctx:HaskellParser.Ty_fam_inst_eqn_listContext):
        pass

    # Exit a parse tree produced by HaskellParser#ty_fam_inst_eqn_list.
    def exitTy_fam_inst_eqn_list(self, ctx:HaskellParser.Ty_fam_inst_eqn_listContext):
        pass


    # Enter a parse tree produced by HaskellParser#ty_fam_inst_eqns.
    def enterTy_fam_inst_eqns(self, ctx:HaskellParser.Ty_fam_inst_eqnsContext):
        pass

    # Exit a parse tree produced by HaskellParser#ty_fam_inst_eqns.
    def exitTy_fam_inst_eqns(self, ctx:HaskellParser.Ty_fam_inst_eqnsContext):
        pass


    # Enter a parse tree produced by HaskellParser#ty_fam_inst_eqn.
    def enterTy_fam_inst_eqn(self, ctx:HaskellParser.Ty_fam_inst_eqnContext):
        pass

    # Exit a parse tree produced by HaskellParser#ty_fam_inst_eqn.
    def exitTy_fam_inst_eqn(self, ctx:HaskellParser.Ty_fam_inst_eqnContext):
        pass


    # Enter a parse tree produced by HaskellParser#at_decl_cls.
    def enterAt_decl_cls(self, ctx:HaskellParser.At_decl_clsContext):
        pass

    # Exit a parse tree produced by HaskellParser#at_decl_cls.
    def exitAt_decl_cls(self, ctx:HaskellParser.At_decl_clsContext):
        pass


    # Enter a parse tree produced by HaskellParser#at_decl_inst.
    def enterAt_decl_inst(self, ctx:HaskellParser.At_decl_instContext):
        pass

    # Exit a parse tree produced by HaskellParser#at_decl_inst.
    def exitAt_decl_inst(self, ctx:HaskellParser.At_decl_instContext):
        pass


    # Enter a parse tree produced by HaskellParser#opt_kind_sig.
    def enterOpt_kind_sig(self, ctx:HaskellParser.Opt_kind_sigContext):
        pass

    # Exit a parse tree produced by HaskellParser#opt_kind_sig.
    def exitOpt_kind_sig(self, ctx:HaskellParser.Opt_kind_sigContext):
        pass


    # Enter a parse tree produced by HaskellParser#opt_datafam_kind_sig.
    def enterOpt_datafam_kind_sig(self, ctx:HaskellParser.Opt_datafam_kind_sigContext):
        pass

    # Exit a parse tree produced by HaskellParser#opt_datafam_kind_sig.
    def exitOpt_datafam_kind_sig(self, ctx:HaskellParser.Opt_datafam_kind_sigContext):
        pass


    # Enter a parse tree produced by HaskellParser#opt_tyfam_kind_sig.
    def enterOpt_tyfam_kind_sig(self, ctx:HaskellParser.Opt_tyfam_kind_sigContext):
        pass

    # Exit a parse tree produced by HaskellParser#opt_tyfam_kind_sig.
    def exitOpt_tyfam_kind_sig(self, ctx:HaskellParser.Opt_tyfam_kind_sigContext):
        pass


    # Enter a parse tree produced by HaskellParser#opt_at_kind_inj_sig.
    def enterOpt_at_kind_inj_sig(self, ctx:HaskellParser.Opt_at_kind_inj_sigContext):
        pass

    # Exit a parse tree produced by HaskellParser#opt_at_kind_inj_sig.
    def exitOpt_at_kind_inj_sig(self, ctx:HaskellParser.Opt_at_kind_inj_sigContext):
        pass


    # Enter a parse tree produced by HaskellParser#tycl_hdr.
    def enterTycl_hdr(self, ctx:HaskellParser.Tycl_hdrContext):
        pass

    # Exit a parse tree produced by HaskellParser#tycl_hdr.
    def exitTycl_hdr(self, ctx:HaskellParser.Tycl_hdrContext):
        pass


    # Enter a parse tree produced by HaskellParser#tycl_hdr_inst.
    def enterTycl_hdr_inst(self, ctx:HaskellParser.Tycl_hdr_instContext):
        pass

    # Exit a parse tree produced by HaskellParser#tycl_hdr_inst.
    def exitTycl_hdr_inst(self, ctx:HaskellParser.Tycl_hdr_instContext):
        pass


    # Enter a parse tree produced by HaskellParser#capi_ctype.
    def enterCapi_ctype(self, ctx:HaskellParser.Capi_ctypeContext):
        pass

    # Exit a parse tree produced by HaskellParser#capi_ctype.
    def exitCapi_ctype(self, ctx:HaskellParser.Capi_ctypeContext):
        pass


    # Enter a parse tree produced by HaskellParser#standalone_deriving.
    def enterStandalone_deriving(self, ctx:HaskellParser.Standalone_derivingContext):
        pass

    # Exit a parse tree produced by HaskellParser#standalone_deriving.
    def exitStandalone_deriving(self, ctx:HaskellParser.Standalone_derivingContext):
        pass


    # Enter a parse tree produced by HaskellParser#role_annot.
    def enterRole_annot(self, ctx:HaskellParser.Role_annotContext):
        pass

    # Exit a parse tree produced by HaskellParser#role_annot.
    def exitRole_annot(self, ctx:HaskellParser.Role_annotContext):
        pass


    # Enter a parse tree produced by HaskellParser#roles.
    def enterRoles(self, ctx:HaskellParser.RolesContext):
        pass

    # Exit a parse tree produced by HaskellParser#roles.
    def exitRoles(self, ctx:HaskellParser.RolesContext):
        pass


    # Enter a parse tree produced by HaskellParser#role.
    def enterRole(self, ctx:HaskellParser.RoleContext):
        pass

    # Exit a parse tree produced by HaskellParser#role.
    def exitRole(self, ctx:HaskellParser.RoleContext):
        pass


    # Enter a parse tree produced by HaskellParser#pattern_synonym_decl.
    def enterPattern_synonym_decl(self, ctx:HaskellParser.Pattern_synonym_declContext):
        pass

    # Exit a parse tree produced by HaskellParser#pattern_synonym_decl.
    def exitPattern_synonym_decl(self, ctx:HaskellParser.Pattern_synonym_declContext):
        pass


    # Enter a parse tree produced by HaskellParser#pattern_synonym_lhs.
    def enterPattern_synonym_lhs(self, ctx:HaskellParser.Pattern_synonym_lhsContext):
        pass

    # Exit a parse tree produced by HaskellParser#pattern_synonym_lhs.
    def exitPattern_synonym_lhs(self, ctx:HaskellParser.Pattern_synonym_lhsContext):
        pass


    # Enter a parse tree produced by HaskellParser#hvars.
    def enterHvars(self, ctx:HaskellParser.HvarsContext):
        pass

    # Exit a parse tree produced by HaskellParser#hvars.
    def exitHvars(self, ctx:HaskellParser.HvarsContext):
        pass


    # Enter a parse tree produced by HaskellParser#cvars.
    def enterCvars(self, ctx:HaskellParser.CvarsContext):
        pass

    # Exit a parse tree produced by HaskellParser#cvars.
    def exitCvars(self, ctx:HaskellParser.CvarsContext):
        pass


    # Enter a parse tree produced by HaskellParser#where_decls.
    def enterWhere_decls(self, ctx:HaskellParser.Where_declsContext):
        pass

    # Exit a parse tree produced by HaskellParser#where_decls.
    def exitWhere_decls(self, ctx:HaskellParser.Where_declsContext):
        pass


    # Enter a parse tree produced by HaskellParser#pattern_synonym_sig.
    def enterPattern_synonym_sig(self, ctx:HaskellParser.Pattern_synonym_sigContext):
        pass

    # Exit a parse tree produced by HaskellParser#pattern_synonym_sig.
    def exitPattern_synonym_sig(self, ctx:HaskellParser.Pattern_synonym_sigContext):
        pass


    # Enter a parse tree produced by HaskellParser#decl_cls.
    def enterDecl_cls(self, ctx:HaskellParser.Decl_clsContext):
        pass

    # Exit a parse tree produced by HaskellParser#decl_cls.
    def exitDecl_cls(self, ctx:HaskellParser.Decl_clsContext):
        pass


    # Enter a parse tree produced by HaskellParser#decls_cls.
    def enterDecls_cls(self, ctx:HaskellParser.Decls_clsContext):
        pass

    # Exit a parse tree produced by HaskellParser#decls_cls.
    def exitDecls_cls(self, ctx:HaskellParser.Decls_clsContext):
        pass


    # Enter a parse tree produced by HaskellParser#decllist_cls.
    def enterDecllist_cls(self, ctx:HaskellParser.Decllist_clsContext):
        pass

    # Exit a parse tree produced by HaskellParser#decllist_cls.
    def exitDecllist_cls(self, ctx:HaskellParser.Decllist_clsContext):
        pass


    # Enter a parse tree produced by HaskellParser#where_cls.
    def enterWhere_cls(self, ctx:HaskellParser.Where_clsContext):
        pass

    # Exit a parse tree produced by HaskellParser#where_cls.
    def exitWhere_cls(self, ctx:HaskellParser.Where_clsContext):
        pass


    # Enter a parse tree produced by HaskellParser#decl_inst.
    def enterDecl_inst(self, ctx:HaskellParser.Decl_instContext):
        pass

    # Exit a parse tree produced by HaskellParser#decl_inst.
    def exitDecl_inst(self, ctx:HaskellParser.Decl_instContext):
        pass


    # Enter a parse tree produced by HaskellParser#decls_inst.
    def enterDecls_inst(self, ctx:HaskellParser.Decls_instContext):
        pass

    # Exit a parse tree produced by HaskellParser#decls_inst.
    def exitDecls_inst(self, ctx:HaskellParser.Decls_instContext):
        pass


    # Enter a parse tree produced by HaskellParser#decllist_inst.
    def enterDecllist_inst(self, ctx:HaskellParser.Decllist_instContext):
        pass

    # Exit a parse tree produced by HaskellParser#decllist_inst.
    def exitDecllist_inst(self, ctx:HaskellParser.Decllist_instContext):
        pass


    # Enter a parse tree produced by HaskellParser#where_inst.
    def enterWhere_inst(self, ctx:HaskellParser.Where_instContext):
        pass

    # Exit a parse tree produced by HaskellParser#where_inst.
    def exitWhere_inst(self, ctx:HaskellParser.Where_instContext):
        pass


    # Enter a parse tree produced by HaskellParser#decls.
    def enterDecls(self, ctx:HaskellParser.DeclsContext):
        pass

    # Exit a parse tree produced by HaskellParser#decls.
    def exitDecls(self, ctx:HaskellParser.DeclsContext):
        pass


    # Enter a parse tree produced by HaskellParser#decllist.
    def enterDecllist(self, ctx:HaskellParser.DecllistContext):
        pass

    # Exit a parse tree produced by HaskellParser#decllist.
    def exitDecllist(self, ctx:HaskellParser.DecllistContext):
        pass


    # Enter a parse tree produced by HaskellParser#binds.
    def enterBinds(self, ctx:HaskellParser.BindsContext):
        pass

    # Exit a parse tree produced by HaskellParser#binds.
    def exitBinds(self, ctx:HaskellParser.BindsContext):
        pass


    # Enter a parse tree produced by HaskellParser#wherebinds.
    def enterWherebinds(self, ctx:HaskellParser.WherebindsContext):
        pass

    # Exit a parse tree produced by HaskellParser#wherebinds.
    def exitWherebinds(self, ctx:HaskellParser.WherebindsContext):
        pass


    # Enter a parse tree produced by HaskellParser#rules.
    def enterRules(self, ctx:HaskellParser.RulesContext):
        pass

    # Exit a parse tree produced by HaskellParser#rules.
    def exitRules(self, ctx:HaskellParser.RulesContext):
        pass


    # Enter a parse tree produced by HaskellParser#pragma_rule.
    def enterPragma_rule(self, ctx:HaskellParser.Pragma_ruleContext):
        pass

    # Exit a parse tree produced by HaskellParser#pragma_rule.
    def exitPragma_rule(self, ctx:HaskellParser.Pragma_ruleContext):
        pass


    # Enter a parse tree produced by HaskellParser#rule_activation_marker.
    def enterRule_activation_marker(self, ctx:HaskellParser.Rule_activation_markerContext):
        pass

    # Exit a parse tree produced by HaskellParser#rule_activation_marker.
    def exitRule_activation_marker(self, ctx:HaskellParser.Rule_activation_markerContext):
        pass


    # Enter a parse tree produced by HaskellParser#rule_activation.
    def enterRule_activation(self, ctx:HaskellParser.Rule_activationContext):
        pass

    # Exit a parse tree produced by HaskellParser#rule_activation.
    def exitRule_activation(self, ctx:HaskellParser.Rule_activationContext):
        pass


    # Enter a parse tree produced by HaskellParser#rule_foralls.
    def enterRule_foralls(self, ctx:HaskellParser.Rule_forallsContext):
        pass

    # Exit a parse tree produced by HaskellParser#rule_foralls.
    def exitRule_foralls(self, ctx:HaskellParser.Rule_forallsContext):
        pass


    # Enter a parse tree produced by HaskellParser#rule_vars.
    def enterRule_vars(self, ctx:HaskellParser.Rule_varsContext):
        pass

    # Exit a parse tree produced by HaskellParser#rule_vars.
    def exitRule_vars(self, ctx:HaskellParser.Rule_varsContext):
        pass


    # Enter a parse tree produced by HaskellParser#rule_var.
    def enterRule_var(self, ctx:HaskellParser.Rule_varContext):
        pass

    # Exit a parse tree produced by HaskellParser#rule_var.
    def exitRule_var(self, ctx:HaskellParser.Rule_varContext):
        pass


    # Enter a parse tree produced by HaskellParser#warnings.
    def enterWarnings(self, ctx:HaskellParser.WarningsContext):
        pass

    # Exit a parse tree produced by HaskellParser#warnings.
    def exitWarnings(self, ctx:HaskellParser.WarningsContext):
        pass


    # Enter a parse tree produced by HaskellParser#pragma_warning.
    def enterPragma_warning(self, ctx:HaskellParser.Pragma_warningContext):
        pass

    # Exit a parse tree produced by HaskellParser#pragma_warning.
    def exitPragma_warning(self, ctx:HaskellParser.Pragma_warningContext):
        pass


    # Enter a parse tree produced by HaskellParser#deprecations.
    def enterDeprecations(self, ctx:HaskellParser.DeprecationsContext):
        pass

    # Exit a parse tree produced by HaskellParser#deprecations.
    def exitDeprecations(self, ctx:HaskellParser.DeprecationsContext):
        pass


    # Enter a parse tree produced by HaskellParser#pragma_deprecation.
    def enterPragma_deprecation(self, ctx:HaskellParser.Pragma_deprecationContext):
        pass

    # Exit a parse tree produced by HaskellParser#pragma_deprecation.
    def exitPragma_deprecation(self, ctx:HaskellParser.Pragma_deprecationContext):
        pass


    # Enter a parse tree produced by HaskellParser#strings.
    def enterStrings(self, ctx:HaskellParser.StringsContext):
        pass

    # Exit a parse tree produced by HaskellParser#strings.
    def exitStrings(self, ctx:HaskellParser.StringsContext):
        pass


    # Enter a parse tree produced by HaskellParser#stringlist.
    def enterStringlist(self, ctx:HaskellParser.StringlistContext):
        pass

    # Exit a parse tree produced by HaskellParser#stringlist.
    def exitStringlist(self, ctx:HaskellParser.StringlistContext):
        pass


    # Enter a parse tree produced by HaskellParser#annotation.
    def enterAnnotation(self, ctx:HaskellParser.AnnotationContext):
        pass

    # Exit a parse tree produced by HaskellParser#annotation.
    def exitAnnotation(self, ctx:HaskellParser.AnnotationContext):
        pass


    # Enter a parse tree produced by HaskellParser#fdecl.
    def enterFdecl(self, ctx:HaskellParser.FdeclContext):
        pass

    # Exit a parse tree produced by HaskellParser#fdecl.
    def exitFdecl(self, ctx:HaskellParser.FdeclContext):
        pass


    # Enter a parse tree produced by HaskellParser#callconv.
    def enterCallconv(self, ctx:HaskellParser.CallconvContext):
        pass

    # Exit a parse tree produced by HaskellParser#callconv.
    def exitCallconv(self, ctx:HaskellParser.CallconvContext):
        pass


    # Enter a parse tree produced by HaskellParser#safety.
    def enterSafety(self, ctx:HaskellParser.SafetyContext):
        pass

    # Exit a parse tree produced by HaskellParser#safety.
    def exitSafety(self, ctx:HaskellParser.SafetyContext):
        pass


    # Enter a parse tree produced by HaskellParser#fspec.
    def enterFspec(self, ctx:HaskellParser.FspecContext):
        pass

    # Exit a parse tree produced by HaskellParser#fspec.
    def exitFspec(self, ctx:HaskellParser.FspecContext):
        pass


    # Enter a parse tree produced by HaskellParser#opt_sig.
    def enterOpt_sig(self, ctx:HaskellParser.Opt_sigContext):
        pass

    # Exit a parse tree produced by HaskellParser#opt_sig.
    def exitOpt_sig(self, ctx:HaskellParser.Opt_sigContext):
        pass


    # Enter a parse tree produced by HaskellParser#opt_tyconsig.
    def enterOpt_tyconsig(self, ctx:HaskellParser.Opt_tyconsigContext):
        pass

    # Exit a parse tree produced by HaskellParser#opt_tyconsig.
    def exitOpt_tyconsig(self, ctx:HaskellParser.Opt_tyconsigContext):
        pass


    # Enter a parse tree produced by HaskellParser#sigtype.
    def enterSigtype(self, ctx:HaskellParser.SigtypeContext):
        pass

    # Exit a parse tree produced by HaskellParser#sigtype.
    def exitSigtype(self, ctx:HaskellParser.SigtypeContext):
        pass


    # Enter a parse tree produced by HaskellParser#sigtypedoc.
    def enterSigtypedoc(self, ctx:HaskellParser.SigtypedocContext):
        pass

    # Exit a parse tree produced by HaskellParser#sigtypedoc.
    def exitSigtypedoc(self, ctx:HaskellParser.SigtypedocContext):
        pass


    # Enter a parse tree produced by HaskellParser#sig_vars.
    def enterSig_vars(self, ctx:HaskellParser.Sig_varsContext):
        pass

    # Exit a parse tree produced by HaskellParser#sig_vars.
    def exitSig_vars(self, ctx:HaskellParser.Sig_varsContext):
        pass


    # Enter a parse tree produced by HaskellParser#sigtypes1.
    def enterSigtypes1(self, ctx:HaskellParser.Sigtypes1Context):
        pass

    # Exit a parse tree produced by HaskellParser#sigtypes1.
    def exitSigtypes1(self, ctx:HaskellParser.Sigtypes1Context):
        pass


    # Enter a parse tree produced by HaskellParser#unpackedness.
    def enterUnpackedness(self, ctx:HaskellParser.UnpackednessContext):
        pass

    # Exit a parse tree produced by HaskellParser#unpackedness.
    def exitUnpackedness(self, ctx:HaskellParser.UnpackednessContext):
        pass


    # Enter a parse tree produced by HaskellParser#forall_vis_flag.
    def enterForall_vis_flag(self, ctx:HaskellParser.Forall_vis_flagContext):
        pass

    # Exit a parse tree produced by HaskellParser#forall_vis_flag.
    def exitForall_vis_flag(self, ctx:HaskellParser.Forall_vis_flagContext):
        pass


    # Enter a parse tree produced by HaskellParser#ktype.
    def enterKtype(self, ctx:HaskellParser.KtypeContext):
        pass

    # Exit a parse tree produced by HaskellParser#ktype.
    def exitKtype(self, ctx:HaskellParser.KtypeContext):
        pass


    # Enter a parse tree produced by HaskellParser#ktypedoc.
    def enterKtypedoc(self, ctx:HaskellParser.KtypedocContext):
        pass

    # Exit a parse tree produced by HaskellParser#ktypedoc.
    def exitKtypedoc(self, ctx:HaskellParser.KtypedocContext):
        pass


    # Enter a parse tree produced by HaskellParser#ctype.
    def enterCtype(self, ctx:HaskellParser.CtypeContext):
        pass

    # Exit a parse tree produced by HaskellParser#ctype.
    def exitCtype(self, ctx:HaskellParser.CtypeContext):
        pass


    # Enter a parse tree produced by HaskellParser#ctypedoc.
    def enterCtypedoc(self, ctx:HaskellParser.CtypedocContext):
        pass

    # Exit a parse tree produced by HaskellParser#ctypedoc.
    def exitCtypedoc(self, ctx:HaskellParser.CtypedocContext):
        pass


    # Enter a parse tree produced by HaskellParser#tycl_context.
    def enterTycl_context(self, ctx:HaskellParser.Tycl_contextContext):
        pass

    # Exit a parse tree produced by HaskellParser#tycl_context.
    def exitTycl_context(self, ctx:HaskellParser.Tycl_contextContext):
        pass


    # Enter a parse tree produced by HaskellParser#constr_context.
    def enterConstr_context(self, ctx:HaskellParser.Constr_contextContext):
        pass

    # Exit a parse tree produced by HaskellParser#constr_context.
    def exitConstr_context(self, ctx:HaskellParser.Constr_contextContext):
        pass


    # Enter a parse tree produced by HaskellParser#htype.
    def enterHtype(self, ctx:HaskellParser.HtypeContext):
        pass

    # Exit a parse tree produced by HaskellParser#htype.
    def exitHtype(self, ctx:HaskellParser.HtypeContext):
        pass


    # Enter a parse tree produced by HaskellParser#typedoc.
    def enterTypedoc(self, ctx:HaskellParser.TypedocContext):
        pass

    # Exit a parse tree produced by HaskellParser#typedoc.
    def exitTypedoc(self, ctx:HaskellParser.TypedocContext):
        pass


    # Enter a parse tree produced by HaskellParser#constr_btype.
    def enterConstr_btype(self, ctx:HaskellParser.Constr_btypeContext):
        pass

    # Exit a parse tree produced by HaskellParser#constr_btype.
    def exitConstr_btype(self, ctx:HaskellParser.Constr_btypeContext):
        pass


    # Enter a parse tree produced by HaskellParser#constr_tyapps.
    def enterConstr_tyapps(self, ctx:HaskellParser.Constr_tyappsContext):
        pass

    # Exit a parse tree produced by HaskellParser#constr_tyapps.
    def exitConstr_tyapps(self, ctx:HaskellParser.Constr_tyappsContext):
        pass


    # Enter a parse tree produced by HaskellParser#constr_tyapp.
    def enterConstr_tyapp(self, ctx:HaskellParser.Constr_tyappContext):
        pass

    # Exit a parse tree produced by HaskellParser#constr_tyapp.
    def exitConstr_tyapp(self, ctx:HaskellParser.Constr_tyappContext):
        pass


    # Enter a parse tree produced by HaskellParser#btype.
    def enterBtype(self, ctx:HaskellParser.BtypeContext):
        pass

    # Exit a parse tree produced by HaskellParser#btype.
    def exitBtype(self, ctx:HaskellParser.BtypeContext):
        pass


    # Enter a parse tree produced by HaskellParser#tyapps.
    def enterTyapps(self, ctx:HaskellParser.TyappsContext):
        pass

    # Exit a parse tree produced by HaskellParser#tyapps.
    def exitTyapps(self, ctx:HaskellParser.TyappsContext):
        pass


    # Enter a parse tree produced by HaskellParser#tyapp.
    def enterTyapp(self, ctx:HaskellParser.TyappContext):
        pass

    # Exit a parse tree produced by HaskellParser#tyapp.
    def exitTyapp(self, ctx:HaskellParser.TyappContext):
        pass


    # Enter a parse tree produced by HaskellParser#atype.
    def enterAtype(self, ctx:HaskellParser.AtypeContext):
        pass

    # Exit a parse tree produced by HaskellParser#atype.
    def exitAtype(self, ctx:HaskellParser.AtypeContext):
        pass


    # Enter a parse tree produced by HaskellParser#inst_type.
    def enterInst_type(self, ctx:HaskellParser.Inst_typeContext):
        pass

    # Exit a parse tree produced by HaskellParser#inst_type.
    def exitInst_type(self, ctx:HaskellParser.Inst_typeContext):
        pass


    # Enter a parse tree produced by HaskellParser#deriv_types.
    def enterDeriv_types(self, ctx:HaskellParser.Deriv_typesContext):
        pass

    # Exit a parse tree produced by HaskellParser#deriv_types.
    def exitDeriv_types(self, ctx:HaskellParser.Deriv_typesContext):
        pass


    # Enter a parse tree produced by HaskellParser#comma_types.
    def enterComma_types(self, ctx:HaskellParser.Comma_typesContext):
        pass

    # Exit a parse tree produced by HaskellParser#comma_types.
    def exitComma_types(self, ctx:HaskellParser.Comma_typesContext):
        pass


    # Enter a parse tree produced by HaskellParser#bar_types2.
    def enterBar_types2(self, ctx:HaskellParser.Bar_types2Context):
        pass

    # Exit a parse tree produced by HaskellParser#bar_types2.
    def exitBar_types2(self, ctx:HaskellParser.Bar_types2Context):
        pass


    # Enter a parse tree produced by HaskellParser#tv_bndrs.
    def enterTv_bndrs(self, ctx:HaskellParser.Tv_bndrsContext):
        pass

    # Exit a parse tree produced by HaskellParser#tv_bndrs.
    def exitTv_bndrs(self, ctx:HaskellParser.Tv_bndrsContext):
        pass


    # Enter a parse tree produced by HaskellParser#tv_bndr.
    def enterTv_bndr(self, ctx:HaskellParser.Tv_bndrContext):
        pass

    # Exit a parse tree produced by HaskellParser#tv_bndr.
    def exitTv_bndr(self, ctx:HaskellParser.Tv_bndrContext):
        pass


    # Enter a parse tree produced by HaskellParser#tv_bndr_no_braces.
    def enterTv_bndr_no_braces(self, ctx:HaskellParser.Tv_bndr_no_bracesContext):
        pass

    # Exit a parse tree produced by HaskellParser#tv_bndr_no_braces.
    def exitTv_bndr_no_braces(self, ctx:HaskellParser.Tv_bndr_no_bracesContext):
        pass


    # Enter a parse tree produced by HaskellParser#fds.
    def enterFds(self, ctx:HaskellParser.FdsContext):
        pass

    # Exit a parse tree produced by HaskellParser#fds.
    def exitFds(self, ctx:HaskellParser.FdsContext):
        pass


    # Enter a parse tree produced by HaskellParser#fds1.
    def enterFds1(self, ctx:HaskellParser.Fds1Context):
        pass

    # Exit a parse tree produced by HaskellParser#fds1.
    def exitFds1(self, ctx:HaskellParser.Fds1Context):
        pass


    # Enter a parse tree produced by HaskellParser#fd.
    def enterFd(self, ctx:HaskellParser.FdContext):
        pass

    # Exit a parse tree produced by HaskellParser#fd.
    def exitFd(self, ctx:HaskellParser.FdContext):
        pass


    # Enter a parse tree produced by HaskellParser#varids0.
    def enterVarids0(self, ctx:HaskellParser.Varids0Context):
        pass

    # Exit a parse tree produced by HaskellParser#varids0.
    def exitVarids0(self, ctx:HaskellParser.Varids0Context):
        pass


    # Enter a parse tree produced by HaskellParser#kind.
    def enterKind(self, ctx:HaskellParser.KindContext):
        pass

    # Exit a parse tree produced by HaskellParser#kind.
    def exitKind(self, ctx:HaskellParser.KindContext):
        pass


    # Enter a parse tree produced by HaskellParser#gadt_constrlist.
    def enterGadt_constrlist(self, ctx:HaskellParser.Gadt_constrlistContext):
        pass

    # Exit a parse tree produced by HaskellParser#gadt_constrlist.
    def exitGadt_constrlist(self, ctx:HaskellParser.Gadt_constrlistContext):
        pass


    # Enter a parse tree produced by HaskellParser#gadt_constrs.
    def enterGadt_constrs(self, ctx:HaskellParser.Gadt_constrsContext):
        pass

    # Exit a parse tree produced by HaskellParser#gadt_constrs.
    def exitGadt_constrs(self, ctx:HaskellParser.Gadt_constrsContext):
        pass


    # Enter a parse tree produced by HaskellParser#gadt_constr_with_doc.
    def enterGadt_constr_with_doc(self, ctx:HaskellParser.Gadt_constr_with_docContext):
        pass

    # Exit a parse tree produced by HaskellParser#gadt_constr_with_doc.
    def exitGadt_constr_with_doc(self, ctx:HaskellParser.Gadt_constr_with_docContext):
        pass


    # Enter a parse tree produced by HaskellParser#gadt_constr.
    def enterGadt_constr(self, ctx:HaskellParser.Gadt_constrContext):
        pass

    # Exit a parse tree produced by HaskellParser#gadt_constr.
    def exitGadt_constr(self, ctx:HaskellParser.Gadt_constrContext):
        pass


    # Enter a parse tree produced by HaskellParser#constrs.
    def enterConstrs(self, ctx:HaskellParser.ConstrsContext):
        pass

    # Exit a parse tree produced by HaskellParser#constrs.
    def exitConstrs(self, ctx:HaskellParser.ConstrsContext):
        pass


    # Enter a parse tree produced by HaskellParser#constrs1.
    def enterConstrs1(self, ctx:HaskellParser.Constrs1Context):
        pass

    # Exit a parse tree produced by HaskellParser#constrs1.
    def exitConstrs1(self, ctx:HaskellParser.Constrs1Context):
        pass


    # Enter a parse tree produced by HaskellParser#constr.
    def enterConstr(self, ctx:HaskellParser.ConstrContext):
        pass

    # Exit a parse tree produced by HaskellParser#constr.
    def exitConstr(self, ctx:HaskellParser.ConstrContext):
        pass


    # Enter a parse tree produced by HaskellParser#forall.
    def enterForall(self, ctx:HaskellParser.ForallContext):
        pass

    # Exit a parse tree produced by HaskellParser#forall.
    def exitForall(self, ctx:HaskellParser.ForallContext):
        pass


    # Enter a parse tree produced by HaskellParser#constr_stuff.
    def enterConstr_stuff(self, ctx:HaskellParser.Constr_stuffContext):
        pass

    # Exit a parse tree produced by HaskellParser#constr_stuff.
    def exitConstr_stuff(self, ctx:HaskellParser.Constr_stuffContext):
        pass


    # Enter a parse tree produced by HaskellParser#fielddecls.
    def enterFielddecls(self, ctx:HaskellParser.FielddeclsContext):
        pass

    # Exit a parse tree produced by HaskellParser#fielddecls.
    def exitFielddecls(self, ctx:HaskellParser.FielddeclsContext):
        pass


    # Enter a parse tree produced by HaskellParser#fielddecl.
    def enterFielddecl(self, ctx:HaskellParser.FielddeclContext):
        pass

    # Exit a parse tree produced by HaskellParser#fielddecl.
    def exitFielddecl(self, ctx:HaskellParser.FielddeclContext):
        pass


    # Enter a parse tree produced by HaskellParser#derivings.
    def enterDerivings(self, ctx:HaskellParser.DerivingsContext):
        pass

    # Exit a parse tree produced by HaskellParser#derivings.
    def exitDerivings(self, ctx:HaskellParser.DerivingsContext):
        pass


    # Enter a parse tree produced by HaskellParser#deriving.
    def enterDeriving(self, ctx:HaskellParser.DerivingContext):
        pass

    # Exit a parse tree produced by HaskellParser#deriving.
    def exitDeriving(self, ctx:HaskellParser.DerivingContext):
        pass


    # Enter a parse tree produced by HaskellParser#deriv_clause_types.
    def enterDeriv_clause_types(self, ctx:HaskellParser.Deriv_clause_typesContext):
        pass

    # Exit a parse tree produced by HaskellParser#deriv_clause_types.
    def exitDeriv_clause_types(self, ctx:HaskellParser.Deriv_clause_typesContext):
        pass


    # Enter a parse tree produced by HaskellParser#decl_no_th.
    def enterDecl_no_th(self, ctx:HaskellParser.Decl_no_thContext):
        pass

    # Exit a parse tree produced by HaskellParser#decl_no_th.
    def exitDecl_no_th(self, ctx:HaskellParser.Decl_no_thContext):
        pass


    # Enter a parse tree produced by HaskellParser#decl.
    def enterDecl(self, ctx:HaskellParser.DeclContext):
        pass

    # Exit a parse tree produced by HaskellParser#decl.
    def exitDecl(self, ctx:HaskellParser.DeclContext):
        pass


    # Enter a parse tree produced by HaskellParser#rhs.
    def enterRhs(self, ctx:HaskellParser.RhsContext):
        pass

    # Exit a parse tree produced by HaskellParser#rhs.
    def exitRhs(self, ctx:HaskellParser.RhsContext):
        pass


    # Enter a parse tree produced by HaskellParser#gdrhs.
    def enterGdrhs(self, ctx:HaskellParser.GdrhsContext):
        pass

    # Exit a parse tree produced by HaskellParser#gdrhs.
    def exitGdrhs(self, ctx:HaskellParser.GdrhsContext):
        pass


    # Enter a parse tree produced by HaskellParser#gdrh.
    def enterGdrh(self, ctx:HaskellParser.GdrhContext):
        pass

    # Exit a parse tree produced by HaskellParser#gdrh.
    def exitGdrh(self, ctx:HaskellParser.GdrhContext):
        pass


    # Enter a parse tree produced by HaskellParser#sigdecl.
    def enterSigdecl(self, ctx:HaskellParser.SigdeclContext):
        pass

    # Exit a parse tree produced by HaskellParser#sigdecl.
    def exitSigdecl(self, ctx:HaskellParser.SigdeclContext):
        pass


    # Enter a parse tree produced by HaskellParser#activation.
    def enterActivation(self, ctx:HaskellParser.ActivationContext):
        pass

    # Exit a parse tree produced by HaskellParser#activation.
    def exitActivation(self, ctx:HaskellParser.ActivationContext):
        pass


    # Enter a parse tree produced by HaskellParser#th_quasiquote.
    def enterTh_quasiquote(self, ctx:HaskellParser.Th_quasiquoteContext):
        pass

    # Exit a parse tree produced by HaskellParser#th_quasiquote.
    def exitTh_quasiquote(self, ctx:HaskellParser.Th_quasiquoteContext):
        pass


    # Enter a parse tree produced by HaskellParser#th_qquasiquote.
    def enterTh_qquasiquote(self, ctx:HaskellParser.Th_qquasiquoteContext):
        pass

    # Exit a parse tree produced by HaskellParser#th_qquasiquote.
    def exitTh_qquasiquote(self, ctx:HaskellParser.Th_qquasiquoteContext):
        pass


    # Enter a parse tree produced by HaskellParser#quasiquote.
    def enterQuasiquote(self, ctx:HaskellParser.QuasiquoteContext):
        pass

    # Exit a parse tree produced by HaskellParser#quasiquote.
    def exitQuasiquote(self, ctx:HaskellParser.QuasiquoteContext):
        pass


    # Enter a parse tree produced by HaskellParser#exp.
    def enterExp(self, ctx:HaskellParser.ExpContext):
        pass

    # Exit a parse tree produced by HaskellParser#exp.
    def exitExp(self, ctx:HaskellParser.ExpContext):
        pass


    # Enter a parse tree produced by HaskellParser#infixexp.
    def enterInfixexp(self, ctx:HaskellParser.InfixexpContext):
        pass

    # Exit a parse tree produced by HaskellParser#infixexp.
    def exitInfixexp(self, ctx:HaskellParser.InfixexpContext):
        pass


    # Enter a parse tree produced by HaskellParser#exp10p.
    def enterExp10p(self, ctx:HaskellParser.Exp10pContext):
        pass

    # Exit a parse tree produced by HaskellParser#exp10p.
    def exitExp10p(self, ctx:HaskellParser.Exp10pContext):
        pass


    # Enter a parse tree produced by HaskellParser#exp10.
    def enterExp10(self, ctx:HaskellParser.Exp10Context):
        pass

    # Exit a parse tree produced by HaskellParser#exp10.
    def exitExp10(self, ctx:HaskellParser.Exp10Context):
        pass


    # Enter a parse tree produced by HaskellParser#fexp.
    def enterFexp(self, ctx:HaskellParser.FexpContext):
        pass

    # Exit a parse tree produced by HaskellParser#fexp.
    def exitFexp(self, ctx:HaskellParser.FexpContext):
        pass


    # Enter a parse tree produced by HaskellParser#aexp.
    def enterAexp(self, ctx:HaskellParser.AexpContext):
        pass

    # Exit a parse tree produced by HaskellParser#aexp.
    def exitAexp(self, ctx:HaskellParser.AexpContext):
        pass


    # Enter a parse tree produced by HaskellParser#aexp1.
    def enterAexp1(self, ctx:HaskellParser.Aexp1Context):
        pass

    # Exit a parse tree produced by HaskellParser#aexp1.
    def exitAexp1(self, ctx:HaskellParser.Aexp1Context):
        pass


    # Enter a parse tree produced by HaskellParser#aexp2.
    def enterAexp2(self, ctx:HaskellParser.Aexp2Context):
        pass

    # Exit a parse tree produced by HaskellParser#aexp2.
    def exitAexp2(self, ctx:HaskellParser.Aexp2Context):
        pass


    # Enter a parse tree produced by HaskellParser#splice_exp.
    def enterSplice_exp(self, ctx:HaskellParser.Splice_expContext):
        pass

    # Exit a parse tree produced by HaskellParser#splice_exp.
    def exitSplice_exp(self, ctx:HaskellParser.Splice_expContext):
        pass


    # Enter a parse tree produced by HaskellParser#splice_untyped.
    def enterSplice_untyped(self, ctx:HaskellParser.Splice_untypedContext):
        pass

    # Exit a parse tree produced by HaskellParser#splice_untyped.
    def exitSplice_untyped(self, ctx:HaskellParser.Splice_untypedContext):
        pass


    # Enter a parse tree produced by HaskellParser#splice_typed.
    def enterSplice_typed(self, ctx:HaskellParser.Splice_typedContext):
        pass

    # Exit a parse tree produced by HaskellParser#splice_typed.
    def exitSplice_typed(self, ctx:HaskellParser.Splice_typedContext):
        pass


    # Enter a parse tree produced by HaskellParser#cmdargs.
    def enterCmdargs(self, ctx:HaskellParser.CmdargsContext):
        pass

    # Exit a parse tree produced by HaskellParser#cmdargs.
    def exitCmdargs(self, ctx:HaskellParser.CmdargsContext):
        pass


    # Enter a parse tree produced by HaskellParser#acmd.
    def enterAcmd(self, ctx:HaskellParser.AcmdContext):
        pass

    # Exit a parse tree produced by HaskellParser#acmd.
    def exitAcmd(self, ctx:HaskellParser.AcmdContext):
        pass


    # Enter a parse tree produced by HaskellParser#cvtopbody.
    def enterCvtopbody(self, ctx:HaskellParser.CvtopbodyContext):
        pass

    # Exit a parse tree produced by HaskellParser#cvtopbody.
    def exitCvtopbody(self, ctx:HaskellParser.CvtopbodyContext):
        pass


    # Enter a parse tree produced by HaskellParser#cvtopdecls0.
    def enterCvtopdecls0(self, ctx:HaskellParser.Cvtopdecls0Context):
        pass

    # Exit a parse tree produced by HaskellParser#cvtopdecls0.
    def exitCvtopdecls0(self, ctx:HaskellParser.Cvtopdecls0Context):
        pass


    # Enter a parse tree produced by HaskellParser#texp.
    def enterTexp(self, ctx:HaskellParser.TexpContext):
        pass

    # Exit a parse tree produced by HaskellParser#texp.
    def exitTexp(self, ctx:HaskellParser.TexpContext):
        pass


    # Enter a parse tree produced by HaskellParser#tup_exprs.
    def enterTup_exprs(self, ctx:HaskellParser.Tup_exprsContext):
        pass

    # Exit a parse tree produced by HaskellParser#tup_exprs.
    def exitTup_exprs(self, ctx:HaskellParser.Tup_exprsContext):
        pass


    # Enter a parse tree produced by HaskellParser#commas_tup_tail.
    def enterCommas_tup_tail(self, ctx:HaskellParser.Commas_tup_tailContext):
        pass

    # Exit a parse tree produced by HaskellParser#commas_tup_tail.
    def exitCommas_tup_tail(self, ctx:HaskellParser.Commas_tup_tailContext):
        pass


    # Enter a parse tree produced by HaskellParser#tup_tail.
    def enterTup_tail(self, ctx:HaskellParser.Tup_tailContext):
        pass

    # Exit a parse tree produced by HaskellParser#tup_tail.
    def exitTup_tail(self, ctx:HaskellParser.Tup_tailContext):
        pass


    # Enter a parse tree produced by HaskellParser#lst.
    def enterLst(self, ctx:HaskellParser.LstContext):
        pass

    # Exit a parse tree produced by HaskellParser#lst.
    def exitLst(self, ctx:HaskellParser.LstContext):
        pass


    # Enter a parse tree produced by HaskellParser#lexps.
    def enterLexps(self, ctx:HaskellParser.LexpsContext):
        pass

    # Exit a parse tree produced by HaskellParser#lexps.
    def exitLexps(self, ctx:HaskellParser.LexpsContext):
        pass


    # Enter a parse tree produced by HaskellParser#flattenedpquals.
    def enterFlattenedpquals(self, ctx:HaskellParser.FlattenedpqualsContext):
        pass

    # Exit a parse tree produced by HaskellParser#flattenedpquals.
    def exitFlattenedpquals(self, ctx:HaskellParser.FlattenedpqualsContext):
        pass


    # Enter a parse tree produced by HaskellParser#pquals.
    def enterPquals(self, ctx:HaskellParser.PqualsContext):
        pass

    # Exit a parse tree produced by HaskellParser#pquals.
    def exitPquals(self, ctx:HaskellParser.PqualsContext):
        pass


    # Enter a parse tree produced by HaskellParser#squals.
    def enterSquals(self, ctx:HaskellParser.SqualsContext):
        pass

    # Exit a parse tree produced by HaskellParser#squals.
    def exitSquals(self, ctx:HaskellParser.SqualsContext):
        pass


    # Enter a parse tree produced by HaskellParser#transformqual.
    def enterTransformqual(self, ctx:HaskellParser.TransformqualContext):
        pass

    # Exit a parse tree produced by HaskellParser#transformqual.
    def exitTransformqual(self, ctx:HaskellParser.TransformqualContext):
        pass


    # Enter a parse tree produced by HaskellParser#guards.
    def enterGuards(self, ctx:HaskellParser.GuardsContext):
        pass

    # Exit a parse tree produced by HaskellParser#guards.
    def exitGuards(self, ctx:HaskellParser.GuardsContext):
        pass


    # Enter a parse tree produced by HaskellParser#guard.
    def enterGuard(self, ctx:HaskellParser.GuardContext):
        pass

    # Exit a parse tree produced by HaskellParser#guard.
    def exitGuard(self, ctx:HaskellParser.GuardContext):
        pass


    # Enter a parse tree produced by HaskellParser#alts.
    def enterAlts(self, ctx:HaskellParser.AltsContext):
        pass

    # Exit a parse tree produced by HaskellParser#alts.
    def exitAlts(self, ctx:HaskellParser.AltsContext):
        pass


    # Enter a parse tree produced by HaskellParser#alt.
    def enterAlt(self, ctx:HaskellParser.AltContext):
        pass

    # Exit a parse tree produced by HaskellParser#alt.
    def exitAlt(self, ctx:HaskellParser.AltContext):
        pass


    # Enter a parse tree produced by HaskellParser#alt_rhs.
    def enterAlt_rhs(self, ctx:HaskellParser.Alt_rhsContext):
        pass

    # Exit a parse tree produced by HaskellParser#alt_rhs.
    def exitAlt_rhs(self, ctx:HaskellParser.Alt_rhsContext):
        pass


    # Enter a parse tree produced by HaskellParser#ralt.
    def enterRalt(self, ctx:HaskellParser.RaltContext):
        pass

    # Exit a parse tree produced by HaskellParser#ralt.
    def exitRalt(self, ctx:HaskellParser.RaltContext):
        pass


    # Enter a parse tree produced by HaskellParser#gdpats.
    def enterGdpats(self, ctx:HaskellParser.GdpatsContext):
        pass

    # Exit a parse tree produced by HaskellParser#gdpats.
    def exitGdpats(self, ctx:HaskellParser.GdpatsContext):
        pass


    # Enter a parse tree produced by HaskellParser#ifgdpats.
    def enterIfgdpats(self, ctx:HaskellParser.IfgdpatsContext):
        pass

    # Exit a parse tree produced by HaskellParser#ifgdpats.
    def exitIfgdpats(self, ctx:HaskellParser.IfgdpatsContext):
        pass


    # Enter a parse tree produced by HaskellParser#gdpat.
    def enterGdpat(self, ctx:HaskellParser.GdpatContext):
        pass

    # Exit a parse tree produced by HaskellParser#gdpat.
    def exitGdpat(self, ctx:HaskellParser.GdpatContext):
        pass


    # Enter a parse tree produced by HaskellParser#pat.
    def enterPat(self, ctx:HaskellParser.PatContext):
        pass

    # Exit a parse tree produced by HaskellParser#pat.
    def exitPat(self, ctx:HaskellParser.PatContext):
        pass


    # Enter a parse tree produced by HaskellParser#bindpat.
    def enterBindpat(self, ctx:HaskellParser.BindpatContext):
        pass

    # Exit a parse tree produced by HaskellParser#bindpat.
    def exitBindpat(self, ctx:HaskellParser.BindpatContext):
        pass


    # Enter a parse tree produced by HaskellParser#apat.
    def enterApat(self, ctx:HaskellParser.ApatContext):
        pass

    # Exit a parse tree produced by HaskellParser#apat.
    def exitApat(self, ctx:HaskellParser.ApatContext):
        pass


    # Enter a parse tree produced by HaskellParser#apats.
    def enterApats(self, ctx:HaskellParser.ApatsContext):
        pass

    # Exit a parse tree produced by HaskellParser#apats.
    def exitApats(self, ctx:HaskellParser.ApatsContext):
        pass


    # Enter a parse tree produced by HaskellParser#fpat.
    def enterFpat(self, ctx:HaskellParser.FpatContext):
        pass

    # Exit a parse tree produced by HaskellParser#fpat.
    def exitFpat(self, ctx:HaskellParser.FpatContext):
        pass


    # Enter a parse tree produced by HaskellParser#stmtlist.
    def enterStmtlist(self, ctx:HaskellParser.StmtlistContext):
        pass

    # Exit a parse tree produced by HaskellParser#stmtlist.
    def exitStmtlist(self, ctx:HaskellParser.StmtlistContext):
        pass


    # Enter a parse tree produced by HaskellParser#stmts.
    def enterStmts(self, ctx:HaskellParser.StmtsContext):
        pass

    # Exit a parse tree produced by HaskellParser#stmts.
    def exitStmts(self, ctx:HaskellParser.StmtsContext):
        pass


    # Enter a parse tree produced by HaskellParser#stmt.
    def enterStmt(self, ctx:HaskellParser.StmtContext):
        pass

    # Exit a parse tree produced by HaskellParser#stmt.
    def exitStmt(self, ctx:HaskellParser.StmtContext):
        pass


    # Enter a parse tree produced by HaskellParser#qual.
    def enterQual(self, ctx:HaskellParser.QualContext):
        pass

    # Exit a parse tree produced by HaskellParser#qual.
    def exitQual(self, ctx:HaskellParser.QualContext):
        pass


    # Enter a parse tree produced by HaskellParser#fbinds.
    def enterFbinds(self, ctx:HaskellParser.FbindsContext):
        pass

    # Exit a parse tree produced by HaskellParser#fbinds.
    def exitFbinds(self, ctx:HaskellParser.FbindsContext):
        pass


    # Enter a parse tree produced by HaskellParser#fbind.
    def enterFbind(self, ctx:HaskellParser.FbindContext):
        pass

    # Exit a parse tree produced by HaskellParser#fbind.
    def exitFbind(self, ctx:HaskellParser.FbindContext):
        pass


    # Enter a parse tree produced by HaskellParser#dbinds.
    def enterDbinds(self, ctx:HaskellParser.DbindsContext):
        pass

    # Exit a parse tree produced by HaskellParser#dbinds.
    def exitDbinds(self, ctx:HaskellParser.DbindsContext):
        pass


    # Enter a parse tree produced by HaskellParser#dbind.
    def enterDbind(self, ctx:HaskellParser.DbindContext):
        pass

    # Exit a parse tree produced by HaskellParser#dbind.
    def exitDbind(self, ctx:HaskellParser.DbindContext):
        pass


    # Enter a parse tree produced by HaskellParser#name_boolformula_opt.
    def enterName_boolformula_opt(self, ctx:HaskellParser.Name_boolformula_optContext):
        pass

    # Exit a parse tree produced by HaskellParser#name_boolformula_opt.
    def exitName_boolformula_opt(self, ctx:HaskellParser.Name_boolformula_optContext):
        pass


    # Enter a parse tree produced by HaskellParser#name_boolformula_and.
    def enterName_boolformula_and(self, ctx:HaskellParser.Name_boolformula_andContext):
        pass

    # Exit a parse tree produced by HaskellParser#name_boolformula_and.
    def exitName_boolformula_and(self, ctx:HaskellParser.Name_boolformula_andContext):
        pass


    # Enter a parse tree produced by HaskellParser#name_boolformula_and_list.
    def enterName_boolformula_and_list(self, ctx:HaskellParser.Name_boolformula_and_listContext):
        pass

    # Exit a parse tree produced by HaskellParser#name_boolformula_and_list.
    def exitName_boolformula_and_list(self, ctx:HaskellParser.Name_boolformula_and_listContext):
        pass


    # Enter a parse tree produced by HaskellParser#name_boolformula_atom.
    def enterName_boolformula_atom(self, ctx:HaskellParser.Name_boolformula_atomContext):
        pass

    # Exit a parse tree produced by HaskellParser#name_boolformula_atom.
    def exitName_boolformula_atom(self, ctx:HaskellParser.Name_boolformula_atomContext):
        pass


    # Enter a parse tree produced by HaskellParser#namelist.
    def enterNamelist(self, ctx:HaskellParser.NamelistContext):
        pass

    # Exit a parse tree produced by HaskellParser#namelist.
    def exitNamelist(self, ctx:HaskellParser.NamelistContext):
        pass


    # Enter a parse tree produced by HaskellParser#name_var.
    def enterName_var(self, ctx:HaskellParser.Name_varContext):
        pass

    # Exit a parse tree produced by HaskellParser#name_var.
    def exitName_var(self, ctx:HaskellParser.Name_varContext):
        pass


    # Enter a parse tree produced by HaskellParser#qcon_nowiredlist.
    def enterQcon_nowiredlist(self, ctx:HaskellParser.Qcon_nowiredlistContext):
        pass

    # Exit a parse tree produced by HaskellParser#qcon_nowiredlist.
    def exitQcon_nowiredlist(self, ctx:HaskellParser.Qcon_nowiredlistContext):
        pass


    # Enter a parse tree produced by HaskellParser#qcon.
    def enterQcon(self, ctx:HaskellParser.QconContext):
        pass

    # Exit a parse tree produced by HaskellParser#qcon.
    def exitQcon(self, ctx:HaskellParser.QconContext):
        pass


    # Enter a parse tree produced by HaskellParser#gen_qcon.
    def enterGen_qcon(self, ctx:HaskellParser.Gen_qconContext):
        pass

    # Exit a parse tree produced by HaskellParser#gen_qcon.
    def exitGen_qcon(self, ctx:HaskellParser.Gen_qconContext):
        pass


    # Enter a parse tree produced by HaskellParser#con.
    def enterCon(self, ctx:HaskellParser.ConContext):
        pass

    # Exit a parse tree produced by HaskellParser#con.
    def exitCon(self, ctx:HaskellParser.ConContext):
        pass


    # Enter a parse tree produced by HaskellParser#con_list.
    def enterCon_list(self, ctx:HaskellParser.Con_listContext):
        pass

    # Exit a parse tree produced by HaskellParser#con_list.
    def exitCon_list(self, ctx:HaskellParser.Con_listContext):
        pass


    # Enter a parse tree produced by HaskellParser#sysdcon_nolist.
    def enterSysdcon_nolist(self, ctx:HaskellParser.Sysdcon_nolistContext):
        pass

    # Exit a parse tree produced by HaskellParser#sysdcon_nolist.
    def exitSysdcon_nolist(self, ctx:HaskellParser.Sysdcon_nolistContext):
        pass


    # Enter a parse tree produced by HaskellParser#sysdcon.
    def enterSysdcon(self, ctx:HaskellParser.SysdconContext):
        pass

    # Exit a parse tree produced by HaskellParser#sysdcon.
    def exitSysdcon(self, ctx:HaskellParser.SysdconContext):
        pass


    # Enter a parse tree produced by HaskellParser#conop.
    def enterConop(self, ctx:HaskellParser.ConopContext):
        pass

    # Exit a parse tree produced by HaskellParser#conop.
    def exitConop(self, ctx:HaskellParser.ConopContext):
        pass


    # Enter a parse tree produced by HaskellParser#qconop.
    def enterQconop(self, ctx:HaskellParser.QconopContext):
        pass

    # Exit a parse tree produced by HaskellParser#qconop.
    def exitQconop(self, ctx:HaskellParser.QconopContext):
        pass


    # Enter a parse tree produced by HaskellParser#gconsym.
    def enterGconsym(self, ctx:HaskellParser.GconsymContext):
        pass

    # Exit a parse tree produced by HaskellParser#gconsym.
    def exitGconsym(self, ctx:HaskellParser.GconsymContext):
        pass


    # Enter a parse tree produced by HaskellParser#gtycon.
    def enterGtycon(self, ctx:HaskellParser.GtyconContext):
        pass

    # Exit a parse tree produced by HaskellParser#gtycon.
    def exitGtycon(self, ctx:HaskellParser.GtyconContext):
        pass


    # Enter a parse tree produced by HaskellParser#ntgtycon.
    def enterNtgtycon(self, ctx:HaskellParser.NtgtyconContext):
        pass

    # Exit a parse tree produced by HaskellParser#ntgtycon.
    def exitNtgtycon(self, ctx:HaskellParser.NtgtyconContext):
        pass


    # Enter a parse tree produced by HaskellParser#oqtycon.
    def enterOqtycon(self, ctx:HaskellParser.OqtyconContext):
        pass

    # Exit a parse tree produced by HaskellParser#oqtycon.
    def exitOqtycon(self, ctx:HaskellParser.OqtyconContext):
        pass


    # Enter a parse tree produced by HaskellParser#qtyconop.
    def enterQtyconop(self, ctx:HaskellParser.QtyconopContext):
        pass

    # Exit a parse tree produced by HaskellParser#qtyconop.
    def exitQtyconop(self, ctx:HaskellParser.QtyconopContext):
        pass


    # Enter a parse tree produced by HaskellParser#qtycon.
    def enterQtycon(self, ctx:HaskellParser.QtyconContext):
        pass

    # Exit a parse tree produced by HaskellParser#qtycon.
    def exitQtycon(self, ctx:HaskellParser.QtyconContext):
        pass


    # Enter a parse tree produced by HaskellParser#tycon.
    def enterTycon(self, ctx:HaskellParser.TyconContext):
        pass

    # Exit a parse tree produced by HaskellParser#tycon.
    def exitTycon(self, ctx:HaskellParser.TyconContext):
        pass


    # Enter a parse tree produced by HaskellParser#qtyconsym.
    def enterQtyconsym(self, ctx:HaskellParser.QtyconsymContext):
        pass

    # Exit a parse tree produced by HaskellParser#qtyconsym.
    def exitQtyconsym(self, ctx:HaskellParser.QtyconsymContext):
        pass


    # Enter a parse tree produced by HaskellParser#tyconsym.
    def enterTyconsym(self, ctx:HaskellParser.TyconsymContext):
        pass

    # Exit a parse tree produced by HaskellParser#tyconsym.
    def exitTyconsym(self, ctx:HaskellParser.TyconsymContext):
        pass


    # Enter a parse tree produced by HaskellParser#op.
    def enterOp(self, ctx:HaskellParser.OpContext):
        pass

    # Exit a parse tree produced by HaskellParser#op.
    def exitOp(self, ctx:HaskellParser.OpContext):
        pass


    # Enter a parse tree produced by HaskellParser#varop.
    def enterVarop(self, ctx:HaskellParser.VaropContext):
        pass

    # Exit a parse tree produced by HaskellParser#varop.
    def exitVarop(self, ctx:HaskellParser.VaropContext):
        pass


    # Enter a parse tree produced by HaskellParser#qop.
    def enterQop(self, ctx:HaskellParser.QopContext):
        pass

    # Exit a parse tree produced by HaskellParser#qop.
    def exitQop(self, ctx:HaskellParser.QopContext):
        pass


    # Enter a parse tree produced by HaskellParser#qopm.
    def enterQopm(self, ctx:HaskellParser.QopmContext):
        pass

    # Exit a parse tree produced by HaskellParser#qopm.
    def exitQopm(self, ctx:HaskellParser.QopmContext):
        pass


    # Enter a parse tree produced by HaskellParser#hole_op.
    def enterHole_op(self, ctx:HaskellParser.Hole_opContext):
        pass

    # Exit a parse tree produced by HaskellParser#hole_op.
    def exitHole_op(self, ctx:HaskellParser.Hole_opContext):
        pass


    # Enter a parse tree produced by HaskellParser#qvarop.
    def enterQvarop(self, ctx:HaskellParser.QvaropContext):
        pass

    # Exit a parse tree produced by HaskellParser#qvarop.
    def exitQvarop(self, ctx:HaskellParser.QvaropContext):
        pass


    # Enter a parse tree produced by HaskellParser#qvaropm.
    def enterQvaropm(self, ctx:HaskellParser.QvaropmContext):
        pass

    # Exit a parse tree produced by HaskellParser#qvaropm.
    def exitQvaropm(self, ctx:HaskellParser.QvaropmContext):
        pass


    # Enter a parse tree produced by HaskellParser#tyvar.
    def enterTyvar(self, ctx:HaskellParser.TyvarContext):
        pass

    # Exit a parse tree produced by HaskellParser#tyvar.
    def exitTyvar(self, ctx:HaskellParser.TyvarContext):
        pass


    # Enter a parse tree produced by HaskellParser#tyvarop.
    def enterTyvarop(self, ctx:HaskellParser.TyvaropContext):
        pass

    # Exit a parse tree produced by HaskellParser#tyvarop.
    def exitTyvarop(self, ctx:HaskellParser.TyvaropContext):
        pass


    # Enter a parse tree produced by HaskellParser#tyvarid.
    def enterTyvarid(self, ctx:HaskellParser.TyvaridContext):
        pass

    # Exit a parse tree produced by HaskellParser#tyvarid.
    def exitTyvarid(self, ctx:HaskellParser.TyvaridContext):
        pass


    # Enter a parse tree produced by HaskellParser#tycls.
    def enterTycls(self, ctx:HaskellParser.TyclsContext):
        pass

    # Exit a parse tree produced by HaskellParser#tycls.
    def exitTycls(self, ctx:HaskellParser.TyclsContext):
        pass


    # Enter a parse tree produced by HaskellParser#qtycls.
    def enterQtycls(self, ctx:HaskellParser.QtyclsContext):
        pass

    # Exit a parse tree produced by HaskellParser#qtycls.
    def exitQtycls(self, ctx:HaskellParser.QtyclsContext):
        pass


    # Enter a parse tree produced by HaskellParser#var.
    def enterVar(self, ctx:HaskellParser.VarContext):
        pass

    # Exit a parse tree produced by HaskellParser#var.
    def exitVar(self, ctx:HaskellParser.VarContext):
        pass


    # Enter a parse tree produced by HaskellParser#qvar.
    def enterQvar(self, ctx:HaskellParser.QvarContext):
        pass

    # Exit a parse tree produced by HaskellParser#qvar.
    def exitQvar(self, ctx:HaskellParser.QvarContext):
        pass


    # Enter a parse tree produced by HaskellParser#qvarid.
    def enterQvarid(self, ctx:HaskellParser.QvaridContext):
        pass

    # Exit a parse tree produced by HaskellParser#qvarid.
    def exitQvarid(self, ctx:HaskellParser.QvaridContext):
        pass


    # Enter a parse tree produced by HaskellParser#varid.
    def enterVarid(self, ctx:HaskellParser.VaridContext):
        pass

    # Exit a parse tree produced by HaskellParser#varid.
    def exitVarid(self, ctx:HaskellParser.VaridContext):
        pass


    # Enter a parse tree produced by HaskellParser#qvarsym.
    def enterQvarsym(self, ctx:HaskellParser.QvarsymContext):
        pass

    # Exit a parse tree produced by HaskellParser#qvarsym.
    def exitQvarsym(self, ctx:HaskellParser.QvarsymContext):
        pass


    # Enter a parse tree produced by HaskellParser#qvarsym_no_minus.
    def enterQvarsym_no_minus(self, ctx:HaskellParser.Qvarsym_no_minusContext):
        pass

    # Exit a parse tree produced by HaskellParser#qvarsym_no_minus.
    def exitQvarsym_no_minus(self, ctx:HaskellParser.Qvarsym_no_minusContext):
        pass


    # Enter a parse tree produced by HaskellParser#varsym.
    def enterVarsym(self, ctx:HaskellParser.VarsymContext):
        pass

    # Exit a parse tree produced by HaskellParser#varsym.
    def exitVarsym(self, ctx:HaskellParser.VarsymContext):
        pass


    # Enter a parse tree produced by HaskellParser#varsym_no_minus.
    def enterVarsym_no_minus(self, ctx:HaskellParser.Varsym_no_minusContext):
        pass

    # Exit a parse tree produced by HaskellParser#varsym_no_minus.
    def exitVarsym_no_minus(self, ctx:HaskellParser.Varsym_no_minusContext):
        pass


    # Enter a parse tree produced by HaskellParser#special_id.
    def enterSpecial_id(self, ctx:HaskellParser.Special_idContext):
        pass

    # Exit a parse tree produced by HaskellParser#special_id.
    def exitSpecial_id(self, ctx:HaskellParser.Special_idContext):
        pass


    # Enter a parse tree produced by HaskellParser#qconid.
    def enterQconid(self, ctx:HaskellParser.QconidContext):
        pass

    # Exit a parse tree produced by HaskellParser#qconid.
    def exitQconid(self, ctx:HaskellParser.QconidContext):
        pass


    # Enter a parse tree produced by HaskellParser#conid.
    def enterConid(self, ctx:HaskellParser.ConidContext):
        pass

    # Exit a parse tree produced by HaskellParser#conid.
    def exitConid(self, ctx:HaskellParser.ConidContext):
        pass


    # Enter a parse tree produced by HaskellParser#qconsym.
    def enterQconsym(self, ctx:HaskellParser.QconsymContext):
        pass

    # Exit a parse tree produced by HaskellParser#qconsym.
    def exitQconsym(self, ctx:HaskellParser.QconsymContext):
        pass


    # Enter a parse tree produced by HaskellParser#consym.
    def enterConsym(self, ctx:HaskellParser.ConsymContext):
        pass

    # Exit a parse tree produced by HaskellParser#consym.
    def exitConsym(self, ctx:HaskellParser.ConsymContext):
        pass


    # Enter a parse tree produced by HaskellParser#literal.
    def enterLiteral(self, ctx:HaskellParser.LiteralContext):
        pass

    # Exit a parse tree produced by HaskellParser#literal.
    def exitLiteral(self, ctx:HaskellParser.LiteralContext):
        pass


    # Enter a parse tree produced by HaskellParser#opn.
    def enterOpn(self, ctx:HaskellParser.OpnContext):
        pass

    # Exit a parse tree produced by HaskellParser#opn.
    def exitOpn(self, ctx:HaskellParser.OpnContext):
        pass


    # Enter a parse tree produced by HaskellParser#close.
    def enterClose(self, ctx:HaskellParser.CloseContext):
        pass

    # Exit a parse tree produced by HaskellParser#close.
    def exitClose(self, ctx:HaskellParser.CloseContext):
        pass


    # Enter a parse tree produced by HaskellParser#semi.
    def enterSemi(self, ctx:HaskellParser.SemiContext):
        pass

    # Exit a parse tree produced by HaskellParser#semi.
    def exitSemi(self, ctx:HaskellParser.SemiContext):
        pass


    # Enter a parse tree produced by HaskellParser#modid.
    def enterModid(self, ctx:HaskellParser.ModidContext):
        pass

    # Exit a parse tree produced by HaskellParser#modid.
    def exitModid(self, ctx:HaskellParser.ModidContext):
        pass


    # Enter a parse tree produced by HaskellParser#commas.
    def enterCommas(self, ctx:HaskellParser.CommasContext):
        pass

    # Exit a parse tree produced by HaskellParser#commas.
    def exitCommas(self, ctx:HaskellParser.CommasContext):
        pass


    # Enter a parse tree produced by HaskellParser#bars.
    def enterBars(self, ctx:HaskellParser.BarsContext):
        pass

    # Exit a parse tree produced by HaskellParser#bars.
    def exitBars(self, ctx:HaskellParser.BarsContext):
        pass


    # Enter a parse tree produced by HaskellParser#special.
    def enterSpecial(self, ctx:HaskellParser.SpecialContext):
        pass

    # Exit a parse tree produced by HaskellParser#special.
    def exitSpecial(self, ctx:HaskellParser.SpecialContext):
        pass


    # Enter a parse tree produced by HaskellParser#symbol.
    def enterSymbol(self, ctx:HaskellParser.SymbolContext):
        pass

    # Exit a parse tree produced by HaskellParser#symbol.
    def exitSymbol(self, ctx:HaskellParser.SymbolContext):
        pass


    # Enter a parse tree produced by HaskellParser#ascSymbol.
    def enterAscSymbol(self, ctx:HaskellParser.AscSymbolContext):
        pass

    # Exit a parse tree produced by HaskellParser#ascSymbol.
    def exitAscSymbol(self, ctx:HaskellParser.AscSymbolContext):
        pass


    # Enter a parse tree produced by HaskellParser#integer.
    def enterInteger(self, ctx:HaskellParser.IntegerContext):
        pass

    # Exit a parse tree produced by HaskellParser#integer.
    def exitInteger(self, ctx:HaskellParser.IntegerContext):
        pass


    # Enter a parse tree produced by HaskellParser#pfloat.
    def enterPfloat(self, ctx:HaskellParser.PfloatContext):
        pass

    # Exit a parse tree produced by HaskellParser#pfloat.
    def exitPfloat(self, ctx:HaskellParser.PfloatContext):
        pass


    # Enter a parse tree produced by HaskellParser#pchar.
    def enterPchar(self, ctx:HaskellParser.PcharContext):
        pass

    # Exit a parse tree produced by HaskellParser#pchar.
    def exitPchar(self, ctx:HaskellParser.PcharContext):
        pass


    # Enter a parse tree produced by HaskellParser#pstring.
    def enterPstring(self, ctx:HaskellParser.PstringContext):
        pass

    # Exit a parse tree produced by HaskellParser#pstring.
    def exitPstring(self, ctx:HaskellParser.PstringContext):
        pass



del HaskellParser